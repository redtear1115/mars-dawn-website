// Renders the first page of a PDF to a PNG of the given width, on white.
// Usage: swift pdf2png.swift in.pdf out.png 1000
import AppKit
import PDFKit

let args = CommandLine.arguments
guard args.count == 4, let width = Double(args[3]),
      let doc = PDFDocument(url: URL(fileURLWithPath: args[1])), let page = doc.page(at: 0) else {
    FileHandle.standardError.write("usage: pdf2png.swift in.pdf out.png width\n".data(using: .utf8)!)
    exit(64)
}
let box = page.bounds(for: .mediaBox)
let scale = width / box.width
let size = NSSize(width: (box.width * scale).rounded(), height: (box.height * scale).rounded())
guard let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: Int(size.width), pixelsHigh: Int(size.height),
                                 bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
                                 colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0),
      let ctx = NSGraphicsContext(bitmapImageRep: rep) else { exit(70) }
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = ctx
let cg = ctx.cgContext
cg.setFillColor(NSColor.white.cgColor)
cg.fill(CGRect(origin: .zero, size: size))
cg.scaleBy(x: scale, y: scale)
page.draw(with: .mediaBox, to: cg)
NSGraphicsContext.restoreGraphicsState()
guard let png = rep.representation(using: .png, properties: [:]) else { exit(70) }
try png.write(to: URL(fileURLWithPath: args[2]))
