Summary:	Courier authentication library
Summary(pl):	Biblioteka uwierzytelniania Couriera
Name:		courier-authlib
Version:	0.57
Release:	1.4
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/courier/%{name}-%{version}.tar.bz2
# Source0-md5:	af146ac84f0c3ee00006af50b4415d8a
Source1:	%{name}.init
Patch0:		%{name}-build.patch
Patch1:		%{name}-md5sum-passwords.patch
URL:		http://www.courier-mta.org/authlib/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	expect
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel
BuildRequires:	sed >= 4.0
BuildRequires:	sysconftool
BuildRequires:	zlib-devel
Requires(post,preun):	/sbin/chkconfig
Requires(post):	/sbin/ldconfig
Obsoletes:	sqwebmail-auth-cram
Obsoletes:	sqwebmail-auth-pam
Obsoletes:	sqwebmail-auth-pwd
Obsoletes:	sqwebmail-auth-shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		schemadir	/usr/share/openldap/schema

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
Requires:	%{name}-authldap = %{version}-%{release}
Requires:	%{name}-authmysql = %{version}-%{release}
Requires:	%{name}-authpgsql = %{version}-%{release}
Requires:	%{name}-userdb = %{version}-%{release}

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
Summary:	LDAP support for the Courier authentication library
Summary(pl):	Obs³uga LDAP dla biblioteki uwierzytelniania Couriera
Group:		Networking/Daemons
PreReq:		%{name} = %{version}-%{release}
Obsoletes:	courier-authldap
Obsoletes:	courier-imap-authldap
Obsoletes:	sqwebmail-auth-ldap

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
Obsoletes:	courier-authmysql
Obsoletes:	courier-imap-authmysql
Obsoletes:	sqwebmail-auth-mysql

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
Obsoletes:	courier-authpgsql
Obsoletes:	courier-imap-authpgsql
Obsoletes:	sqwebmail-auth-pgsql

%description authpgsql
This package installs PostgreSQL support for the Courier
authentication library. Install this package in order to be able to
authenticate using PostgreSQL.

%description authpgsql -l pl
Ten pakiet dodaje obs³ugê PostgreSQL do biblioteki uwierzytelniania
Couriera. Nale¿y go zainstalowaæ aby móc uwierzytelniaæ siê z u¿yciem
PostgreSQL.

%package userdb
Summary:	Userdb support for the Courier authentication library
Summary(pl):	Obs³uga userdb dla biblioteki uwierzytelniania Couriera
Group:		Networking/Daemons
PreReq:		%{name} = %{version}-%{release}
Obsoletes:	courier-imap-userdb
Obsoletes:	sqwebmail-auth-userdb

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

%package pipe
Summary:	External authentication module that communicates via pipes
Summary(pl):	Zewnêtrzny modu³ uwierzytelniaj±cy komunikuj±cy siê przez potoki
Group:		Networking/Daemons
PreReq:		%{name} = %{version}-%{release}

%description pipe
This package installs the authpipe module, which is a generic plugin
that enables authentication requests to be serviced by an external
program, then communicates through messages on stdin and stdout.

%description pipe -l pl
Pakiet ten instaluje modu³ authpipe, który jest ogóln± wtyczk±
umo¿liwiaj±c± obs³ugê ¿±dañ uwierzytelnienia przez zewnêtrzny program
komunikuj±cy siê poprzez wiadomo¶ci wysy³ane na stdin i stdout.

%package -n openldap-schema-courier
Summary:	Courier LDAP schema
Summary(pl):	Schemat LDAP Couriera
Group:		Networking/Daemons
Requires(post,postun):	sed >= 4.0
Requires:	sed >= 4.0
Requires:	openldap-servers

%description -n openldap-schema-courier
This package contains Courier authldap.schema for openldap.

%description -n openldap-schema-courier -l pl
Ten pakiet zawiera schemat Couriera authldap.schema dla openldapa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp /usr/share/automake/config.sub libltdl
%{__libtoolize}

# Change Makefile.am files and force recreate Makefile.in's.
OLDDIR=`pwd`
find -type f -a \( -name configure.in -o -name configure.ac \) | while read FILE; do
	cd "`dirname "$FILE"`"

	if [ -f Makefile.am ]; then
		sed -i -e '/_LDFLAGS=-static/d' Makefile.am
	fi

	%{__aclocal}
	%{__autoconf}
	%{__autoheader}
	%{__automake}

	cd "$OLDDIR"
done

%configure \
	--with-db=db \
	--with-mailuser=daemon \
	--with-mailgroup=daemon

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_sysconfdir}/authlib/userdb,%{schemadir}}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/courier-authlib
install authldap.schema $RPM_BUILD_ROOT%{schemadir}/courier.schema

# make config files
./sysconftool $RPM_BUILD_ROOT%{_sysconfdir}/authlib/*.dist
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/authlib/*.dist

# remove static library - for now
rm -f $RPM_BUILD_ROOT%{_libdir}/courier-authlib/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig %{_libexecdir}/courier-authlib

/sbin/chkconfig --add courier-authlib

if [ -f /var/lock/subsys/courier-authlib ]; then
	/etc/rc.d/init.d/courier-authlib restart
else
	echo "Run \"/etc/rc.d/init.d/courier-authlib start\" to start authlib daemon"
fi

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del courier-authlib
fi

if [ -f /var/lock/subsys/courier-authlib ]; then
	/etc/rc.d/init.d/courier-authlib stop
fi

%postun
/sbin/ldconfig %{_libexecdir}/courier-authlib

%post authldap
/sbin/ldconfig %{_libexecdir}/courier-authlib
if [ -f /var/lock/subsys/courier-authlib ]; then
	/etc/rc.d/init.d/courier-authlib restart
fi

%postun authldap
/sbin/ldconfig %{_libexecdir}/courier-authlib
if [ -f /var/lock/subsys/courier-authlib ]; then
	/etc/rc.d/init.d/courier-authlib restart
fi

%post authmysql
/sbin/ldconfig %{_libexecdir}/courier-authlib
if [ -f /var/lock/subsys/courier-authlib ]; then
	/etc/rc.d/init.d/courier-authlib restart
fi

%postun authmysql
/sbin/ldconfig %{_libexecdir}/courier-authlib
if [ -f /var/lock/subsys/courier-authlib ]; then
	/etc/rc.d/init.d/courier-authlib restart
fi

%post authpgsql
/sbin/ldconfig %{_libexecdir}/courier-authlib
if [ -f /var/lock/subsys/courier-authlib ]; then
	/etc/rc.d/init.d/courier-authlib restart
fi

%postun authpgsql
/sbin/ldconfig %{_libexecdir}/courier-authlib
if [ -f /var/lock/subsys/courier-authlib ]; then
	/etc/rc.d/init.d/courier-authlib restart
fi

%post userdb
/sbin/ldconfig %{_libexecdir}/courier-authlib
if [ -f /var/lock/subsys/courier-authlib ]; then
	/etc/rc.d/init.d/courier-authlib restart
fi

%postun userdb
/sbin/ldconfig %{_libexecdir}/courier-authlib
if [ -f /var/lock/subsys/courier-authlib ]; then
	/etc/rc.d/init.d/courier-authlib restart
fi

%post pipe
/sbin/ldconfig %{_libexecdir}/courier-authlib
if [ -f /var/lock/subsys/courier-authlib ]; then
	/etc/rc.d/init.d/courier-authlib restart
fi

%postun pipe
/sbin/ldconfig %{_libexecdir}/courier-authlib
if [ -f /var/lock/subsys/courier-authlib ]; then
	/etc/rc.d/init.d/courier-authlib restart
fi

%post -n openldap-schema-courier
if ! grep -q %{schemadir}/courier.schema /etc/openldap/slapd.conf; then
	sed -i -e '
		/^include.*local.schema/{
			i\
include		%{schemadir}/courier.schema
		}

		# enable dependant schemas: nis.schema
		/^#include.*\(nis\)\.schema/{
			s/^#//
		}
	' /etc/openldap/slapd.conf
fi

if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%postun -n openldap-schema-courier
if [ "$1" = "0" ]; then
	if grep -q %{schemadir}/courier.schema /etc/openldap/slapd.conf; then
		sed -i -e '
		/^include.*\/usr\/share\/openldap\/schema\/courier.schema/d

		# for symmetry it would be nice if we disable enabled schemas in post,
		# but we really can not do that, it would break something else.
		' /etc/openldap/slapd.conf
	fi

	if [ -f /var/lock/subsys/ldap ]; then
		/etc/rc.d/init.d/ldap restart >&2 || :
	fi
fi

%triggerin -- courier < 0.48
if [ -f /etc/courier/authdaemonrc ]; then
	. /etc/courier/authdaemonrc

	sed -i s/^authmodulelist=.*/"authmodulelist=\"`echo $authmodulelist \
		| sed s/'authcram'/''/ | sed s/'  '/' '/`\""/ /etc/authlib/authdaemonrc
	sed -i s/^authmodulelistorig=.*/"authmodulelistorig=\"`echo $authmodulelistorig\
		| sed s/'authcram'/''/ | sed s/'  '/' '/`\""/ /etc/authlib/authdaemonrc
	sed -i s/^daemons=.*/"daemons=$daemons"/ /etc/authlib/authdaemonrc
fi
if [ -f /var/lock/subsys/courier ]; then
	if [ -f /var/spool/courier/authdaemon/pid ]; then
		kill `cat /var/spool/courier/authdaemon/pid`
		rm -f /var/spool/courier/authdaemon/*
		/etc/rc.d/init.d/courier-authlib start
	fi
fi

%triggerin -- courier-imap-common < 4.0.0
if [ -f /etc/courier-imap/authdaemonrc ]; then
	. /etc/courier-imap/authdaemonrc

	sed -i s/^authmodulelist=.*/"authmodulelist=\"`echo $authmodulelist \
		| sed s/'authcram'/''/ | sed s/'  '/' '/`\""/ /etc/authlib/authdaemonrc
	sed -i s/^authmodulelistorig=.*/"authmodulelistorig=\"`echo $authmodulelistorig\
		| sed s/'authcram'/''/ | sed s/'  '/' '/`\""/ /etc/authlib/authdaemonrc
	sed -i s/^daemons=.*/"daemons=$daemons"/ /etc/authlib/authdaemonrc
fi
if [ -f /var/lock/subsys/courier-imap ]; then
	if [ -f /var/lib/authdaemon/pid ]; then
		kill `cat /var/lib/authdaemon/pid`
		rm -f /var/lib/authdaemon/*
		/etc/rc.d/init.d/courier-authlib start
	fi
fi

%triggerin -- sqwebmail < 5.0.0
if [ -f /etc/sqwebmail/authdaemonrc ]; then
	. /etc/sqwebmail/authdaemonrc

	sed -i s/^authmodulelist=.*/"authmodulelist=\"`echo $authmodulelist \
		| sed s/'authcram'/''/ | sed s/'  '/' '/`\""/ /etc/authlib/authdaemonrc
	sed -i s/^authmodulelistorig=.*/"authmodulelistorig=\"`echo $authmodulelistorig\
		| sed s/'authcram'/''/ | sed s/'  '/' '/`\""/ /etc/authlib/authdaemonrc
	sed -i s/^daemons=.*/"daemons=$daemons"/ /etc/authlib/authdaemonrc
fi
if [ -f /var/lock/subsys/sqwebmail ]; then
	if [ -f /var/spool/sqwebmail/authdaemon/pid ]; then
		kill `cat /var/spool/sqwebmail/authdaemon/pid`
		rm -f /var/spool/sqwebmail/authdaemon/*
		/etc/rc.d/init.d/courier-authlib start
	fi
fi

%triggerin -n %{name}-authldap -- courier-authldap < 0.48
if [ -f /etc/courier/authldaprc ]; then
	mv -f /etc/authlib/authldaprc /etc/authlib/authldaprc.new
	cp -f /etc/courier/authldaprc /etc/authlib/authldaprc
	if [ -f /var/lock/subsys/courier-authlib ]; then
		/etc/rc.d/init.d/courier-authlib restart
	fi
fi

%triggerin -n %{name}-authldap -- courier-imap-authldap < 4.0.0
if [ -f /etc/courier-imap/authldaprc ]; then
	mv -f /etc/authlib/authldaprc /etc/authlib/authldaprc.new
	cp -f /etc/courier-imap/authldaprc /etc/authlib/authldaprc
	if [ -f /var/lock/subsys/courier-authlib ]; then
		/etc/rc.d/init.d/courier-authlib restart
	fi
fi

%triggerin -n %{name}-authldap -- sqwebmail-auth-ldap < 5.0.0
if [ -f /etc/sqwebmail/authldaprc ]; then
	mv -f /etc/authlib/authldaprc /etc/authlib/authldaprc.new
	cp -f /etc/sqwebmail/authldaprc /etc/authlib/authldaprc
	if [ -f /var/lock/subsys/courier-authlib ]; then
		/etc/rc.d/init.d/courier-authlib restart
	fi
fi

%triggerin -n %{name}-authmysql -- courier-authmysql < 0.48
if [ -f /etc/courier/authmysqlrc ]; then
	mv -f /etc/authlib/authmysqlrc /etc/authlib/authmysqlrc.new
	cp -f /etc/courier/authmysqlrc /etc/authlib/authmysqlrc
	if [ -f /var/lock/subsys/courier-authlib ]; then
		/etc/rc.d/init.d/courier-authlib restart
	fi
fi

%triggerin -n %{name}-authmysql -- courier-imap-authmysql < 4.0.0
if [ -f /etc/courier-imap/authmysqlrc ]; then
	mv -f /etc/authlib/authmysqlrc /etc/authlib/authmysqlrc.new
	cp -f /etc/courier-imap/authmysqlrc /etc/authlib/authmysqlrc
	if [ -f /var/lock/subsys/courier-authlib ]; then
		/etc/rc.d/init.d/courier-authlib restart
	fi
fi

%triggerin -n %{name}-authmysql -- sqwebmail-auth-mysql < 5.0.0
if [ -f /etc/sqwebmail/authmysqlrc ]; then
	mv -f /etc/authlib/authmysqlrc /etc/authlib/authmysqlrc.new
	cp -f /etc/sqwebmail/authmysqlrc /etc/authlib/authmysqlrc
	if [ -f /var/lock/subsys/courier-authlib ]; then
		/etc/rc.d/init.d/courier-authlib restart
	fi
fi

%triggerin -n %{name}-authpgsql -- courier-authpgsql < 0.48
if [ -f /etc/courier/authpgsqlrc ]; then
	mv -f /etc/authlib/authpgsqlrc /etc/authlib/authpgsqlrc.new
	cp -f /etc/courier/authpgsqlrc /etc/authlib/authpgsqlrc
	if [ -f /var/lock/subsys/courier-authlib ]; then
		/etc/rc.d/init.d/courier-authlib restart
	fi
fi

%triggerin -n %{name}-authpgsql -- courier-imap-authpgsql < 4.0.0
if [ -f /etc/courier-imap/authpgsqlrc ]; then
	mv -f /etc/authlib/authpgsqlrc /etc/authlib/authpgsqlrc.new
	cp -f /etc/courier-imap/authpgsqlrc /etc/authlib/authpgsqlrc
	if [ -f /var/lock/subsys/courier-authlib ]; then
		/etc/rc.d/init.d/courier-authlib restart
	fi
fi

%triggerin -n %{name}-authpgsql -- sqwebmail-auth-pgsql < 5.0.0
if [ -f /etc/sqwebmail/authpgsqlrc ]; then
	mv -f /etc/authlib/authpgsqlrc /etc/authlib/authpgsqlrc.new
	cp -f /etc/sqwebmail/authpgsqlrc /etc/authlib/authpgsqlrc
	if [ -f /var/lock/subsys/courier-authlib ]; then
		/etc/rc.d/init.d/courier-authlib restart
	fi
fi

%triggerin -n %{name}-userdb -- courier < 0.48
if [ -d /etc/courier/userdb ]; then
	mv -f /etc/courier/userdb/* /etc/authlib/userdb
	makeuserdb
fi
if [ -f /etc/courier/userdb ]; then
	mv -f /etc/courier/userdb /etc/authlib/userdb
	makeuserdb
fi

%triggerin -n %{name}-userdb -- courier-imap-userdb < 4.0.0
if [ -d /etc/courier-imap/userdb ]; then
	mv -f /etc/courier-imap/userdb/* /etc/authlib/userdb
	makeuserdb
fi
if [ -f /etc/courier-imap/userdb ]; then
	mv -f /etc/courier-imap/userdb /etc/authlib/userdb
	makeuserdb
fi

%triggerin -n %{name}-userdb -- sqwebmail-auth-userdb < 5.0.0
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
%dir %{_sysconfdir}/authlib
%dir %{_libexecdir}/courier-authlib
%attr(754,root,root) /etc/rc.d/init.d/courier-authlib
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/authlib/authdaemonrc
%attr(755,root,root) %{_libexecdir}/courier-authlib/authdaemond
%attr(755,root,root) %{_libexecdir}/courier-authlib/authsystem.passwd
%attr(755,root,root) %{_libexecdir}/courier-authlib/makedatprog
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthcustom.so.*.*.*
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthpam.so.*.*.*
%attr(755,root,root) %{_libexecdir}/courier-authlib/libcourierauth.so.*.*.*
%attr(755,root,root) %{_libexecdir}/courier-authlib/libcourierauthcommon.so.*.*.*
%attr(755,root,root) %{_libexecdir}/courier-authlib/libcourierauthsasl.so.*.*.*
%attr(755,root,root) %{_libexecdir}/courier-authlib/libcourierauthsaslclient.so.*.*.*
%{_libexecdir}/courier-authlib/libauthcustom.la
%{_libexecdir}/courier-authlib/libauthpam.la
%{_libexecdir}/courier-authlib/libcourierauth.la
%{_libexecdir}/courier-authlib/libcourierauthcommon.la
%{_libexecdir}/courier-authlib/libcourierauthsasl.la
%{_libexecdir}/courier-authlib/libcourierauthsaslclient.la
%attr(770,root,daemon) %dir %{_localstatedir}/spool/authdaemon
%attr(755,root,root) %{_sbindir}/authdaemond
%attr(755,root,root) %{_sbindir}/authenumerate
%attr(755,root,root) %{_sbindir}/authpasswd
%attr(755,root,root) %{_sbindir}/authtest
%attr(755,root,root) %{_sbindir}/courierlogger
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc authlib.html auth_*.html
%attr(755,root,root) %{_bindir}/courierauthconfig
%{_includedir}/*
%{_mandir}/man3/*
%{_libexecdir}/courier-authlib/*.so

%files authldap
%defattr(644,root,root,755)
%doc authldap.schema README.ldap
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/authlib/authldaprc
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthldap.so.*.*.*
%{_libexecdir}/courier-authlib/libauthldap.la

%files authmysql
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/authlib/authmysqlrc
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthmysql.so.*.*.*
%{_libexecdir}/courier-authlib/libauthmysql.la

%files authpgsql
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/authlib/authpgsqlrc
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthpgsql.so.*.*.*
%{_libexecdir}/courier-authlib/libauthpgsql.la

%files userdb
%defattr(644,root,root,755)
%attr(700,root,root) %dir %{_sysconfdir}/authlib/userdb
%attr(755,root,root) %{_sbindir}/makeuserdb
%attr(755,root,root) %{_sbindir}/pw2userdb
%attr(755,root,root) %{_sbindir}/userdb
%attr(755,root,root) %{_sbindir}/userdb-test-cram-md5
%attr(755,root,root) %{_sbindir}/userdbpw
%attr(755,root,root) %{_sbindir}/vchkpw2userdb
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthuserdb.so.*.*.*
%{_libexecdir}/courier-authlib/libauthuserdb.la
%{_mandir}/man8/*userdb*

%files pipe
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/courier-authlib/libauthpipe.so.*.*.*
%{_libexecdir}/courier-authlib/libauthpipe.la

%files -n openldap-schema-courier
%defattr(644,root,root,755)
%{schemadir}/*.schema
