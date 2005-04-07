Summary:	A partitioning tool for Apple Macintosh-style partitioned disks
Summary(pl):	Narzêdzie do partycjonowania dysków Apple Macintosh
Name:		pdisk
Version:	0.8
Release:	4
License:	Apple Free Copyright
Group:		Applications/System
Source0:	ftp://cfcl.com/pub/ev/%{name}.20000516.src.tar
# Source0-md5:	ca1279cc31edb92acaf00fd8b58b1dda
Patch0:		%{name}-docs.patch
Patch1:		%{name}-CC.patch
URL:		http://www.cfcl.com/~eryk/linux/pdisk/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
pdisk enables you to view and modify Apple Macintosh-style partition
maps. Normally, it is used to create MkLinux (or PPC Linux) partitions
on your disk, however, it can create partitions of any type, including
HFS (except it would be up to Mac OS or some other tool to actually
create the HFS filesystem in that HFS partition). pdisk won't put Mac
OS disk drivers onto your disk.

%description -l pl
pdisk jest odpowiednikiem fdiska, umo¿liwiaj±cym podgl±d i modyfikacjê
tablic partycji zapisanych w formacie Apple Macintosh. Jest u¿ywany do
tworzenia partycji linuksowych na dysku, a tak¿e do tworzenia partycji
innych typów, takich jak HFS. Nie nagrywa sterowników pod MacOS na
dysk.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} CC="%{__cc}" LDFLAGS="%{rpmldflags}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install pdisk $RPM_BUILD_ROOT%{_sbindir}/pdisk
install cvt_pt $RPM_BUILD_ROOT%{_sbindir}/cvt_pt
install pdisk.8 $RPM_BUILD_ROOT%{_mandir}/man8/pdisk.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README pdisk.html
%attr(755,root,root) %{_sbindir}/pdisk
%attr(755,root,root) %{_sbindir}/cvt_pt
%{_mandir}/man8/*
