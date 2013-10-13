# revision 31577
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/hungarian/magyar.ldf
# catalog-date 2013-06-19 11:14:18 +0200
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-babel-hungarian
Version:	1.5
Release:	1
Summary:	Babel support for Hungarian (Magyar)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/hungarian/magyar.ldf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-hungarian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a language definition file that enables
support of Magyar (Hungarian) with babel.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/babel-hungarian/magyar.ldf

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
