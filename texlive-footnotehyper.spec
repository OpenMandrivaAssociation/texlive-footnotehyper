%global tl_name footnotehyper
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1f
Release:	%{tl_revision}.1
Summary:	A hyperref aware footnote environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/footnotehyper
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footnotehyper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footnotehyper.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footnotehyper.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a footnote environment allowing verbatim material
and a savenotes environment which captures footnotes across problematic
environments. It is a successor to the footnote package by Mark Wooding
which had various compatibility issues with modern packages (hyperref,
color, xcolor, babel-french).

