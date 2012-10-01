Summary:	GTK+2 based notepad clone
Name:		leafpad
Version:	0.8.18.1
Release:	2
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://savannah.nongnu.org/download/leafpad/%{name}-%{version}.tar.gz
# Source0-md5:	254a72fc67505e3aa52884c729cd7b97
Patch0:		%{name}-config.patch
Patch1:		%{name}-desktop.patch
URL:		http://tarot.freeshell.org/leafpad/
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	pkgconfig
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Leafpad is a simple GTK+ based text editor. The user interface is
similar to "notepad", and it aims to be lighter than GEdit and KWrite
and to be as useful as them.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--enable-chooser
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/hicolor/*/*/*
%{_desktopdir}/*.desktop

