Name:		nsis-simple-service-plugin
Version:	1.30
Release:	2%{?dist}
Summary:	RPM wrapper for %{name}
License:	MPLv1.1 or LGPLv2+
Source:		http://nsis.sourceforge.net/mediawiki/images/c/c9/NSIS_Simple_Service_Plugin_1.30.zip
URL:		http://nsis.sourceforge.net/NSIS_Simple_Service_Plugin
BuildArch:	noarch
Packager:	Yedidyah Bar David <didi@redhat.com>

%description
A package wrapping %{name} to provide dependency features.

%prep
%setup -c -n %{name}

%install
DST=%{buildroot}%{_datadir}/nsis/Plugins
mkdir -p $DST
cp -v %{_builddir}/%{name}/SimpleSC.dll $DST
# NSIS 3 searches for Plugins by default in a specific subdir, depending
# on whether it's compiled for unicode or not.
# http://stackoverflow.com/questions/20583533/nsis-simple-service-plugin-invalid-command-simplescinstallservice
mkdir -p $DST/x86-ansi
ln -s ../SimpleSC.dll $DST/x86-ansi/SimpleSC.dll

%files
%{_datadir}/nsis/Plugins/SimpleSC.dll
%{_datadir}/nsis/Plugins/x86-ansi/SimpleSC.dll

%changelog
* Sun Jan 22 2017 Yedidyah Bar David <didi@redhat.com> 1.30-2
- Link also in Plugins/x86-ansi for compatibility with nsis-3

* Thu Jul 30 2015 Yedidyah Bar David <didi@redhat.com> 1.30-1
- Initial release
