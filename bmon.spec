Summary:	Console interface bandwidth usage monitor
Summary(pl):	Konsolowy monitor u¿ycia interfejsu sieciowego
Name:		bmon
Version:	2.0.1
Release:	1
License:	Artistic
Group:		Applications/Networking
Source0:	http://people.suug.ch/~tgr/bmon/files/%{name}-%{version}.tar.gz
# Source0-md5:	d0da9d05f18c82a621171985d536dec7
URL:		http://people.suug.ch/~tgr/bmon/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
Conflicts:	nstats
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bmon is an interface bandwidth monitor.

It is able to generate and draw three types of diagrams:
- The overview diagram which is a list of all interfaces and their
  send/receive rates.
- A very MRTG like graphical diagram in ASCII showing the rate over a
  specific time period in a bar diagram.
- The details diagram which contains all counters of an interface such
  as total bytes sent/received, errors, compressed packets, ...

%description -l pl
bmon jest monitorem ruchu na interfejsach sieciowych.

Pozwala on na generowanie i rysowanie trzech typów diagramów:
- Diagram ogólny który wy¶wietla wszystkie interfejsy sieciowe i
  informacje o aktualnym zu¿yciu przepustowo¶ci
- Diagram ASCII podobny do generowanego przez MRTG, pokazuj±cy
  informacje o przesyle danych w postaci wykresu paskowego
- Diagram szczegó³owy który zawiera wszystkie liczniki danego
  interfejsu, takie jak ca³kowita liczba bajtów odebranych/wys³anych,
  b³êdy, skompresowane pakiety...

%package devel
Summary:	Header files for bmon
Summary(pl):	Pliki nag³ówkowe dla bmon
Group:		Development/Libraries

%description devel
Header files neccesary to develop bmon applications.

%description devel -l pl
Pliki nag³ówkowe niezbêdne do tworzenia aplikacji korzystaj±cych z
bmon.


%prep
%setup -q

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}
install etc/%{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
install include/%{name}/* $RPM_BUILD_ROOT%{_includedir}/%{name}/


%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
