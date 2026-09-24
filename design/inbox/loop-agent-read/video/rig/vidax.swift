// vidax <pid> place x y w h   move/resize the app's first window (top-left origin)
// vidax <pid> rows            "<selected 0/1>\t<cx>\t<cy>\t<text>" for every AXRow with text
// vidax 0 click x y           move the pointer there and click once
// vidax 0 move x y            move the pointer
// vidax 0 display             asleep/awake
import ApplicationServices
import Foundation

func attr(_ e: AXUIElement, _ n: String) -> AnyObject? {
    var v: AnyObject?; return AXUIElementCopyAttributeValue(e, n as CFString, &v) == .success ? v : nil
}
func kids(_ e: AXUIElement) -> [AXUIElement] { (attr(e, kAXChildrenAttribute) as? [AXUIElement]) ?? [] }
func text(_ e: AXUIElement, _ d: Int = 0) -> String? {
    if d > 6 { return nil }
    let role = attr(e, kAXRoleAttribute) as? String
    if role == kAXStaticTextRole || role == kAXTextFieldRole, let s = attr(e, kAXValueAttribute) as? String, !s.isEmpty { return s }
    for k in kids(e) { if let s = text(k, d + 1) { return s } }
    return nil
}
func frame(_ e: AXUIElement) -> CGRect? {
    guard let p = attr(e, kAXPositionAttribute), let s = attr(e, kAXSizeAttribute) else { return nil }
    var pt = CGPoint.zero, sz = CGSize.zero
    AXValueGetValue(p as! AXValue, .cgPoint, &pt); AXValueGetValue(s as! AXValue, .cgSize, &sz)
    return CGRect(origin: pt, size: sz)
}
func rows(_ e: AXUIElement, _ d: Int = 0) -> [AXUIElement] {
    if d > 40 { return [] }
    if (attr(e, kAXRoleAttribute) as? String) == kAXRowRole { return [e] }
    return kids(e).flatMap { rows($0, d + 1) }
}
func click(_ x: Double, _ y: Double) {
    let p = CGPoint(x: x, y: y)
    CGEvent(mouseEventSource: nil, mouseType: .mouseMoved, mouseCursorPosition: p, mouseButton: .left)?.post(tap: .cghidEventTap)
    usleep(150_000)
    CGEvent(mouseEventSource: nil, mouseType: .leftMouseDown, mouseCursorPosition: p, mouseButton: .left)?.post(tap: .cghidEventTap)
    usleep(60_000)
    CGEvent(mouseEventSource: nil, mouseType: .leftMouseUp, mouseCursorPosition: p, mouseButton: .left)?.post(tap: .cghidEventTap)
}
let a = CommandLine.arguments
let pid = pid_t(a[1])!
switch a[2] {
case "display": print(CGDisplayIsAsleep(CGMainDisplayID()) != 0 ? "asleep" : "awake")
case "click": click(Double(a[3])!, Double(a[4])!)
case "move":
    CGEvent(mouseEventSource: nil, mouseType: .mouseMoved, mouseCursorPosition: CGPoint(x: Double(a[3])!, y: Double(a[4])!), mouseButton: .left)?.post(tap: .cghidEventTap)
case "place":
    let app = AXUIElementCreateApplication(pid)
    guard let w = (attr(app, kAXWindowsAttribute) as? [AXUIElement])?.first else { print("no window"); exit(1) }
    var pt = CGPoint(x: Double(a[3])!, y: Double(a[4])!), sz = CGSize(width: Double(a[5])!, height: Double(a[6])!)
    AXUIElementSetAttributeValue(w, kAXPositionAttribute as CFString, AXValueCreate(.cgPoint, &pt)!)
    AXUIElementSetAttributeValue(w, kAXSizeAttribute as CFString, AXValueCreate(.cgSize, &sz)!)
    print(frame(w).map { "\($0)" } ?? "?")
case "rows":
    let app = AXUIElementCreateApplication(pid)
    for w in (attr(app, kAXWindowsAttribute) as? [AXUIElement]) ?? [] {
        for r in rows(w) {
            guard let t = text(r), let f = frame(r), f.height > 0 else { continue }
            let sel = (attr(r, kAXSelectedAttribute) as? Bool) == true ? 1 : 0
            print("\(sel)\t\(Int(f.midX))\t\(Int(f.midY))\t\(t)")
        }
    }
case "zoomin":  // vidax <pid> zoomin n : Cmd-= n times, posted to the app
    for _ in 0..<Int(a[3])! {
        for down in [true, false] {
            let e = CGEvent(keyboardEventSource: nil, virtualKey: 24, keyDown: down)!
            e.flags = .maskCommand
            e.postToPid(pid)
        }
        usleep(400_000)
    }
case "zoomreset":  // Cmd-0, Actual Size
    for down in [true, false] {
        let e = CGEvent(keyboardEventSource: nil, virtualKey: 29, keyDown: down)!
        e.flags = .maskCommand
        e.postToPid(pid)
    }
    usleep(400_000)
case "glide":  // vidax 0 glide x y ms : smooth pointer move from where it is now
    let from = CGEvent(source: nil)!.location
    let to = CGPoint(x: Double(a[3])!, y: Double(a[4])!)
    let ms = Double(a[5]) ?? 600
    let n = max(1, Int(ms / 12))
    for i in 1...n {
        let t = Double(i) / Double(n)
        let e = t < 0.5 ? 2 * t * t : 1 - pow(-2 * t + 2, 2) / 2
        let p = CGPoint(x: from.x + (to.x - from.x) * e, y: from.y + (to.y - from.y) * e)
        CGEvent(mouseEventSource: nil, mouseType: .mouseMoved, mouseCursorPosition: p, mouseButton: .left)?.post(tap: .cghidEventTap)
        usleep(12_000)
    }
case "dclick":  // vidax 0 dclick x y : double-click in place
    let p = CGPoint(x: Double(a[3])!, y: Double(a[4])!)
    for n in 1...2 {
        for type in [CGEventType.leftMouseDown, .leftMouseUp] {
            let e = CGEvent(mouseEventSource: nil, mouseType: type, mouseCursorPosition: p, mouseButton: .left)!
            e.setIntegerValueField(.mouseEventClickState, value: Int64(n))
            e.post(tap: .cghidEventTap); usleep(40_000)
        }
        usleep(60_000)
    }
case "menubar", "menuitem":  // vidax <pid> menubar|menuitem <title> : "cx cy" of a menu bar item / an open menu's item
    let app = AXUIElementCreateApplication(pid)
    let want = a[3]
    let role = a[2] == "menubar" ? kAXMenuBarItemRole : kAXMenuItemRole
    func find(_ e: AXUIElement, _ d: Int) -> AXUIElement? {
        if d > 8 { return nil }
        if (attr(e, kAXRoleAttribute) as? String) == role, (attr(e, kAXTitleAttribute) as? String) == want,
           let f = frame(e), f.width > 0, f.height > 0 { return e }
        for k in kids(e) { if let r = find(k, d + 1) { return r } }
        return nil
    }
    guard let bar = attr(app, kAXMenuBarAttribute), let hit = find(bar as! AXUIElement, 0), let f = frame(hit) else { print("none"); exit(1) }
    print("\(Int(f.midX)) \(Int(f.midY))")
case "srcword":  // vidax <pid> srcword <after> <word> : "cx cy" of <word>'s first occurrence after <after> in the source text view
    let app = AXUIElementCreateApplication(pid)
    func area(_ e: AXUIElement, _ d: Int) -> AXUIElement? {
        if d > 40 { return nil }
        if (attr(e, kAXRoleAttribute) as? String) == kAXTextAreaRole { return e }
        for k in kids(e) { if let r = area(k, d + 1) { return r } }
        return nil
    }
    guard let w = (attr(app, kAXWindowsAttribute) as? [AXUIElement])?.first, let t = area(w, 0),
          let text = attr(t, kAXValueAttribute) as? String else { print("none"); exit(1) }
    let ns = text as NSString
    let anchor = ns.range(of: a[3])
    guard anchor.location != NSNotFound else { print("none"); exit(1) }
    let r = ns.range(of: a[4], range: NSRange(location: anchor.location, length: ns.length - anchor.location))
    guard r.location != NSNotFound else { print("none"); exit(1) }
    var cf = CFRange(location: r.location, length: r.length)
    var out: AnyObject?
    guard AXUIElementCopyParameterizedAttributeValue(t, kAXBoundsForRangeParameterizedAttribute as CFString, AXValueCreate(.cfRange, &cf)!, &out) == .success else { print("none"); exit(1) }
    var rect = CGRect.zero; AXValueGetValue(out as! AXValue, .cgRect, &rect)
    print("\(Int(rect.midX)) \(Int(rect.midY))")
case "srctext":  // vidax <pid> srctext : the source text view's contents
    let app = AXUIElementCreateApplication(pid)
    func area(_ e: AXUIElement, _ d: Int) -> AXUIElement? {
        if d > 40 { return nil }
        if (attr(e, kAXRoleAttribute) as? String) == kAXTextAreaRole { return e }
        for k in kids(e) { if let r = area(k, d + 1) { return r } }
        return nil
    }
    guard let w = (attr(app, kAXWindowsAttribute) as? [AXUIElement])?.first, let t = area(w, 0),
          let text = attr(t, kAXValueAttribute) as? String else { exit(1) }
    print(text, terminator: "")
case "type":  // vidax 0 type <text> [ms] : type characters to the focused app
    let ms = UInt32(a.count > 4 ? Int(a[4])! : 90) * 1000
    for ch in a[3].utf16 {
        var c = ch
        for down in [true, false] {
            let e = CGEvent(keyboardEventSource: nil, virtualKey: 0, keyDown: down)!
            e.keyboardSetUnicodeString(stringLength: 1, unicodeString: &c)
            e.post(tap: .cghidEventTap)
        }
        usleep(ms)
    }
case "key":  // vidax 0 key <keycode> [cmd] : one key press to the focused app
    for down in [true, false] {
        let e = CGEvent(keyboardEventSource: nil, virtualKey: CGKeyCode(a[3])!, keyDown: down)!
        if a.count > 4 { e.flags = .maskCommand }
        e.post(tap: .cghidEventTap)
    }
case "windows":  // vidax <pid> windows : "x y w h title" per window
    let app = AXUIElementCreateApplication(pid)
    for w in (attr(app, kAXWindowsAttribute) as? [AXUIElement]) ?? [] {
        let f = frame(w) ?? .zero
        print("\(Int(f.minX)) \(Int(f.minY)) \(Int(f.width)) \(Int(f.height)) \((attr(w, kAXTitleAttribute) as? String) ?? "")")
    }
case "press":  // vidax <pid> press <menu item title> : AXPress a menu item without opening its menu
    let app = AXUIElementCreateApplication(pid)
    func find(_ e: AXUIElement, _ d: Int) -> AXUIElement? {
        if d > 8 { return nil }
        if (attr(e, kAXRoleAttribute) as? String) == kAXMenuItemRole, (attr(e, kAXTitleAttribute) as? String) == a[3] { return e }
        for k in kids(e) { if let r = find(k, d + 1) { return r } }
        return nil
    }
    guard let bar = attr(app, kAXMenuBarAttribute), let item = find(bar as! AXUIElement, 0) else { print("none"); exit(1) }
    exit(AXUIElementPerformAction(item, kAXPressAction as CFString) == .success ? 0 : 1)
case "button":  // vidax <pid> button <title> : "cx cy" of a visible button with that title
    let app = AXUIElementCreateApplication(pid)
    func find(_ e: AXUIElement, _ d: Int) -> AXUIElement? {
        if d > 30 { return nil }
        if (attr(e, kAXRoleAttribute) as? String) == kAXButtonRole, (attr(e, kAXTitleAttribute) as? String) == a[3],
           let f = frame(e), f.width > 0 { return e }
        for k in kids(e) { if let r = find(k, d + 1) { return r } }
        return nil
    }
    for w in (attr(app, kAXWindowsAttribute) as? [AXUIElement]) ?? [] {
        if let b = find(w, 0), let f = frame(b) { print("\(Int(f.midX)) \(Int(f.midY))"); exit(0) }
    }
    print("none"); exit(1)
case "front":  // vidax <pid> front : make that process frontmost and raise its first window
    let app = AXUIElementCreateApplication(pid)
    AXUIElementSetAttributeValue(app, kAXFrontmostAttribute as CFString, kCFBooleanTrue)
    if let w = (attr(app, kAXWindowsAttribute) as? [AXUIElement])?.first { AXUIElementPerformAction(w, kAXRaiseAction as CFString) }
default: exit(64)
}
