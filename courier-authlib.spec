#
# TODO:
#	- files
#	- post, preun
#	- triggers to allow upgrade from courier,courier-imap,sqwebmail
#
Summary:	Courier authentication library
Summary(pl):	Biblioteka uwierzytelniania Couriera
Name:		courier-authlib
%define		snap 20041116
Version:	0.50
Release:	0.%{snap}.0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.courier-mta.org/beta/courier-authlib/%{name}-%{version}.%{snap}.tar.bz2
# Source0-md5:	d6afed924f2195f55e17082336d679a7
URL:		http://www.courier-mta.org/
Requires(post,preun):	/sbin/chkconfig
BuildRequires:	expect
BuildRequires:	gdbm-devel
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Courier authentication library provides authentication services
for other Courier applications.

%description -l pl
Biblioteka uwierzytelniania Couriera dostarcza us³ugi uwierzytelniania
dla innych aplikacji Couriera.

%package devel
Summary:	Development files for the Courier authentication library
Summary(pl):	Pliki programistyczne dla biblioteki uwierzytelniania Couriera
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to compile Courier
packages that use this authentication library. Install this package in
order to build the rest of the Courier packages. After they are built
and installed this package can be removed. Files in this package are
not needed at runtime.

%description devel -l pl
Ten pakiet zawiera pliki programistyczne potrzebne do kompilacji
pakietów Couriera u¿ywaj±cych biblioteki uwierzytelniania. Nale¿y go
zainstalowaæ aby zbudowaæ resztê pakietów Couriera. Po ich zbudowaniu
i zainstalowaniu ten pakiet mo¿na usun±æ. Pliki z tego pakietu nie s±
potrzebne w czasie dzia³ania programów.

%package authldap
Summary:        LDAP support for the Courier authentication library
Summary(pl):    Obs³uga LDAP dla biblioteki uwierzytelniania Couriera
Group:          Networking/Daemons
PreReq:         %{name} = %{version}-%{release}

%description authldap
This package installs LDAP support for the Courier authentication
library. Install this package in order to be able to authenticate
using LDAP.

%description authldap -l pl
Ten pakiet dodaje obs³ugê LDAP do biblioteki uwierzytelniania
Couriera. Nale¿y go zainstalowaæ aby móc uwierzytelniaæ siê z u¿yciem
LDAP.

%package authmysql
Summary:	MySQL support for the Courier authentication library
Summary(pl):	Obs³uga MySQL dla biblioteki uwierzytelniania Couriera
Group:		Networking/Daemons
PreReq:		%{name} = %{version}-%{release}

%description authmysql
This package installs MySQL support for the Courier authentication
library. Install this package in order to be able to authenticate
using MySQL.

%description authmysql -l pl
Ten pakiet dodaje obs³ugê MySQL do biblioteki uwierzytelniania
Couriera. Nale¿y go zainstalowaæ aby móc uwierzytelniaæ siê z u¿yciem
MySQL.

%package authpgsql
Summary:	PostgreSQL support for the Courier authentication library
Summary(pl):	Obs³uga PostgreSQL dla biblioteki uwierzytelniania Couriera
Group:		Networking/Daemons
PreReq:		%{name} = %{version}-%{release}

%description authpgsql
This package installs PostgreSQL support for the Courier
authentication library. Install this package in order to be able to
authenticate using PostgreSQL.

%description authpgsql -l pl
Ten pakiet dodaje obs³ugê PostgreSQL do biblioteki uwierzytelniania
Couriera. Nale¿y go zainstalowaæ aby móc uwierzytelniaæ siê z u¿yciem
PostgreSQL.

%package userdb
Summary:        Userdb support for the Courier authentication library
Summary(pl):    Obs³uga userdb dla biblioteki uwierzytelniania Couriera
Group:          Networking/Daemons
PreReq:		%{name} = %{version}-%{release}

%description userdb
This package installs the userdb support for the Courier
authentication library. Userdb is a simple way to manage virtual mail
accounts using a GDBM-based database file.

Install this package in order to be able to authenticate with userdb.

%description userdb -l pl
Ten pakiet dodaje obs³ugê userdb do biblioteki uwierzytelniania
Couriera. Userdb to prosty sposób zarz±dzania wirtualnymi kontami
pocztowymi przy u¿yciu pliku bazy danych opartej na GDBM.

Nale¿y go zainstalowaæ aby móc uwierzytelniaæ siê z u¿yciem userdb.

%prep
%setup -q -n %{name}-%{version}.%{snap}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

install courier-authlib.sysvinit $RPM_BUILD_ROOT/etcdir}/rc.d/init.d/courier-authlib

# make config files
./sysconftool $RPM_BUILD_ROOT%{_sysconfdir}/authlib/*.dist
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/authlib/*.dist

# remove static library - for now
rm -f $RPM_BUILD_ROOT%{_libdir}/courier-authlib/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_libexecdir}/courier-authlib/authmigrate >/dev/null

/sbin/chkconfig --add courier-authlib

%preun
if [ -x %{_sbindir}/authdaemond ]; then
	%{_sbindir}/authdaemond >/dev/null 2>&1 || /bin/true
fi

if [ "$1" = "0" ]; then
	/sbin/chkconfig --del courier-authlib
fi

%files
%defattr(644,root,root,755)
# COPYING contains only note
%doc AUTHORS COPYING ChangeLog NEWS README README*html README.authmysql.myownquery authldap.schema
%dir %{_sysconfdir}/authlib
%dir %{_libexecdir}/courier-authlib
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/courier-authlib
%attr(755,root,root) %{_sysconfdir}/authlib/authdaemonrc
%attr(755,root,root) %{_libexecdir}/courier-authlib/authdaemond
%attr(755,root,root) %{_libexecdir}/courier-authlib/authsystem.passwd
%attr(755,root,root) %{_libexecdir}/courier-authlib/makedatprog
%attr(770,root,daemon) %dir %{_localstatedir}/spool/authdaemon
%attr(755,root,root) %{_sbindir}/authdaemond
%attr(755,root,root) %{_sbindir}/authenumerate
%attr(755,root,root) %{_sbindir}/authtest
%attr(755,root,root) %{_sbindir}/courierlogger
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc authlib.html auth_*.html
%attr(755,root,root) %{_bindir}/courierauthconfig
%{_includedir}/*
%{_mandir}/man3/*

%files authldap
%defattr(644,root,root,755)
%doc authldap.schema README.ldap
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/authlib/authldaprc
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthldap*

%files authmysql
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/authlib/authmysqlrc
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthmysql*

%files authpgsql
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/authlib/authpgsqlrc
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthpgsql*

%files userdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/makeuserdb
%attr(755,root,root) %{_sbindir}/userdb
%attr(755,root,root) %{_sbindir}/userdbpw
%attr(755,root,root) %{_sbindir}/vchkpw2userdb
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthuserdb*
%{_mandir}/man8/*userdb*
