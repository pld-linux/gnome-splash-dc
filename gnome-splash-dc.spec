Summary:	GNOME splash screen
Summary(pl.UTF-8):   Ekran startowy GNOME
Name:		gnome-splash-dc
Version:	1
Release:	2
License:	GPL
Group:		X11/Amusements
Source0:	http://www1.pld-dc.org/~averne/gnome-splash.png
# Source0-md5:	de56a169360ed8a6dcc5237e343d6f50
URL:		http://www.pld-dc.org/
Requires:	gnome-session >= 2.4.1-6
Provides:	gnome-splash
Obsoletes:	gnome-splash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME splash screen from DC.

%description -l pl.UTF-8
Ekran startowy GNOME z DC.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/splash

install %{SOURCE0} $RPM_BUILD_ROOT%{_pixmapsdir}/splash/gnome-splash.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_pixmapsdir}/splash/gnome-splash.png
