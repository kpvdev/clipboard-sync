#!/usr/bin/env bash
#
# clipboard-sync: Bidirectional sync between PRIMARY and CLIPBOARD selections.
# Auto-detects Wayland vs X11 and uses the appropriate tools.
#
# On Wayland, reads via xclip (through XWayland, avoids flicker) and
# writes via wl-copy (native Wayland). Debounces to avoid interfering
# with active text highlighting.
#

POLL_INTERVAL=0.3
DEBOUNCE_CYCLES=3  # selection must be stable for this many cycles before syncing

export DISPLAY="${DISPLAY:-:0}"

get_primary()   { xclip -o -selection primary 2>/dev/null; }
get_clipboard() { xclip -o -selection clipboard 2>/dev/null; }

if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
    set_primary()   { wl-copy --primary -- "$1"; }
    set_clipboard() { wl-copy -- "$1"; }
else
    set_primary()   { printf '%s' "$1" | xclip -i -selection primary; }
    set_clipboard() { printf '%s' "$1" | xclip -i -selection clipboard; }
fi

last_synced_primary=""
last_synced_clipboard=""
prev_primary=""
prev_clipboard=""
stable_primary=0
stable_clipboard=0

while true; do
    primary=$(get_primary)
    clipboard=$(get_clipboard)

    # Track how long PRIMARY has been stable (unchanged between polls)
    if [ "$primary" != "$prev_primary" ]; then
        stable_primary=0
        prev_primary="$primary"
    else
        stable_primary=$((stable_primary + 1))
    fi

    # Track how long CLIPBOARD has been stable
    if [ "$clipboard" != "$prev_clipboard" ]; then
        stable_clipboard=0
        prev_clipboard="$clipboard"
    else
        stable_clipboard=$((stable_clipboard + 1))
    fi

    # PRIMARY changed and has settled — sync to CLIPBOARD
    if [ "$stable_primary" -eq "$DEBOUNCE_CYCLES" ] \
       && [ -n "$primary" ] \
       && [ "$primary" != "$last_synced_primary" ] \
       && [ "$primary" != "$clipboard" ]; then
        set_clipboard "$primary"
        last_synced_primary="$primary"
        last_synced_clipboard="$primary"
    fi

    # CLIPBOARD changed and has settled — sync to PRIMARY
    if [ "$stable_clipboard" -eq "$DEBOUNCE_CYCLES" ] \
       && [ -n "$clipboard" ] \
       && [ "$clipboard" != "$last_synced_clipboard" ] \
       && [ "$clipboard" != "$primary" ]; then
        set_primary "$clipboard"
        last_synced_clipboard="$clipboard"
        last_synced_primary="$clipboard"
    fi

    sleep "$POLL_INTERVAL"
done
