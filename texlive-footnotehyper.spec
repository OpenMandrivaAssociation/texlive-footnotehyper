Name:		texlive-footnotehyper
Version:	60374
Release:	1
Summary:	hyperref aware footnote.sty
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/footnotehyper
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnotehyper.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnotehyper.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnotehyper.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The footnote package by Mark Wooding dates back to 1997 and has
not been made hyperref compatible. The aim of the present
package is to do that.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/footnotehyper
%{_texmfdistdir}/tex/latex/footnotehyper
%doc %{_texmfdistdir}/doc/latex/footnotehyper

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
