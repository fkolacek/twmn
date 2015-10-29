Name:   twmn-customized
Version:  1.0
Release:  1%{?dist}
Summary:  Customized twmn packed to RPM
Packager: Frantisek Kolacek <fkolacek@redhat.com>
Group:    User Interface/Desktops
License:  GNU LGPL 3
URL:    http://github.com/fkolacek/twmn
Source0:  twmn-customized-1.0.tgz

BuildRequires:  gcc make boost-devel qt5-qtbase-devel gcc-c++ qt5-qtx11extras-devel
Requires: libnotify

%description
Custom twmn configuration packed to RPM package.

%prep
%setup -q

%clean
rm -rf %{buildroot}

%build
qmake-qt5
make

%install
#make install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/etc/systemd/user

install twmnc %{buildroot}/usr/local/bin/twmnc
install twmnd %{buildroot}/usr/local/bin/twmnd
chmod 755 %{buildroot}/usr/local/bin/twmnc
chmod 755 %{buildroot}/usr/local/bin/twmnd

install scripts/twmnd.service %{buildroot}/etc/systemd/user/twmnd.service
chmod 644 %{buildroot}/etc/systemd/user/twmnd.service

%files
/usr/local/bin/twmnc
/usr/local/bin/twmnd
/etc/systemd/user/twmnd.service

%changelog
* Thu Sep 29 2015 Frantisek Kolacek <fkolacek@redhat.com> 1.0-1
--First repack
