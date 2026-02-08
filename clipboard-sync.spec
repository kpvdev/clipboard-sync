Name:           clipboard-sync
Version:        1.1.0
Release:        1%{?dist}
Summary:        Bidirectional clipboard synchronization for X11/XWayland

License:        MIT
URL:            https://github.com/kpvdev/clipboard-sync
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  systemd-rpm-macros

Requires:       systemd
Requires:       xclip

BuildArch:      noarch

%description
Synchronizes PRIMARY and CLIPBOARD selections bidirectionally, allowing
highlighted text and copied text to be pasted with either Ctrl+V or Shift+Insert.
Uses xclip and works on X11 and Wayland sessions with XWayland.

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
- Use xclip for all I/O (works on X11 and Wayland via XWayland)
- Debounce selection changes to avoid interfering with active highlighting
- Eliminate race condition between two independent polling loops
- Drop wl-clipboard dependency

* Fri Feb 07 2025 Kyle P. Vincent <kpvdev@users.noreply.github.com> - 1.0.0-1
- Initial package release
