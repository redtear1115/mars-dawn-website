#!/bin/bash
# One continuous take of the whole video. Full-screen recording; the shots are cut in post from
# timeline.txt. Throwaway copy only; every exit path ends what this script started, nothing else.
set -u
S=/private/tmp/claude-501/-Users-redtear-Projects-swift-mars-dawn/8534784c-2ee2-47fc-a0ec-9c913a59325e/scratchpad; R=/Users/redtear/Projects/swift/mars-dawn/.claude/worktrees/demo-video
X=$S/rig/vidax
FIX="$HOME/Obsidian/vault/MarsDawn Product Loop Video fixtures"
ID=dev.southern-light.marsdawn.video
CPREF="$HOME/Library/Containers/$ID/Data/Library/Preferences/$ID.plist"
TAKE=$S/rec/take-$(date +%H%M%S); mkdir -p "$TAKE/sig" "$TAKE/notes"
WORK=$(mktemp -d); COPY=$WORK/MarsDawn.app
PID=""; REC=""; QL=""; TERM_STARTED=0
T0=0
mark() { echo "$(python3 -c "import time;print(round(time.time()-$T0,2))") $*" >> "$TAKE/timeline.txt"; echo "mark $*"; }
fail() { echo "FAIL: $*" | tee -a "$TAKE/timeline.txt"; exit 1; }
cleanup() {
  touch "$TAKE/sig/end"
  [ -z "$QL" ] || kill $QL 2>/dev/null
  [ -z "$REC" ] || { kill -INT $REC 2>/dev/null; sleep 2; }
  [ -z "$PID" ] || kill $PID 2>/dev/null
  [ $TERM_STARTED = 1 ] && [ -n "${TPID:-}" ] && kill $TPID 2>/dev/null
  sleep 1
  defaults delete "$CPREF" >/dev/null 2>&1
  # An export that landed outside this take (e.g. ~/Documents) is ours to remove; the copy is kept.
  [ -n "${PDF:-}" ] && case "$PDF" in "$TAKE"/*) ;; *) rm -f "$PDF" ;; esac
  /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -u "$COPY" 2>/dev/null
  rm -rf "$WORK"
}
trap cleanup EXIT INT TERM
pgrep -x Terminal >/dev/null && fail "Terminal is already running; not touching it"
[ "$($X 0 display)" = awake ] || fail "display asleep"

# The copy, as in tools/screenshots/capture.sh.
ditto "$S/dd/Build/Products/Release/MarsDawn.app" "$COPY"; rm -rf "$COPY/Contents/PlugIns"
/usr/libexec/PlistBuddy -c "Set :CFBundleIdentifier $ID" "$COPY/Contents/Info.plist"
codesign --force --sign - --entitlements "$R/MarsDawn/MarsDawn.entitlements" "$COPY" >/dev/null 2>&1
[ "$(/usr/libexec/PlistBuddy -c 'Print :CFBundleIdentifier' "$COPY/Contents/Info.plist")" = "$ID" ] || fail "id not changed"
codesign -d --entitlements - --xml "$COPY" 2>/dev/null | plutil -p - | grep -q '"com.apple.security.app-sandbox" => true' || fail "not sandboxed"

# The copy's own settings (marsdawn open passes no launch arguments).
defaults delete "$CPREF" >/dev/null 2>&1
defaults write "$CPREF" AppleLanguages -array en
defaults write "$CPREF" appearance light
defaults write "$CPREF" lightTheme dawn
defaults write "$CPREF" darkTheme dawn
defaults write "$CPREF" defaultViewMode split
defaults write "$CPREF" zoom -float 2.5
defaults write "$CPREF" showSidebar -bool false
defaults write "$CPREF" sidebarTab outline
defaults write "$CPREF" ApplePersistenceIgnoreState -bool true
# Already asked for a review today: the App Store rating prompt must not appear on camera.
defaults write "$CPREF" ReviewPromptLastRequest -date "$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# Terminal: one window running the replay, English menus, dark, big type. No AppleScript (it
# needs an automation grant); a .command file, escape sequences, Cmd-= and AX instead.
cat > "$TAKE/replay.command" <<CMD
#!/bin/bash
exec /bin/bash '$S/rec/replay.sh' '$TAKE/notes' '$COPY' '$FIX' '$TAKE/sig'
CMD
chmod +x "$TAKE/replay.command"
open -a Terminal "$TAKE/replay.command" --args -AppleLanguages '(en)' -ApplePersistenceIgnoreState YES "-Default Window Settings" Basic "-Startup Window Settings" Basic; TERM_STARTED=1
for _ in $(seq 1 50); do TPID=$(pgrep -x Terminal); [ -n "$TPID" ] && break; sleep 0.1; done
[ -n "$TPID" ] || fail "Terminal did not start"
until [ -f "$TAKE/sig/ready" ]; do sleep 0.1; done
sleep 0.5; $X $TPID windows > "$TAKE/terminal-windows.txt"
[ "$(wc -l < "$TAKE/terminal-windows.txt")" -eq 1 ] || fail "Terminal has more than one window: $(cat "$TAKE/terminal-windows.txt")"
$X $TPID zoomin ${FONT_STEPS:-13}; sleep 0.8
$X $TPID place 0 30 1600 930 >/dev/null; sleep 0.8
$X $TPID windows >> "$TAKE/terminal-windows.txt"
touch "$TAKE/sig/layout"; until [ -f "$TAKE/sig/laid" ]; do sleep 0.1; done
open -a Terminal; sleep 1
[ "$(lsappinfo info -only name "$(lsappinfo front)" | sed -n 's/.*"LSDisplayName"="\(.*\)"/\1/p')" = Terminal ] || fail "Terminal is not frontmost: $(lsappinfo info -only name "$(lsappinfo front)")"
until [ -f "$TAKE/sig/ready" ]; do sleep 0.1; done
$X 0 move 1590 985; sleep 2

screencapture -v -C -V ${SECS:-110} "$TAKE/take.mov" >/dev/null 2>&1 & REC=$!
T0=$(python3 -c 'import time;print(time.time())'); sleep 1.5
mark rec-start

# Shots 1-2: the ask, the reply, marsdawn open.
mark shot1; touch "$TAKE/sig/go1"
until [ -f "$TAKE/sig/saved-v1" ]; do sleep 0.05; done; mark reply1
until [ -f "$TAKE/sig/open-cmd" ]; do sleep 0.05; done; mark open-entered
for _ in $(seq 1 60); do PID=$(lsappinfo info -only pid -app "$ID" | sed -n 's/.*"pid"=\([0-9]*\).*/\1/p'); [ -n "$PID" ] && break; sleep 0.1; done
[ -n "$PID" ] || fail "copy did not launch ($(cat $TAKE/sig/open.log))"
for _ in $(seq 1 60); do $X $PID windows | grep -q launch-note && break; sleep 0.1; done
$X $PID place 0 30 1600 900 >/dev/null; open -a "$COPY"; sleep 0.4
[ "$(lsappinfo info -only name "$(lsappinfo front)" | sed -n 's/.*"LSDisplayName"="\(.*\)"/\1/p')" = MarsDawn ] || fail "MarsDawn is not frontmost"
mark window-placed
sleep 4.5; mark shot3-end

# Shot 4: View > Show Sidebar, then "When it ships".
read vx vy < <($X $PID menubar View) ; $X 0 glide $vx $vy 700; sleep 0.2; $X 0 click $vx $vy; sleep 0.6
read sx sy < <($X $PID menuitem "Show Sidebar") || fail "no Show Sidebar"; $X 0 glide $sx $sy 500; sleep 0.2; $X 0 click $sx $sy; mark sidebar
sleep 1.2
read -r _ rx ry _ < <($X $PID rows | awk -F'\t' '$4=="When it ships"' | head -1)
[ -n "$rx" ] || fail "no outline row"
$X 0 glide $rx $ry 700; sleep 0.25; $X 0 click $rx $ry; mark jump-when
sleep 2.5; mark shot4-end

# Shot 5: Wednesday -> Friday under "When it ships", then save.
read wx wy < <($X $PID srcword "## When it ships" "Wednesday") || fail "no word"
$X 0 glide $wx $wy 700; sleep 0.3; $X 0 dclick $wx $wy; mark selected; sleep 0.8
$X 0 type Friday 110; mark typed; sleep 1.2
$X $PID press Save || fail "Save not pressed"; mark saved; sleep 1.5
cmp -s "$TAKE/notes/launch-note.md" "$FIX/launch-note.v2-user.md" && mark disk-is-v2 || { cp "$TAKE/notes/launch-note.md" "$TAKE/disk-after-edit.md"; fail "disk is not v2-user"; }
sleep 1; mark shot5-end

# Shots 6-7: back to the terminal; the agent makes it agree; MarsDawn reloads.
$X 0 glide 1590 985 400; sleep 0.2
open -a Terminal; mark terminal; sleep 0.5
touch "$TAKE/sig/go2"
until [ -f "$TAKE/sig/wrote-v3" ]; do sleep 0.05; done; mark reply2
sleep 2.5
open -a "$COPY"; mark back-to-app
sleep 2
[ "$($X $PID srctext)" = "$(cat "$FIX/launch-note.v3-agent.md")" ] && mark reloaded-v3 || mark "RELOAD-MISMATCH"
sleep 2.5; mark shot7-end

# Shot 8: read it again.
read -r _ rx ry _ < <($X $PID rows | awk -F'\t' '$4=="What changed"' | head -1)
$X 0 glide $rx $ry 600; sleep 0.25; $X 0 click $rx $ry; mark jump-what; sleep 2
read -r _ rx ry _ < <($X $PID rows | awk -F'\t' '$4=="Who does what"' | head -1)
$X 0 glide $rx $ry 600; sleep 0.25; $X 0 click $rx $ry; mark jump-who; sleep 2.2; mark shot8-end

# Shot 9: File > Export as PDF..., Save, Quick Look.
read fx fy < <($X $PID menubar File); $X 0 glide $fx $fy 700; sleep 0.2; $X 0 click $fx $fy; sleep 0.6
read ex ey < <($X $PID menuitem "Export as PDF…") || fail "no Export as PDF…"; $X 0 glide $ex $ey 500; sleep 0.2; $X 0 click $ex $ey; mark export-menu
sleep 2; $X $PID windows > "$TAKE/windows-at-panel.txt"; mark save-panel
read bx by < <($X $PID button Save) || fail "no Save button"; $X 0 glide $bx $by 600; sleep 0.25; $X 0 click $bx $by; mark save-pressed; sleep 2.5
PDF=$(find "$TAKE/notes" "$HOME/Library/Containers/$ID/Data" "$HOME/Downloads" "$HOME/Documents" "$HOME/Desktop" -maxdepth 3 -name 'launch-note.pdf' -newer "$TAKE/sig/go1" 2>/dev/null | head -1)
[ -n "$PDF" ] || fail "no PDF written"
echo "$PDF" > "$TAKE/pdf-path.txt"; cp "$PDF" "$TAKE/launch-note.pdf"
$X 0 glide 1590 985 500
open -a "$COPY" "$PDF"; sleep 1.5; $X $PID place 0 30 1600 900 >/dev/null; $X $PID windows > "$TAKE/pdf-windows.txt"; mark pdf-view
sleep 4; mark shot9-end
sleep 1; mark done
