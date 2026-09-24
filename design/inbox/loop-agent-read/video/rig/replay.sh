#!/bin/bash
# Runs inside the Terminal window: plays the user's lines and the agent's replies. The file writes
# (cp) and `marsdawn open` are real; the "agent" is this script. Every line comes from the
# fixtures folder or the storyboard, copied, never retyped.
DIR=$1; COPY=$2; FIX=$3; SIG=$4
cd "$DIR" || exit 1
P=$'\033[1;38;5;209m›\033[0m '
type_line() { local s="$1"; local i; for ((i=0;i<${#s};i++)); do printf '%s' "${s:i:1}"; sleep 0.03; done; }
wait_for() { until [ -f "$SIG/$1" ]; do sleep 0.05; done; }
printf '\033]11;#181a1c\007\033]10;#e6e6e4\007\033]12;#e6e6e4\007'
clear
touch "$SIG/ready"
wait_for layout
printf '\033[3J\033[H\033[2J'
touch "$SIG/laid"
wait_for go1
sleep 0.4
printf '%s' "$P"
sleep 0.8
type_line 'Write a launch note for the new sign-in page. Save it as launch-note.md.'
sleep 0.9; printf '\n\n'; sleep 1.4
cp "$FIX/launch-note.v1.md" launch-note.md
printf '%s\n\n' 'Saved launch-note.md: what changed, when it ships, who does what, and rollback.'
touch "$SIG/saved-v1"
sleep 1.8
printf '%s' "$P"; sleep 0.5
type_line 'marsdawn open launch-note.md'
sleep 0.6; printf '\n'
touch "$SIG/open-cmd"
MARSDAWN_APP_PATH="$COPY" marsdawn open launch-note.md >"$SIG/open.log" 2>&1; echo "rc=$?" >>"$SIG/open.log"
printf '\n%s' "$P"
wait_for go2
sleep 0.6
type_line "I edited \"When it ships\". Make the other sections agree. Don't add sections."
sleep 0.9; printf '\n\n'; sleep 1.6
cp "$FIX/launch-note.v3-agent.md" launch-note.md
printf '%s\n%s\n\n' "Done. \"What changed\" and \"Who does what\" now say Friday." "Design's Tuesday deadline and Rollback are unchanged."
touch "$SIG/wrote-v3"
printf '%s' "$P"
wait_for end
