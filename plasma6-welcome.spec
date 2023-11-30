%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20231130

Summary:	A friendly onboarding wizard for Plasma
Name:		plasma6-welcome
Version:	5.90.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://invent.kde.org/plasma/plasma-welcome
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-welcome/-/archive/master/plasma-welcome-master.tar.bz2#/plasma-welcome-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/plasma-welcome-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6UserFeedback)
BuildRequires:	pkgconfig(Qt6QuickControls2)

%description
A Friendly onboarding wizard for Plasma.
Welcome Center is the perfect introduction
to KDE Plasma! It can help you learn how to
connect to the internet, install apps,
customize the system, and more!

%prep
%autosetup -p1 -n plasma-welcome-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_TESTING:BOOL=OFF \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang plasma-welcome

%files -f plasma-welcome.lang
%{_bindir}/plasma-welcome
%{_qtdir}/plugins/kf6/kded/kded_plasma-welcome.so
%{_datadir}/applications/org.kde.plasma-welcome.desktop
%{_datadir}/metainfo/org.kde.plasma-welcome.appdata.xml
