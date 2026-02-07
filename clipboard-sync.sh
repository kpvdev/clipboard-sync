#!/bin/bash
export DISPLAY=:0
last=""
while true; do
    current=$(xclip -o -selection primary 2>/dev/null)
    if [ "$current" != "$last" ] && [ -n "$current" ]; then
        printf '%s' "$current" | xclip -i -selection clipboard
        last="$current"
    fi
    sleep 0.1
done
