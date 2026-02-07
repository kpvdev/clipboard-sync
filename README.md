# Clipboard Sync

Bidirectional clipboard synchronization for Linux (X11/GNOME/Wayland).

## What it does

- Syncs highlighted text (PRIMARY selection) to clipboard → paste with Ctrl+V or Shift+Insert
- Syncs copied text (CLIPBOARD) to PRIMARY selection → paste with Shift+Insert after clicking "Copy"
- Works seamlessly with GNOME Terminal and web browsers

## Installation

### Fedora (via COPR)
```bash
sudo dnf copr enable kpvdev/clipboard-sync
sudo dnf install clipboard-sync
```

### Enable the services
```bash
systemctl --user enable --now clipboard-sync.service
systemctl --user enable --now clipboard-reverse-sync.service
```

## Requirements

- Fedora Linux (or compatible)
- xclip
- systemd

## How it works

Two systemd user services poll the PRIMARY and CLIPBOARD selections and keep them in sync, allowing you to use either Ctrl+V or Shift+Insert regardless of how you copied the text.

## License

MIT License
