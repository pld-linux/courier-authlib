Summary:	Courier authentication library
Summary(pl.UTF-8):	Biblioteka uwierzytelniania Couriera
Name:		courier-authlib
Version:	0.60.6
Release:	3
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/courier/%{name}-%{version}.tar.bz2
# Source0-md5:	1a59634a8c8c4168dc84c920a467c1a9
Source1:	%{name}.init
Patch0:		%{name}-md5sum-passwords.patch
Patch1:		%{name}-authdaemonrc.patch
Patch2:		%{name}-nostatic.patch
Patch3:		%{name}-ltdl.patch
URL:		http://www.courier-mta.org/authlib/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	expect
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel
BuildRequires:	rpmbuild(macros) >= 1.304
BuildRequires:	sysconftool
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	/sbin/chkconfig
Requires:	rc-scripts
Obsoletes:	sqwebmail-auth-cram
Obsoletes:	sqwebmail-auth-pam
Obsoletes:	sqwebmail-auth-pwd
Obsoletes:	sqwebmail-auth-shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		schemadir	/usr/share/openldap/schema

%description
The Courier authentication library provides authentication services
for other Courier applications.

%description -l pl.UTF-8
Biblioteka uwierzytelniania Couriera dostarcza usługi uwierzytelniania
dla innych aplikacji Couriera.

%package libs
Summary:	Courier authentication library
Summary(pl.UTF-8):	Biblioteka uwierzytelniania Couriera
Group:		Libraries
Requires(post,postun):	/sbin/ldconfig

%description libs
The Courier authentication library provides authentication services
for other Courier applications.

This package contains libcourierauth.so which client programs link
against.

%description libs -l pl.UTF-8
Biblioteka uwierzytelniania Couriera dostarcza usługi uwierzytelniania
dla innych aplikacji Couriera.

%package devel
Summary:	Development files for the Courier authentication library
Summary(pl.UTF-8):	Pliki programistyczne dla biblioteki uwierzytelniania Couriera
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-authldap = %{version}-%{release}
Requires:	%{name}-authmysql = %{version}-%{release}
Requires:	%{name}-authpgsql = %{version}-%{release}
Requires:	%{name}-authuserdb = %{version}-%{release}
Requires:	%{name}-authpipe = %{version}-%{release}

%description devel
This package contains the development files needed to compile Courier
packages that use this authentication library. Install this package in
order to build the rest of the Courier packages. After they are built
and installed this package can be removed. Files in this package are
not needed at runtime.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne potrzebne do kompilacji
pakietów Couriera używających biblioteki uwierzytelniania. Należy go
zainstalować aby zbudować resztę pakietów Couriera. Po ich zbudowaniu
i zainstalowaniu ten pakiet można usunąć. Pliki z tego pakietu nie są
potrzebne w czasie działania programów.

%package authldap
Summary:	LDAP support for the Courier authentication library
Summary(pl.UTF-8):	Obsługa LDAP dla biblioteki uwierzytelniania Couriera
Group:		Networking/Daemons
Requires(pre,postun):	sed >= 4.0
Requires:	%{name} = %{version}-%{release}
Obsoletes:	courier-authldap
Obsoletes:	courier-imap-authldap
Obsoletes:	sqwebmail-auth-ldap

%description authldap
This package installs LDAP support for the Courier authentication
library. Install this package in order to be able to authenticate
using LDAP.

%description authldap -l pl.UTF-8
Ten pakiet dodaje obsługę LDAP do biblioteki uwierzytelniania
Couriera. Należy go zainstalować aby móc uwierzytelniać się z użyciem
LDAP.

%package authmysql
Summary:	MySQL support for the Courier authentication library
Summary(pl.UTF-8):	Obsługa MySQL dla biblioteki uwierzytelniania Couriera
Group:		Networking/Daemons
Requires(pre,postun):	sed >= 4.0
Requires:	%{name} = %{version}-%{release}
Obsoletes:	courier-authmysql
Obsoletes:	courier-imap-authmysql
Obsoletes:	sqwebmail-auth-mysql

%description authmysql
This package installs MySQL support for the Courier authentication
library. Install this package in order to be able to authenticate
using MySQL.

%description authmysql -l pl.UTF-8
Ten pakiet dodaje obsługę MySQL do biblioteki uwierzytelniania
Couriera. Należy go zainstalować aby móc uwierzytelniać się z użyciem
MySQL.

%package authpgsql
Summary:	PostgreSQL support for the Courier authentication library
Summary(pl.UTF-8):	Obsługa PostgreSQL dla biblioteki uwierzytelniania Couriera
Group:		Networking/Daemons
Requires(pre,postun):	sed >= 4.0
Requires:	%{name} = %{version}-%{release}
Obsoletes:	courier-authpgsql
Obsoletes:	courier-imap-authpgsql
Obsoletes:	sqwebmail-auth-pgsql

%description authpgsql
This package installs PostgreSQL support for the Courier
authentication library. Install this package in order to be able to
authenticate using PostgreSQL.

%description authpgsql -l pl.UTF-8
Ten pakiet dodaje obsługę PostgreSQL do biblioteki uwierzytelniania
Couriera. Należy go zainstalować aby móc uwierzytelniać się z użyciem
PostgreSQL.

%package authuserdb
Summary:	Userdb support for the Courier authentication library
Summary(pl.UTF-8):	Obsługa userdb dla biblioteki uwierzytelniania Couriera
Group:		Networking/Daemons
Requires(pre,postun):	sed >= 4.0
Requires:	%{name} = %{version}-%{release}
Obsoletes:	courier-authlib-userdb
Obsoletes:	courier-imap-userdb
Obsoletes:	sqwebmail-auth-userdb

%description authuserdb
This package installs the userdb support for the Courier
authentication library. Userdb is a simple way to manage virtual mail
accounts using a GDBM-based database file.

Install this package in order to be able to authenticate with userdb.

%description authuserdb -l pl.UTF-8
Ten pakiet dodaje obsługę userdb do biblioteki uwierzytelniania
Couriera. Userdb to prosty sposób zarządzania wirtualnymi kontami
pocztowymi przy użyciu pliku bazy danych opartej na GDBM.

Należy go zainstalować aby móc uwierzytelniać się z użyciem userdb.

%package authpipe
Summary:	External authentication module that communicates via pipes
Summary(pl.UTF-8):	Zewnętrzny moduł uwierzytelniający komunikujący się przez potoki
Group:		Networking/Daemons
Requires(pre,postun):	sed >= 4.0
Requires:	%{name} = %{version}-%{release}
Obsoletes:	courier-authlib-authpipe

%description authpipe
This package installs the authpipe module, which is a generic plugin
that enables authentication requests to be serviced by an external
program, then communicates through messages on stdin and stdout.

%description authpipe -l pl.UTF-8
Pakiet ten instaluje moduł authpipe, który jest ogólną wtyczką
umożliwiającą obsługę żądań uwierzytelnienia przez zewnętrzny program
komunikujący się poprzez wiadomości wysyłane na stdin i stdout.

%package -n openldap-schema-courier
Summary:	Courier LDAP schema
Summary(pl.UTF-8):	Schemat LDAP Couriera
Group:		Networking/Daemons
Requires(post,postun):	sed >= 4.0
Requires:	openldap-servers
Requires:	sed >= 4.0

%description -n openldap-schema-courier
This package contains Courier authldap.schema for openldap.

%description -n openldap-schema-courier -l pl.UTF-8
Ten pakiet zawiera schemat Couriera authldap.schema dla openldapa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

rm -rf libltdl

%build
for d in . gdbmobj bdbobj md5 sha1 libhmac numlib makedat userdb rfc822 random128 liblock liblog; do
cd $d
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	%{__automake}
cd -
done

%configure \
	--enable-ltdl-install=no \
	--with-db=db \
	--with-mailuser=daemon \
	--with-mailgroup=daemon

%{__make} \
	LDFLAGS="%{rpmldflags} -lcrypt"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_sysconfdir}/authlib/userdb,%{schemadir},%{_bindir}}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/courier-authlib
install authldap.schema $RPM_BUILD_ROOT%{schemadir}/courier.schema
install makedat/makedat $RPM_BUILD_ROOT%{_bindir}/makedat

# make config files
./sysconftool $RPM_BUILD_ROOT%{_sysconfdir}/authlib/*.dist
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/authlib/*.dist

touch $RPM_BUILD_ROOT%{_localstatedir}/spool/authdaemon/socket

# remove static library - for now
rm $RPM_BUILD_ROOT%{_libdir}/courier-authlib/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig %{_libexecdir}/courier-authlib
/sbin/chkconfig --add courier-authlib

%service courier-authlib restart "authlib daemon"

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del courier-authlib
	%service courier-authlib stop
fi

%postun
/sbin/ldconfig %{_libexecdir}/courier-authlib

%post libs
/sbin/ldconfig %{_libexecdir}/courier-authlib

%postun libs
/sbin/ldconfig %{_libexecdir}/courier-authlib

%post authldap
if [ "$1" = 1 ]; then
	# add to authmodulelist list if package is first installed
	%{__sed} -i -e '/^authmodulelist=/{/\bauthldap\b/!s/"$/ authldap"/}' /etc/authlib/authdaemonrc
fi
/sbin/ldconfig %{_libexecdir}/courier-authlib
%service -q courier-authlib restart

%postun authldap
if [ "$1" = 0 ]; then
	# remove from authmodulelist if package is removed
	%{__sed} -i -e '/^authmodulelist=/{s/ \?\bauthldap\b \?//}' /etc/authlib/authdaemonrc
fi
/sbin/ldconfig %{_libexecdir}/courier-authlib
%service -q courier-authlib restart

%post authmysql
if [ "$1" = 1 ]; then
	# add to authmodulelist list if package is first installed
	%{__sed} -i -e '/^authmodulelist=/{/\bauthmysql\b/!s/"$/ authmysql"/}' /etc/authlib/authdaemonrc
fi
/sbin/ldconfig %{_libexecdir}/courier-authlib
%service -q courier-authlib restart

%postun authmysql
if [ "$1" = 0 ]; then
	# remove from authmodulelist if package is removed
	%{__sed} -i -e '/^authmodulelist=/{s/ \?\bauthmysql\b \?//}' /etc/authlib/authdaemonrc
fi
/sbin/ldconfig %{_libexecdir}/courier-authlib
%service -q courier-authlib restart

%post authpgsql
if [ "$1" = 1 ]; then
	# add to authmodulelist list if package is first installed
	%{__sed} -i -e '/^authmodulelist=/{/\bauthpgsql\b/!s/"$/ authpgsql"/}' /etc/authlib/authdaemonrc
fi
/sbin/ldconfig %{_libexecdir}/courier-authlib
%service -q courier-authlib restart

%postun authpgsql
if [ "$1" = 0 ]; then
	# remove from authmodulelist if package is removed
	%{__sed} -i -e '/^authmodulelist=/{s/ \?\bauthpgsql\b \?//}' /etc/authlib/authdaemonrc
fi
/sbin/ldconfig %{_libexecdir}/courier-authlib
%service -q courier-authlib restart

%post authuserdb
if [ "$1" = 1 ]; then
	# add to authmodulelist list if package is first installed
	%{__sed} -i -e '/^authmodulelist=/{/\buserdb\b/!s/"$/ userdb"/}' /etc/authlib/authdaemonrc
fi
/sbin/ldconfig %{_libexecdir}/courier-authlib
%service -q courier-authlib restart

%postun authuserdb
if [ "$1" = 0 ]; then
	# remove from authmodulelist if package is removed
	%{__sed} -i -e '/^authmodulelist=/{s/ \?\buserdb\b \?//}' /etc/authlib/authdaemonrc
fi
/sbin/ldconfig %{_libexecdir}/courier-authlib
%service -q courier-authlib restart

%post authpipe
if [ "$1" = 1 ]; then
	# add to authmodulelist list if package is first installed
	%{__sed} -i -e '/^authmodulelist=/{/\bpipe\b/!s/"$/ pipe"/}' /etc/authlib/authdaemonrc
fi
/sbin/ldconfig %{_libexecdir}/courier-authlib
%service -q courier-authlib restart

%postun authpipe
if [ "$1" = 0 ]; then
	# remove from authmodulelist if package is removed
	%{__sed} -i -e '/^authmodulelist=/{s/ \?\bpipe\b \?//}' /etc/authlib/authdaemonrc
fi
/sbin/ldconfig %{_libexecdir}/courier-authlib
%service -q courier-authlib restart

%post -n openldap-schema-courier
%openldap_schema_register %{schemadir}/courier.schema -d nis,cosine
%service -q ldap restart

%postun -n openldap-schema-courier
if [ "$1" = "0" ]; then
	%openldap_schema_unregister %{schemadir}/courier.schema
	%service -q ldap restart
fi

%triggerin -- courier < 0.48
if [ -f /etc/courier/authdaemonrc ]; then
	. /etc/courier/authdaemonrc

	%{__sed} -i s/^authmodulelist=.*/"authmodulelist=\"`echo $authmodulelist \
		| sed s/'authcram'/''/ | sed s/'  '/' '/`\""/ /etc/authlib/authdaemonrc
	%{__sed} -i s/^authmodulelistorig=.*/"authmodulelistorig=\"`echo $authmodulelistorig\
		| sed s/'authcram'/''/ | sed s/'  '/' '/`\""/ /etc/authlib/authdaemonrc
	%{__sed} -i s/^daemons=.*/"daemons=$daemons"/ /etc/authlib/authdaemonrc
fi
if [ -f /var/lock/subsys/courier ]; then
	if [ -f /var/spool/courier/authdaemon/pid ]; then
		kill `cat /var/spool/courier/authdaemon/pid`
		rm -f /var/spool/courier/authdaemon/*
		/sbin/service courier-authlib start
	fi
fi

%triggerin -- courier-imap-common < 4.0.0
if [ -f /etc/courier-imap/authdaemonrc ]; then
	. /etc/courier-imap/authdaemonrc

	%{__sed} -i s/^authmodulelist=.*/"authmodulelist=\"`echo $authmodulelist \
		| sed s/'authcram'/''/ | sed s/'  '/' '/`\""/ /etc/authlib/authdaemonrc
	%{__sed} -i s/^authmodulelistorig=.*/"authmodulelistorig=\"`echo $authmodulelistorig\
		| sed s/'authcram'/''/ | sed s/'  '/' '/`\""/ /etc/authlib/authdaemonrc
	%{__sed} -i s/^daemons=.*/"daemons=$daemons"/ /etc/authlib/authdaemonrc
fi
if [ -f /var/lock/subsys/courier-imap ]; then
	if [ -f /var/lib/authdaemon/pid ]; then
		kill `cat /var/lib/authdaemon/pid`
		rm -f /var/lib/authdaemon/*
		/sbin/service courier-authlib start
	fi
fi

%triggerin -- sqwebmail < 5.0.0
if [ -f /etc/sqwebmail/authdaemonrc ]; then
	. /etc/sqwebmail/authdaemonrc

	%{__sed} -i s/^authmodulelist=.*/"authmodulelist=\"`echo $authmodulelist \
		| sed s/'authcram'/''/ | sed s/'  '/' '/`\""/ /etc/authlib/authdaemonrc
	%{__sed} -i s/^authmodulelistorig=.*/"authmodulelistorig=\"`echo $authmodulelistorig\
		| sed s/'authcram'/''/ | sed s/'  '/' '/`\""/ /etc/authlib/authdaemonrc
	%{__sed} -i s/^daemons=.*/"daemons=$daemons"/ /etc/authlib/authdaemonrc
fi
if [ -f /var/lock/subsys/sqwebmail ]; then
	if [ -f /var/spool/sqwebmail/authdaemon/pid ]; then
		kill `cat /var/spool/sqwebmail/authdaemon/pid`
		rm -f /var/spool/sqwebmail/authdaemon/*
		/sbin/service courier-authlib start
	fi
fi

%triggerin -n %{name}-authldap -- courier-authldap < 0.48
if [ -f /etc/courier/authldaprc ]; then
	mv -f /etc/authlib/authldaprc /etc/authlib/authldaprc.new
	cp -f /etc/courier/authldaprc /etc/authlib/authldaprc
	%service -q courier-authlib restart
fi

%triggerin -n %{name}-authldap -- courier-imap-authldap < 4.0.0
if [ -f /etc/courier-imap/authldaprc ]; then
	mv -f /etc/authlib/authldaprc /etc/authlib/authldaprc.new
	cp -f /etc/courier-imap/authldaprc /etc/authlib/authldaprc
	%service -q courier-authlib restart
fi

%triggerin -n %{name}-authldap -- sqwebmail-auth-ldap < 5.0.0
if [ -f /etc/sqwebmail/authldaprc ]; then
	mv -f /etc/authlib/authldaprc /etc/authlib/authldaprc.new
	cp -f /etc/sqwebmail/authldaprc /etc/authlib/authldaprc
	%service -q courier-authlib restart
fi

%triggerin -n %{name}-authmysql -- courier-authmysql < 0.48
if [ -f /etc/courier/authmysqlrc ]; then
	mv -f /etc/authlib/authmysqlrc /etc/authlib/authmysqlrc.new
	cp -f /etc/courier/authmysqlrc /etc/authlib/authmysqlrc
	%service -q courier-authlib restart
fi

%triggerin -n %{name}-authmysql -- courier-imap-authmysql < 4.0.0
if [ -f /etc/courier-imap/authmysqlrc ]; then
	mv -f /etc/authlib/authmysqlrc /etc/authlib/authmysqlrc.new
	cp -f /etc/courier-imap/authmysqlrc /etc/authlib/authmysqlrc
	%service -q courier-authlib restart
fi

%triggerin -n %{name}-authmysql -- sqwebmail-auth-mysql < 5.0.0
if [ -f /etc/sqwebmail/authmysqlrc ]; then
	mv -f /etc/authlib/authmysqlrc /etc/authlib/authmysqlrc.new
	cp -f /etc/sqwebmail/authmysqlrc /etc/authlib/authmysqlrc
	%service -q courier-authlib restart
fi

%triggerin -n %{name}-authpgsql -- courier-authpgsql < 0.48
if [ -f /etc/courier/authpgsqlrc ]; then
	mv -f /etc/authlib/authpgsqlrc /etc/authlib/authpgsqlrc.new
	cp -f /etc/courier/authpgsqlrc /etc/authlib/authpgsqlrc
	%service -q courier-authlib restart
fi

%triggerin -n %{name}-authpgsql -- courier-imap-authpgsql < 4.0.0
if [ -f /etc/courier-imap/authpgsqlrc ]; then
	mv -f /etc/authlib/authpgsqlrc /etc/authlib/authpgsqlrc.new
	cp -f /etc/courier-imap/authpgsqlrc /etc/authlib/authpgsqlrc
	%service -q courier-authlib restart
fi

%triggerin -n %{name}-authpgsql -- sqwebmail-auth-pgsql < 5.0.0
if [ -f /etc/sqwebmail/authpgsqlrc ]; then
	mv -f /etc/authlib/authpgsqlrc /etc/authlib/authpgsqlrc.new
	cp -f /etc/sqwebmail/authpgsqlrc /etc/authlib/authpgsqlrc
	%service -q courier-authlib restart
fi

%triggerin -n %{name}-authuserdb -- courier < 0.48
if [ -d /etc/courier/userdb ]; then
	mv -f /etc/courier/userdb/* /etc/authlib/userdb
	makeuserdb
fi
if [ -f /etc/courier/userdb ]; then
	mv -f /etc/courier/userdb /etc/authlib/userdb
	makeuserdb
fi

%triggerin -n %{name}-authuserdb -- courier-imap-userdb < 4.0.0
if [ -d /etc/courier-imap/userdb ]; then
	mv -f /etc/courier-imap/userdb/* /etc/authlib/userdb
	makeuserdb
fi
if [ -f /etc/courier-imap/userdb ]; then
	mv -f /etc/courier-imap/userdb /etc/authlib/userdb
	makeuserdb
fi

%triggerin -n %{name}-authuserdb -- sqwebmail-auth-userdb < 5.0.0
if [ -d /etc/sqwebmail/userdb ]; then
	mv -f /etc/sqwebmail/userdb/* /etc/authlib/userdb
	makeuserdb
fi
if [ -f /etc/sqwebmail/userdb ]; then
	mv -f /etc/sqwebmail/userdb /etc/authlib/userdb
	makeuserdb
fi

%files
%defattr(644,root,root,755)
# COPYING contains only note
%doc AUTHORS COPYING ChangeLog NEWS README README*html README.authmysql.myownquery authldap.schema
%attr(755,root,root) %{_bindir}/makedat
%dir %{_sysconfdir}/authlib
%attr(754,root,root) /etc/rc.d/init.d/courier-authlib
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/authlib/authdaemonrc
%attr(755,root,root) %{_libexecdir}/courier-authlib/authdaemond
%attr(755,root,root) %{_libexecdir}/courier-authlib/authsystem.passwd
%attr(755,root,root) %{_libexecdir}/courier-authlib/makedatprog
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthcustom.so.*.*.*
%attr(755,root,root) %ghost %{_libexecdir}/courier-authlib/libauthcustom.so.0
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthpam.so.*.*.*
%attr(755,root,root) %ghost %{_libexecdir}/courier-authlib/libauthpam.so.0
%attr(755,root,root) %{_libexecdir}/courier-authlib/libcourierauthcommon.so.*.*.*
%attr(755,root,root) %ghost %{_libexecdir}/courier-authlib/libcourierauthcommon.so.0
%attr(755,root,root) %{_libexecdir}/courier-authlib/libcourierauthsasl.so.*.*.*
%attr(755,root,root) %ghost %{_libexecdir}/courier-authlib/libcourierauthsasl.so.0
%attr(755,root,root) %{_libexecdir}/courier-authlib/libcourierauthsaslclient.so.*.*.*
%attr(755,root,root) %ghost %{_libexecdir}/courier-authlib/libcourierauthsaslclient.so.0
%{_libexecdir}/courier-authlib/libauthcustom.la
%{_libexecdir}/courier-authlib/libauthpam.la
%{_libexecdir}/courier-authlib/libcourierauth.la
%{_libexecdir}/courier-authlib/libcourierauthcommon.la
%{_libexecdir}/courier-authlib/libcourierauthsasl.la
%{_libexecdir}/courier-authlib/libcourierauthsaslclient.la
%attr(770,root,daemon) %dir %{_localstatedir}/spool/authdaemon
%attr(777,root,root) %ghost %{_localstatedir}/spool/authdaemon/socket
%attr(755,root,root) %{_sbindir}/authdaemond
%attr(755,root,root) %{_sbindir}/authenumerate
%attr(755,root,root) %{_sbindir}/authpasswd
%attr(755,root,root) %{_sbindir}/authtest
%attr(755,root,root) %{_sbindir}/courierlogger
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%dir %{_libexecdir}/courier-authlib
%attr(755,root,root) %{_libexecdir}/courier-authlib/libcourierauth.so.*.*.*
%attr(755,root,root) %ghost %{_libexecdir}/courier-authlib/libcourierauth.so.0

%files devel
%defattr(644,root,root,755)
%doc authlib.html auth_*.html
%attr(755,root,root) %{_bindir}/courierauthconfig
%{_includedir}/*
%{_mandir}/man3/*
%attr(755,root,root) %{_libexecdir}/courier-authlib/*.so

%files authldap
%defattr(644,root,root,755)
%doc authldap.schema README.ldap
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/authlib/authldaprc
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthldap.so.*.*.*
%attr(755,root,root) %ghost %{_libexecdir}/courier-authlib/libauthldap.so.0
%{_libexecdir}/courier-authlib/libauthldap.la

%files authmysql
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/authlib/authmysqlrc
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthmysql.so.*.*.*
%attr(755,root,root) %ghost %{_libexecdir}/courier-authlib/libauthmysql.so.0
%{_libexecdir}/courier-authlib/libauthmysql.la

%files authpgsql
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/authlib/authpgsqlrc
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthpgsql.so.*.*.*
%attr(755,root,root) %ghost %{_libexecdir}/courier-authlib/libauthpgsql.so.0
%{_libexecdir}/courier-authlib/libauthpgsql.la

%files authuserdb
%defattr(644,root,root,755)
%attr(700,root,root) %dir %{_sysconfdir}/authlib/userdb
%attr(755,root,root) %{_sbindir}/makeuserdb
%attr(755,root,root) %{_sbindir}/pw2userdb
%attr(755,root,root) %{_sbindir}/userdb
%attr(755,root,root) %{_sbindir}/userdb-test-cram-md5
%attr(755,root,root) %{_sbindir}/userdbpw
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthuserdb.so.*.*.*
%attr(755,root,root) %ghost %{_libexecdir}/courier-authlib/libauthuserdb.so.0
%{_libexecdir}/courier-authlib/libauthuserdb.la
%{_mandir}/man8/*userdb*

%files authpipe
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthpipe.so.*.*.*
%attr(755,root,root) %ghost %{_libexecdir}/courier-authlib/libauthpipe.so.0
%{_libexecdir}/courier-authlib/libauthpipe.la

%files -n openldap-schema-courier
%defattr(644,root,root,755)
%{schemadir}/*.schema
