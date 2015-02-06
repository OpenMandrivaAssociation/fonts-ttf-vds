%define pkgname vds

Summary:	VDS font family
Name:		fonts-ttf-vds
Version:	20110926
Release:	2
License:	OFL
Group:		System/Fonts/True type
URL:		http://openfontlibrary.org/font/vds
Source0:	%{pkgname}.zip
Source1:	OFL.txt
Source2:	OFL-FAQ.txt
BuildArch:	noarch
BuildRequires:	freetype-tools
BuildRequires:	dos2unix

%description
Font family. Regular Bold Italic Bold Italic. More than 15 languages supported,
including Baltic & Cyrillic symbols.

%prep
%setup -q -c -n %{pkgname}-%{version}

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/vds

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/vds
ttmkfdir %{buildroot}%{_xfontdir}/TTF/vds -o %{buildroot}%{_xfontdir}/TTF/vds/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/vds/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/vds \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-vds:pri=50

%__install -D -m 644 %{SOURCE1} %{buildroot}%{_docdir}/%name/OFL.txt
%__install -D -m 644 %{SOURCE2} %{buildroot}%{_docdir}/%name/OFL-FAQ.txt

%files
%doc %{_docdir}/%name/OFL.txt
%doc %{_docdir}/%name/OFL-FAQ.txt
%dir %{_xfontdir}/TTF/vds
%{_xfontdir}/TTF/vds/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/vds/fonts.dir
%{_xfontdir}/TTF/vds/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-vds:pri=50


%changelog
* Wed Dec 14 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 20110926-1
+ Revision: 741054
- imported package fonts-ttf-vds

