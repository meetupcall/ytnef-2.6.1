Summary: Yerase's TNEF Stream Reader
Name: ytnef
Version: 2.6
Release: 1
License: GPL
Group: Applications/Productivity
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: libytnef >= 1.4

%description
Yerase's TNEF Stream Reader.  Can take a TNEF Stream (winmail.dat) sent from
Microsoft Outlook (or similar products) and extract the attachments, including
construction of Contact Cards & Calendar entries.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING README 
/usr/bin/ytnef
/usr/bin/ytnefprint

%changelog
* Fri Mar 12 2004 Patrick <rpms@puzzled.xs4all.nl>
- Initial version

