Name:          b43-firmware
Version:       5.100.138
Release:       1%{?dist}
Summary:       Broadcom Firmware installer
License:       GPL
BuildRequires: b43-fwcutter
Source0:       http://www.lwfinger.com/%{name}/broadcom-wl-%{version}.tar.bz2
BuildArch:     noarch

%description
Firmware for Broadcom 802.11 B/G/N family of wireless chips.

%prep
%autosetup -n broadcom-wl-%{version}
b43-fwcutter -w . linux/wl_apsta.o

%install
mkdir -p %{buildroot}/lib/firmware
cp -r b43 %{buildroot}/lib/firmware/

%files
/lib/firmware/b43/*

%changelog
* Fri Jan 2 2015 Chris Smart <csmart@kororaproject.org> 5.100.138-1
- Initial spec.

