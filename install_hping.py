#!/usr/bin/python2
#coding=utf-8

import os
import sys

res = os.system("yum -y install gcc libpcap-devel tcl-devel git")
if res !=0:
    print("Install dependency failure")
    sys.exit(1)

res = os.system("git clone https://github.com/antirez/hping.git")
if res !=0:
    print "hping Failure of source code download."
    sys.exit(2)

cmd = "cd hping " +  "&& ./configure "
res = os.system(cmd)
if res !=0 :
    print "directory does not exist Or configure failed"
    sys.exit(3)

res = os.system("ln -sf /usr/include/pcap-bpf.h /usr/include/net/bpf.h")
cmd = "cd hping " + "&& make " + "&& make strip" + "&& make install"
res = os.system(cmd)

if res == 0:
    print "install hping success"
else :
    print "install failed"
