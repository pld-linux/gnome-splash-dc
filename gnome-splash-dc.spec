Summary:	GNOME splash screen
Summary(pl):	Ekran startowy GNOME
Name:		gnome-splash-pld
Version:	1
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://www1.pld-dc.org/~averne/gnome-splash.png
# Source0-md5:	de56a169360ed8a6dcc5237e343d6f50
URL:		http://www.pld-dc.org/
Requires:	gnome-session >= 2.4.1-6
Provides:	gnome-splash
Obsoletes:	gnome-splash
BuildArch:      noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME splash screen

%description -l pl
Ekran startowy GNOME

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/splash
cp -f %{SOURCE0} $RPM_BUILD_ROOT%{_pixmapsdir}/splash/gnome-splash.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_pixmapsdir}/splash/gnome-splash.png
