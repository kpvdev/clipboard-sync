Name:           clipboard-sync
Version:        1.0.0
Release:        1%{?dist}
Summary:        Bidirectional clipboard synchronization for X11/Wayland

License:        MIT
URL:            https://github.com/kpvdev/clipboard-sync

Requires:       xclip
Requires:       systemd

BuildArch:      noarch

%description
Synchronizes PRIMARY and CLIPBOARD selections bidirectionally, allowing
highlighted text and copied text to be pasted with either Ctrl+V or Shift+Insert.

%prep
# Files are already present from git checkout, no extraction needed

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_userunitdir}

install -m 0755 %{_builddir}/clipboard-sync-%{version}-build/clipboard-sync.sh %{buildroot}%{_bindir}/clipboard-sync
install -m 0755 %{_builddir}/clipboard-sync-%{version}-build/clipboard-reverse-sync.sh %{buildroot}%{_bindir}/clipboard-reverse-sync

install -m 0644 %{_builddir}/clipboard-sync-%{version}-build/clipboard-sync.service %{buildroot}%{_userunitdir}/clipboard-sync.service
install -m 0644 %{_builddir}/clipboard-sync-%{version}-build/clipboard-reverse-sync.service %{buildroot}%{_userunitdir}/clipboard-reverse-sync.service

%files
%license %{_builddir}/clipboard-sync-%{version}-build/LICENSE
%doc %{_builddir}/clipboard-sync-%{version}-build/README.md
%{_bindir}/clipboard-sync
%{_bindir}/clipboard-reverse-sync
%{_userunitdir}/clipboard-sync.service
%{_userunitdir}/clipboard-reverse-sync.service

%post
echo "To enable clipboard sync, run:"
echo "  systemctl --user enable --now clipboard-sync.service"
echo "  systemctl --user enable --now clipboard-reverse-sync.service"

%preun
if [ $1 -eq 0 ]; then
    systemctl --user stop clipboard-sync.service 2>/dev/null || true
    systemctl --user stop clipboard-reverse-sync.service 2>/dev/null || true
    systemctl --user disable clipboard-sync.service 2>/dev/null || true
    systemctl --user disable clipboard-reverse-sync.service 2>/dev/null || true
fi

%changelog
* Fri Feb 07 2025 Kyle P. Vincent <kpvdev@users.noreply.github.com> - 1.0.0-1
- Initial package release
