Name: man-pages-ja
Version: 20100115
Release: 2%{?dist}
# Actual license for each Japanese manpages is the same to the original English manpages' license.
License: Freely redistributable without restriction
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
URL: http://www.linux.or.jp/JM/

Source: http://www.linux.or.jp/JM/%{name}-%{version}.tar.gz
Source1: rh-man-pages-ja.pl
Source2: tail.1
Patch0: man-pages-ja-fix-configure.perl.patch
Patch9: man-pages-ja-20060815-204667-nfs.5.patch
Patch11: man-pages-ja-20060815-178955-at.1.patch
Patch12: man-pages-ja-missing-pkglist.patch
Patch15: man-pages-ja-358081-sysctl-warn.patch
Patch16: man-pages-ja-connect.2.patch
Patch18: man-pages-ja-433692-printf.1.patch
Patch19: man-pages-ja-446881-bash.1.patch
Patch20: man-pages-ja-455016-bash.1.patch
Patch21: man-pages-ja-456263-top.1.patch
Patch22: man-pages-ja-481750-bash.1.patch
Patch23: man-pages-ja-451238-sysctl.8.patch
Patch24: man-pages-ja-454048-bash.1.patch
Patch25: man-pages-ja-454419-echo.1.patch
Patch26: man-pages-ja-457361-wall.1.patch
Patch27: man-pages-ja-20090615-vmstat.8.patch
Patch28: man-pages-ja-493783-edquota.8.patch
Patch29: man-pages-ja-486655-mkfs.8.patch
Patch30: man-pages-ja-509048-less.1.patch
Patch31: man-pages-ja-515467-strings.1.patch
Patch32: man-pages-ja-527638-chgrp.1.patch
Patch33: man-pages-ja-537103-ip.7.patch
Patch34: man-pages-ja-fix-mdoc.patch
Patch35: man-pages-ja-565362-iptables.8.patch

Summary: Japanese man (manual) pages from the Japanese Manual Project
Group: Documentation
%description
Japanese Manual pages, translated by JM-Project (Japanese Manual Project).

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .0-configure.perl
%patch9 -p1 -b .9-nfs
%patch11 -p1 -b .11-at
%patch12 -p1 -b .12-pkglist
%patch15 -p1 -b .15-sysctl
%patch16 -p1 -b .16-connect
%patch18 -p1 -b .18-printf
%patch19 -p1 -b .19-bash-continue
%patch20 -p1 -b .20-bash-suspend
%patch21 -p1 -b .21-top
%patch22 -p1 -b .22-bash-source
%patch23 -p1 -b .23-sysctl
%patch24 -p1 -b .24-bash-hex
%patch25 -p1 -b .25-echo
%patch26 -p1 -b .26-wall
%patch27 -p1 -b .27-vmstat
%patch28 -p1 -b .28-edquota
%patch29 -p1 -b .29-mkfs
%patch30 -p1 -b .30-less
%patch31 -p1 -b .31-strings
%patch32 -p1 -b .32-chgrp
%patch33 -p1 -b .33-ip
%patch34 -p1 -b .34-mdoc
%patch35 -p1 -b .35-iptables

%build
perl %{SOURCE1} '$DESTDIR' | make

%install
rm -fr $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT sh ./installman.sh

rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/{chage.1,gpasswd.1,sg.1,apropos.1,man.1,whatis.1,newgrp.1}*
rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man5/{faillog.5,shadow.5,login.defs.5}*
rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man8/{adduser.8,chpasswd.8,faillog.8,groupadd.8,groupdel.8,groupmod.8,grpck.8,grpconv.8,grpunconv.8,lastlog.8,newusers.8,pwck.8,pwconv.8,pwunconv.8,rpm2cpio.8,useradd.8,userdel.8,usermod.8,vipw.8}*
rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man8/{rpmgraph,rpmcache,rpmbuild,rpm,vigr}.8*

# fix su(1) man page.
if [ -f $RPM_BUILD_DIR/%{name}-%{version}/manual/GNU_sh-utils/man1/su.1 ]; then
	rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/su.1*
	iconv -f euc-jp -t utf-8 $RPM_BUILD_DIR/%{name}-%{version}/manual/GNU_sh-utils/man1/su.1 > $RPM_BUILD_ROOT%{_mandir}/ja/man1/su.1
fi
# fix kill(1) man page.
if [ -f $RPM_BUILD_DIR/%{name}-%{version}/manual/util-linux/man1/kill.1 ]; then
	rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/kill.1*
	iconv -f euc-jp -t utf-8 $RPM_BUILD_DIR/%{name}-%{version}/manual/util-linux/man1/kill.1 > $RPM_BUILD_ROOT%{_mandir}/ja/man1/kill.1
fi
# fix chown(1) man page.
if [ -f $RPM_BUILD_DIR/%{name}-%{version}/manual/GNU_fileutils/man1/chown.1 ]; then
	rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/chown.1*
	iconv -f euc-jp -t utf-8 $RPM_BUILD_DIR/%{name}-%{version}/manual/GNU_fileutils/man1/chown.1 > $RPM_BUILD_ROOT%{_mandir}/ja/man1/chown.1
fi
# fix hostname(1) man page.
if [ -f $RPM_BUILD_DIR/%{name}-%{version}/manual/net-tools/man1/hostname.1 ]; then
	rm -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/hostname.1*
	iconv -f euc-jp -t utf-8 $RPM_BUILD_DIR/%{name}-%{version}/manual/net-tools/man1/hostname.1 > $RPM_BUILD_ROOT%{_mandir}/ja/man1/hostname.1
fi
# For Bug#128612
mv $RPM_BUILD_ROOT%{_mandir}/ja/man8/in.telned.8.gz $RPM_BUILD_ROOT%{_mandir}/ja/man8/in.telnetd.8.gz
# For Bug#128833
mv $RPM_BUILD_ROOT%{_mandir}/ja/man8/in.rlogin.8.gz $RPM_BUILD_ROOT%{_mandir}/ja/man8/in.rlogind.8.gz
# For Bug#551476
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man1/tail.1*
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/ja/man1/

# accumulate translation_lists
mkdir $RPM_BUILD_DIR/%{name}-%{version}/translation_lists
(cd $RPM_BUILD_DIR/%{name}-%{version}/manual
for i in `find -type f -name translation_list`; do
	package=`basename \`dirname $i\``;
	name=`basename $i`;
	if [ -s $i ]; then
		iconv -f euc-jp -t utf-8 $i > $RPM_BUILD_DIR/%{name}-%{version}/translation_lists/$package.$name;
	fi
done
)
 
%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc README translation_lists
%{_mandir}/ja/*


%changelog
* Wed Feb 17 2010 Akira TAGOH <tagoh@redhat.com> - 20100115-2
- Fix a typo in iptables(8). (#565362)

* Fri Jan 15 2010 Akira TAGOH <tagoh@redhat.com> - 20100115-1
- updates to 20100115.

* Fri Jan  8 2010 Akira TAGOH <tagoh@redhat.com> - 20091215-2
- Update tail.1 (#551476)

* Thu Dec 24 2009 Akira TAGOH <tagoh@redhat.com> - 20091215-1
- updates to 20091215.
- apply some patches to correct typos:
  - man-pages-ja-486655-mkfs.8.patch
  - man-pages-ja-509048-less.1.patch
  - man-pages-ja-515467-strings.1.patch
  - man-pages-ja-527638-chgrp.1.patch
  - man-pages-ja-537103-ip.7.patch
  - man-pages-ja-fix-mdoc.patch
- clean up the spec file.

* Tue Nov 10 2009 Akira TAGOH <tagoh@redhat.com> - 20091015-1
- updates to 20091015.
- use the corect man page for hostname(1).

* Mon Jul 27 2009 Akira TAGOH <tagoh@redhat.com> - 20090715-1
- updates to 20090715.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090615-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Akira TAGOH <tagoh@redhat.com> - 20090615-1
- updates to 20090615.
- Remove patches merged upstream:
  - man-pages-ja-20031215-crontab-0days.patch
  - man-pages-ja-432668-iptables.8.patch
  - man-pages-ja-20050215-ls.patch
- Correct various typos:
  - sysctl(8), bash(1), echo(1), wall(1), vmstat(8), edquota(8).

* Wed Feb 25 2009 Akira TAGOH <tagoh@redhat.com> - 20090215-2
- Remove vigr.8 to avoid file-conflict to shadow-utils.

* Wed Feb 25 2009 Akira TAGOH <tagoh@redhat.com> - 20090215-1
- updates to 20090215.
- Correct the description of 'source' built-in command in bash(1). (#481750)

* Thu Oct 16 2008 Akira TAGOH <tagoh@redhat.com> - 20081015-1
- updates to 20081015.

* Tue Oct  7 2008 Akira TAGOH <tagoh@redhat.com> - 20080915-1
- updates to 20080915.

* Sat Aug 23 2008 Akira TAGOH <tagoh@redhat.com> - 20080815-1
- updates to 20080815.
- correct the description of 'suspend' built-in command in bash(1).
- correct the description of top(1) command.

* Fri May 23 2008 Akira TAGOH <tagoh@redhat.com> - 20080515-2
- correct the description of 'continue' built-in command in bash(1).

* Thu May 22 2008 Akira TAGOH <tagoh@redhat.com> - 20080515-1
- updates to 20080515.

* Wed Apr 30 2008 Akira TAGOH <tagoh@redhat.com> - 20080415-2
- correct the description of --dscp option in iptables(8).
- correct the description of the syntax for octadecimal and hexadecimal
  in printf(1).

* Mon Apr 28 2008 Akira TAGOH <tagoh@redhat.com> - 20080415-1
- updates to 20080415.
- correct the description of the error section in connect(2).

* Tue Apr  1 2008 Akira TAGOH <tagoh@redhat.com> - 20080315-1
- updates to 20080315.

* Thu Feb 21 2008 Akira TAGOH <tagoh@redhat.com> - 20080215-1
- updates to 20080215.
- Apply man-pages-ja-358081-sysctl-warn.patch from RHEL.

* Mon Dec 17 2007 Akira TAGOH <tagoh@redhat.com> - 20071215-1
- updates to 20071215.
- remove vipw.8 to solve the file conflict to shadow-utils.

* Mon Nov 26 2007 Akira TAGOH <tagoh@redhat.com> - 20071119-1
- updates to 20071119.

* Mon Oct 29 2007 Akira TAGOH <tagoh@redhat.com> - 20071015-1
- updates to 20071015.

* Thu Sep 27 2007 Akira TAGOH <tagoh@redhat.com> - 20070915-1
- updates to 20070915.
  - remove man-pages-ja-222495-swapon.2.patch so that it's no longer needed.
- clean up the spec file.
- fix some warnings in perl script.

* Fri Aug 17 2007 Akira TAGOH <tagoh@redhat.com> - 20070815-1
- updates to 20070815.

* Thu Aug  9 2007 Akira TAGOH <tagoh@redhat.com>
- Update License tag.

* Mon Jul 23 2007 Akira TAGOH <tagoh@redhat.com> - 20070715-1
- updates to 20070715.
- man-pages-ja-222495-swapon.2.patch: applied to correct swapon(2).

* Thu Jul  5 2007 Akira TAGOH <tagoh@redhat.com> - 20070615-1
- updates to 20070615.
  - man-pages-ja-20051115-libaio.patch: removed.
  - man-pages-ja-20060815-204664-write.2.patch: removed.

* Thu Apr 26 2007 Akira TAGOH <tagoh@redhat.com> - 20070415-1
- updates to 20070415.

* Fri Mar 16 2007 Akira TAGOH <tagoh@redhat.com> - 20070315-1
- updates to 20070315.
- convert a spec file to UTF-8.
- remove empty translation_list.

* Thu Feb 15 2007 Akira TAGOH <tagoh@redhat.com> - 20070215-1
- updates to 20070215.

* Mon Feb  5 2007 Akira TAGOH <tagoh@redhat.com> - 20070115-1
- updates to 20070115.

* Mon Dec 18 2006 Akira TAGOH <tagoh@redhat.com> - 20061215-1
- updates o 20061215.

* Tue Sep  5 2006 Akira TAGOH <tagoh@redhat.com> - 20060815-2
- man-pages-ja-20060815-204667-nfs.5.patch: fixed nfs.5
- man-pages-ja-20060815-204664-write.2.patch: fixed write.2
- man-pages-ja-20060815-178955-at.1.patch: fixed at.1

* Thu Aug 17 2006 Akira TAGOH <tagoh@redhat.com> - 20060815-1
- updates to 20060815.

* Thu Jul 20 2006 Akira TAGOH <tagoh@redhat.com> - 20060715-1
- updates to 20060715.

* Fri Jun 23 2006 Akira TAGOH <tagoh@redhat.com> - 20060615-1
- updates to 20060615.

* Mon May 29 2006 Akira TAGOH <tagoh@redhat.com> - 20060515-1
- updates to 20060515.

* Mon Apr 17 2006 Akira TAGOH <tagoh@redhat.com> - 20060415-1
- updates to 20060415.

* Mon Mar 20 2006 Akira TAGOH <tagoh@redhat.com> - 20060315-1
- updates to 20060315.

* Thu Mar  9 2006 Akira TAGOH <tagoh@redhat.com> - 20060215-1
- updates to 20060215.

* Mon Jan 16 2006 Akira TAGOH <tagoh@redhat.com> - 20060115-1
- updates to 20060115.

* Wed Dec 21 2005 Akira TAGOH <tagoh@redhat.com> - 20051215-1
- updates to 20051215.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 21 2005 Akira TAGOH <tagoh@redhat.com> - 20051115-1
- updates to 20051115.
- man-pages-ja-20051115-libaio.patch: fixed a misleading of the header file
  required and a typo.
- man-pages-ja-20050215-ls.patch: fixed the -H option's explanation.

* Thu Oct 20 2005 Akira TAGOH <tagoh@redhat.com> - 20051015-1
- updates to 20051015.
- man-pages-ja-20050215-shmget.patch: no longer needed. merged into upstream.

* Fri Sep 30 2005 Florian La Roche <laroche@redhat.com>
- remove man-page now part of shadow-utils

* Tue Sep 27 2005 Akira TAGOH <tagoh@redhat.com> - 20050915-1
- updates to 20050915.

* Wed Aug 17 2005 Akira TAGOH <tagoh@redhat.com> - 20050815-1
- updates to 20050815.

* Wed Jul 20 2005 Akira TAGOH <tagoh@redhat.com> - 20050715-1
- updates to 20050715.

* Mon Jun 20 2005 Akira TAGOH <tagoh@redhat.com> - 20050615-1
- updates to 20050615.

* Mon May 16 2005 Akira TAGOH <tagoh@redhat.com> - 20050515-1
- updates to 20050515.

* Wed Apr 20 2005 Akira TAGOH <tagoh@redhat.com> - 20050415-1
- updates to 20050415.

* Tue Apr  5 2005 Akira TAGOH <tagoh@redhat.com> - 20050315-2
- removed newgrp.1 to avoid a file conflict.

* Tue Mar 15 2005 Akira TAGOH <tagoh@redhat.com> - 20050315-1
- updates to 20050315.

* Wed Feb 23 2005 Akira TAGOH <tagoh@redhat.com> - 20050215-1
- updates to 20050215.
- fixed wrong argument type and structure member variable type
  in shmget(2) (#149217)

* Tue Jan 18 2005 Akira TAGOH <tagoh@redhat.com> - 20050115-1
- updates to 20050115.

* Wed Jan  5 2005 Akira TAGOH <tagoh@redhat.com> - 20041215-2
- prefer GNU fileutils's chown(1) rather than gnumaniak's. (#142077)

* Wed Dec 15 2004 Akira TAGOH <tagoh@redhat.com> - 20041215-1
- updates to 20041215.

* Fri Nov 19 2004 Akira TAGOH <tagoh@redhat.com> - 20041115-1
- updates to 20041115.

* Mon Oct 25 2004 Akira TAGOH <tagoh@redhat.com> - 20041015-1
- updates to 20041015.

* Wed Sep 15 2004 Akira TAGOH <tagoh@redhat.com> - 20040915-1
- updates to 20040915.

* Mon Aug 16 2004 Akira TAGOH <tagoh@redhat.com> 20040815-1
- updates to 20040815.

* Mon Aug 02 2004 Akira TAGOH <tagoh@redhat.com> 20040715-5
- fixed wrong filename for in.rlogind.8 man pages. (#128833)

* Fri Jul 30 2004 Akira TAGOH <tagoh@redhat.com> 20040715-4
- rebuilt

* Thu Jul 29 2004 Akira TAGOH <tagoh@redhat.com> 20040715-3
- applied a patch to fix crontab.5's typo. (#128623)

* Tue Jul 27 2004 Akira TAGOH <tagoh@redhat.com> 20040715-2
- fixed wrong filename for in.telnetd.8 man pages. (#128612)

* Fri Jul 23 2004 Akira TAGOH <tagoh@redhat.com> 20040715-1
- updates to 20040715.

* Tue Jun 29 2004 Akira TAGOH <tagoh@redhat.com> 20040615-1
- updates to 20040615.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 19 2004 Akira TAGOH <tagoh@redhat.com> 20040515-1
- updates to 20040515.
- fixed wrong manpage for kill(1). we prefers util-linux thing rather than procps.

* Fri Apr 16 2004 Akira TAGOH <tagoh@redhat.com> 20040415-1
- updates to 20040415.

* Tue Mar 16 2004 Akira TAGOH <tagoh@redhat.com> 20040315-1
- updates to 20040315.

* Mon Feb 16 2004 Akira TAGOH <tagoh@redhat.com> 20040215-1
- updates to 20040215.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 10 2004 Akira TAGOH <tagoh@redhat.com> 20040115-2
- removed apropos.1, man.1, and whatis.1. the latest man contains those manpages now.

* Mon Jan 19 2004 Akira TAGOH <tagoh@redhat.com> 20040115-1
- updates to 20040115.

* Thu Dec 18 2003 Akira TAGOH <tagoh@redhat.com> 20031215-1
- updates to 20031215.

* Tue Oct 21 2003 Akira TAGOH <tagoh@redhat.com> 20031015-1
- updates to 20031015.

* Mon Sep 01 2003 Akira TAGOH <tagoh@redhat.com> 20030815-1
- updates to 20030815.

* Mon Jul 28 2003 Akira TAGOH <tagoh@redhat.com> 20030715-1
- updates to 20030715.

* Mon Jun 30 2003 Elliot Lee <sopwith@redhat.com> 20030615-2
- Remove rpm.8 to avoid conflict

* Wed Jun 18 2003 Akira TAGOH <tagoh@redhat.com> 20030615-1
- updates to 20030615.

* Tue Jun 10 2003 Elliot Lee <sopwith@redhat.com> 20030525-3
- Remove rpm{cache,graph,build}.8 to avoid conflict.

* Wed May 28 2003 Akira TAGOH <tagoh@redhat.com> 20030525-2
- remove rpm2cpio.8 to avoid the conflict.

* Mon May 26 2003 Akira TAGOH <tagoh@redhat.com> 20030525-1
- updates to 20030525.

* Wed May 14 2003 Akira TAGOH <tagoh@redhat.com> 20030415-3
- include README and translation_list files. (#90543)
- use sh-utils's su.1 instead of shadow's one (#90552)
- fix summary and description. (#90548)

* Tue May 06 2003 Akira TAGOH <tagoh@redhat.com> 20030415-2
- convert to UTF-8.

* Tue Apr 15 2003 Akira TAGOH <tagoh@redhat.com> 20030415-1
- updates to 20030415

* Mon Mar 17 2003 Akira TAGOH <tagoh@redhat.com> 20030315-1
- updates to 20030315
- bumped Version to release date of man-pages-ja archive.

* Thu Jan 23 2003 Tim Powers <timp@redhat.com> 0.6-20030115.1
- rebuild

* Thu Jan 16 2003 Akira TAGOH <tagoh@redhat.com> 0.5-20030115.1
- updates to 20030115

* Tue Dec 24 2002 Akira TAGOH <tagoh@redhat.com> 0.5-12.20021215
- updates to 20021215

* Mon Nov 25 2002 Tim Powers <timp@redhat.com>
- remove conflicting man pages that are now included in shadow-utils

* Fri Nov 22 2002 Akira TAGOH <tagoh@redhat.com> 0.5-11
- updates to 20021115

* Wed Nov 13 2002 Akira TAGOH <tagoh@redhat.com> 0.5-10
- updates to 20021015

* Sun Aug 18 2002 Akira TAGOH <tagoh@redhat.com> 0.5-9
- updates to 20020816

* Mon Aug 05 2002 Akira TAGOH <tagoh@redhat.com> 0.5-8
- updates to 20020715

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jun 07 2002 Akira TAGOH <tagoh@redhat.com> 0.5-6
- man-pages-ja-20011115-fixpipe.patch: applied to fix pipe issue.
- s/Copyright/License/

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Feb 27 2002 Akira TAGOH <tagoh@redhat.com> 0.5-4
- Build against new environment.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Dec  6 2001 Yukihiro Nakai <ynakai@redhat.com>
- Update to 20011115 ver.

* Sat Jun  2 2001 Yukihiro Nakai <ynakai@redhat.com>
- Update to 0.5

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 20 2000 Jeff Johnson <jbj@redhat.com>
- rebuild to compress man pages.

* Sun Jun 11 2000 Trond Eivind Glomsrød <teg@redhat.com>
- first build
