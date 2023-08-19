Summary:	Console interface bandwidth usage monitor
Summary(pl.UTF-8):	Konsolowy monitor użycia interfejsu sieciowego
Name:		bmon
Version:	4.0
Release:	1
License:	Artistic
Group:		Applications/Networking
Source0:	https://github.com/tgraf/bmon/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	954afe2cedd8f972fc3903c10772a017
URL:		https://github.com/tgraf/bmon/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libconfuse-devel
BuildRequires:	libnl-devel >= 3.0
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
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

%description -l pl.UTF-8
bmon jest monitorem ruchu na interfejsach sieciowych.

Pozwala on na generowanie i rysowanie trzech typów diagramów:
- Diagram ogólny który wyświetla wszystkie interfejsy sieciowe i
  informacje o aktualnym zużyciu przepustowości
- Diagram ASCII podobny do generowanego przez MRTG, pokazujący
  informacje o przesyle danych w postaci wykresu paskowego
- Diagram szczegółowy który zawiera wszystkie liczniki danego
  interfejsu, takie jak całkowita liczba bajtów odebranych/wysłanych,
  błędy, skompresowane pakiety...

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%{__autoheader}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_docdir}/bmon/examples/bmon.conf

cp -p examples/bmon.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS examples/bmon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bmon.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
