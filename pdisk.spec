Summary:	A partitioning tool for Apple Macintosh-style partitioned disks
Name:		pdisk
Version:	0.8
Release:	3
Copyright:	Apple Free Copyright
Group:		Applications/System
Source0:	ftp://cfcl.com/pub/ev/%{name}.20000516.src.tar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Patch0:		%{name}-docs.patch

%description
pdisk enables you to view and modify Apple Macintosh-style partition
maps. Normally, it is used to create MkLinux (or PPC Linux) partitions
on your disk, however, it can create partitions of any type, including
HFS (except it would be up to Mac OS or some other tool to actually
create the HFS filesystem in that HFS partition). pdisk won't put Mac
OS disk drivers onto your disk.

%description -l pl
pdisk jest odpowiednikiem fdiska, umo¿liwiaja±cym podgl±d i modyfikacjê
tablic partycji zapisanych w formacie Apple Macintosh. Jest u¿ywany do
tworzenia partycji linuxowych na dysku, a tak¿e do tworzenia partycji
innych typów, takich jak HFS. Nie wgrywa sterowników pod MacOS na dysk.

%prep

%setup -q -n pdisk
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_mandir}/man8}

install pdisk $RPM_BUILD_ROOT/sbin/pdisk
install cvt_pt $RPM_BUILD_ROOT/sbin/cvt_pt
install pdisk.8 $RPM_BUILD_ROOT%{_mandir}/man8/pdisk.8

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/pdisk
%attr(755,root,root) /sbin/cvt_pt
%{_mandir}/man8/*
%doc README.gz pdisk.html
