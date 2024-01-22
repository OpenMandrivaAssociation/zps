Name:           zps
Version:        2.0.0
Release:        1
Summary:        A small utility for listing and cleaning up zombie processes
License:        GPL-3.0-only
URL:            https://github.com/orhun/zps
Source0:        https://github.com/orhun/zps/archive/%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  cmake

%description
zps lists the running processes with theirs stats and indicates/reaps the 
zombie processes.
 
%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
