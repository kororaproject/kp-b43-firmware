Name:          b43-firmware
Version:       6.30.163.46
Release:       1%{?dist}
Summary:       Broadcom Firmware installer
License:       GPL
BuildRequires: b43-fwcutter
Source0:       http://www.lwfinger.com/%{name}/broadcom-wl-%{version}.tar.bz2
BuildArch:     noarch

%description
Firmware for Broadcom 802.11 B/G/N family of wireless chips.

%prep
%setup -c broadcom-wl-%{version}
b43-fwcutter -w . broadcom-wl-%{version}.wl_apsta.o

%install
mkdir -p %{buildroot}/lib/firmware
cp -r b43 %{buildroot}/lib/firmware/

%files
/lib/firmware/b43/*

%changelog
* Fri Apr 8 2016 Michael Donnelly <mike@donnellyonine.com> 6.30.163.46-1
- Upgrade to version 6.30.163.46.

* Fri Jan 2 2015 Chris Smart <csmart@kororaproject.org> 5.100.138-1
- Initial spec.
