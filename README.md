# Clipboard Sync

Bidirectional clipboard synchronization for Linux desktops running X11 or XWayland.

## What it does

- Syncs highlighted text (PRIMARY selection) to clipboard — paste with Ctrl+V or Shift+Insert
- Syncs copied text (CLIPBOARD) to PRIMARY selection — paste with Shift+Insert or middle-click after Ctrl+C
- Works seamlessly with GNOME Terminal, web browsers, and other desktop applications

## Compatibility

| Session Type | Supported |
|---|---|
| X11 | Yes |
| Wayland with XWayland (default on GNOME, KDE) | Yes |
| Pure Wayland (no XWayland) | No |

This tool uses `xclip` which operates through the X11 protocol. On Wayland sessions, it works via the XWayland compatibility layer that most desktop environments provide by default.

## Installation

### Fedora (via COPR)
```bash
sudo dnf copr enable kpvdev/clipboard-sync
sudo dnf install clipboard-sync
```

### Enable the service
```bash
systemctl --user enable --now clipboard-sync.service
```

## Requirements

- Linux desktop with X11 or XWayland
- xclip
- systemd

## How it works

A single systemd user service polls the PRIMARY and CLIPBOARD selections via `xclip` and keeps them in sync. Changes are debounced (~1 second) so that active text highlighting is not interrupted.

## License

MIT License
