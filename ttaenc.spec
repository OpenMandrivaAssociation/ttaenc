%global debug_package %{nil}

Name:		ttaenc
Version:	3.4.1
Release:	3
License:	GPL-2.0-or-later
Summary:	The True Audio codec lossless audio compressor
URL:		https://tausoft.org/en/
Group:		Sound/Utilities
Source0:	https://sourceforge.net/projects/tta/files/tta/ttaenc-src/%{name}-%{version}-src.tgz
Patch0:		ttaenc-3.4.1-src-shntool.patch

BuildRequires:	make
BuildRequires:	gcc-c++

%description
TTA performs lossless compression on multichannel 8,16 and 24 bits
data of the Wav audio files. Being "lossless" means that no data-
quality is lost in the compression - when uncompressed, the data will
be identical to the original. The compression ratios of TTA depend on
the type of music file being compressed, but the compression size
will generally range between 30% - 70% of the original. TTA format
supports both of ID3v1/v2 and APEv2 tags. Detailed format description
is available at http://tta.sourceforge.net

This version is patched with shntool patch.

%prep
%autosetup -n %{name}-%{version}-src -p1

%build
%if 0%{?arch64}
%make_build INSDIR=%{buildroot}%{_bindir} \
CFLAGS="-Wall -O3 -fomit-frame-pointer -funroll-loops -fforce-addr -falign-functions=4"
%else
%make_build INSDIR=%{buildroot}%{_bindir}
%endif

%install
mkdir -p %{buildroot}/usr/bin/
%make_install INSDIR=%{buildroot}%{_bindir}

%files
%{_bindir}/%{name}
%doc README
%doc ChangeLog-%{version}
%license COPYING

