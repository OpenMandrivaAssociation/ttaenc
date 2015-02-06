Name:		ttaenc
Version:	3.4.1
Release:	2
License:	GPLv2
Summary:	The True Audio (TTA) codec lossless audio compressor
Group:		Sound
URL:		http://sourceforge.net/projects/tta/
Source:		http://sourceforge.net/projects/tta/files/tta/ttaenc-src/%{name}-%{version}-src.tgz
Patch0:		ttaenc-3.4.1-src-shntool.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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
%setup -q -n %{name}-%{version}-src
%patch0 -p1

%build
%make

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__install -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc COPYING README
%{_bindir}/%{name}



%changelog
* Thu Sep 22 2011 Andrey Bondrov <abondrov@mandriva.org> 3.4.1-1mdv2011.0
+ Revision: 700842
- imported package ttaenc

