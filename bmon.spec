
%define		_pre	pre6

Summary:	Console interface bandwidth usage monitor
Summary(pl):	Konsolowy monitor u�ycia interfejsu sieciowego
Name:		bmon
Version:	2.1.0
Release:	0.%{_pre}.1
License:	Artistic
Group:		Applications/Networking
Source0:	http://people.suug.ch/~tgr/bmon/files/%{name}-%{version}-%{_pre}.tar.gz
# Source0-md5:	909fe967ff361a7648586c7c1311aa2a
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

Pozwala on na generowanie i rysowanie trzech typ�w diagram�w:
- Diagram og�lny kt�ry wy�wietla wszystkie interfejsy sieciowe i
  informacje o aktualnym zu�yciu przepustowo�ci
- Diagram ASCII podobny do generowanego przez MRTG, pokazuj�cy
  informacje o przesyle danych w postaci wykresu paskowego
- Diagram szczeg�owy kt�ry zawiera wszystkie liczniki danego
  interfejsu, takie jak ca�kowita liczba bajt�w odebranych/wys�anych,
  b��dy, skompresowane pakiety...

%package devel
Summary:	Header files for bmon
Summary(pl):	Pliki nag��wkowe dla bmon
Group:		Development/Libraries

%description devel
Header files neccesary to develop bmon applications.

%description devel -l pl
Pliki nag��wkowe niezb�dne do tworzenia aplikacji korzystaj�cych z
bmon.


%prep
%setup -q -n %{name}-%{version}-%{_pre}

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
