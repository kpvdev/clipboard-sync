#!/bin/bash
export DISPLAY=:0
last=""
while true; do
    current=$(xclip -o -selection clipboard 2>/dev/null)
    if [ "$current" != "$last" ] && [ -n "$current" ]; then
        printf '%s' "$current" | xclip -i -selection primary
        last="$current"
    fi
    sleep 0.1
done
