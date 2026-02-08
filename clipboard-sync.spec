Name:           clipboard-sync
Version:        1.1.0
Release:        1%{?dist}
Summary:        Bidirectional clipboard synchronization for X11/Wayland

License:        MIT
URL:            https://github.com/kpvdev/clipboard-sync
Source0:        %{name}-%{version}.tar.gz

Requires:       systemd
Requires:       xclip
Requires:       (wl-clipboard if wayland-protocols)

BuildArch:      noarch

%description
Synchronizes PRIMARY and CLIPBOARD selections bidirectionally, allowing
highlighted text and copied text to be pasted with either Ctrl+V or Shift+Insert.
Automatically detects Wayland or X11 and uses the appropriate clipboard tools.

%prep
%setup -q

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_userunitdir}

install -m 0755 clipboard-sync.sh %{buildroot}%{_bindir}/clipboard-sync
install -m 0644 clipboard-sync.service %{buildroot}%{_userunitdir}/clipboard-sync.service

%files
%license LICENSE
%doc README.md
%{_bindir}/clipboard-sync
%{_userunitdir}/clipboard-sync.service

%post
echo "To enable clipboard sync, run:"
echo "  systemctl --user enable --now clipboard-sync.service"

%preun
if [ $1 -eq 0 ]; then
    systemctl --user stop clipboard-sync.service 2>/dev/null || true
    systemctl --user disable clipboard-sync.service 2>/dev/null || true
    systemctl --user stop clipboard-reverse-sync.service 2>/dev/null || true
    systemctl --user disable clipboard-reverse-sync.service 2>/dev/null || true
fi

%changelog
* Sat Feb 07 2026 Kyle P. Vincent <kpvdev@users.noreply.github.com> - 1.1.0-1
- Merge forward and reverse sync into single bidirectional script
- Auto-detect Wayland vs X11 session type
- Read via xclip (avoids Wayland compositor flicker), write via wl-copy on Wayland
- Debounce selection changes to avoid interfering with active highlighting
- Eliminate race condition between two independent polling loops

* Fri Feb 07 2025 Kyle P. Vincent <kpvdev@users.noreply.github.com> - 1.0.0-1
- Initial package release
