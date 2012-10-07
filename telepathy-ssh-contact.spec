Summary:	Tool to ease connecting with telepathy IM contacts via SSH
Summary(pl.UTF-8):	Narzędzie ułatwiające łączenie się z kontaktami IM telepathy przez SSH
Name:		telepathy-ssh-contact
Version:	0.7
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://telepathy.freedesktop.org/releases/ssh-contact/ssh-contact-%{version}.tar.gz
# Source0-md5:	2e98c1199c883980d4c8ef5fca4c5b70
URL:		http://telepathy.freedesktop.org/wiki/SSH-Contact
BuildRequires:	glib2-devel >= 1:2.28
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	telepathy-glib-devel >= 0.15.5
Requires:	glib2 >= 1:2.28
Requires:	telepathy-glib >= 0.15.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SSH-Contact is a client/service tool that makes it easy to connect to
your telepathy IM contacts via SSH. No need to care about dynamic IP,
NAT, port forwarding, or firewalls anymore; if you can chat with a
friend, you can also SSH to their machine.

%description -l pl.UTF-8
SSH-Contact to klient/narzędzie serwisowe ułatwiające łączenie się z
kontaktami IM telepathy poprzez SSH. Nie trzeba martwić się o
dynamiczne IP, NAT, przekazywanie portów czy firewalle; jeśli można
rozmawiać ze znajomym, można także połączyć się po SSH na jego
komputer.

%prep
%setup -q -n ssh-contact-%{version}

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/ssh-contact
%attr(755,root,root) %{_libexecdir}/ssh-contact-service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.SSHContact.service
%{_datadir}/telepathy/clients/SSHContact.client
