Summary:	Console interface bandwidth usage monitor
Summary(pl):	Konsolowy monitor u¿ycia interfejsu sieciowego
Name:		bmon
Version:	1.2.1
Release:	1
License:	Artistic
Group:		Applications/Networking
Source0:	http://trash.net/~reeler/bmon/files/%{name}-%{version}.tar.bz2
# Source0-md5:	52c400477996b6f85046981226b2d278
URL:		http://trash.net/~reeler/bmon/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install bmon $RPM_BUILD_ROOT%{_bindir}
install bmon.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
