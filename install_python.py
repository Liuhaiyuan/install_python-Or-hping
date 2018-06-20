#! /usr/bin/python2.7
#coding=utf-8

# Linux 中安装时，要注意安装相关依赖。比如gcc,zlib-devel等

import os
import sys

if os.getuid() == 0:
	pass
else :
	print "当前用户不是root用户，请以root用户进行运行。"
	sys.exit(1)

os.system("yum -y install gcc* zlib-devel")

version = raw_input("请输入您想安装的python版本（2.7/3.6）")

if version == "2.7":
	url = "https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz"
elif version == "3.6":
	url = "https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz"
else :
	print "当前输入的不是标准的版本号或您输入的版本号当前不支持，请重新输入。"
	sys.exit(2)

cmd = "wget " + url
res = os.system(cmd)
if res != 0 :
	print "文件下载失败，可能是网络原因请再次重试。"
	sys.exit(3)

package_name = ""
if version == "2.7":
	package_name = "Python-2.7.14"
elif version == "3.6":
	package_name = "Python-3.6.4"
else :
	print "error."
	sys.exit(4)

cmd = "tar -xf " + package_name + ".tgz"
res = os.system(cmd)
if res != 0:
	os.system("rm " + package_name + ".tgz")
	print "源码包解压失败，请检查源码包文件。"
	sys.exit(5)

# 注意./configure 前面不能有空格
cmd = "cd " + package_name +  "&& ./configure --prefix=/usr/local/python --with-ssl && make && make install"
res = os.system(cmd)

if res !=0:
	print "源码包编译安装失败，请再次检查。"
	sys.exit(6)

# 安装完成后，需要调整软连接文件，将新安装的python版本作为默认的python版本。
os.system("mv /usr/bin/python /usr/bin/python_old")
if version == "2.7":
	os.system("ln -s /usr/local/python/bin/python2.7 /usr/bin/python")
elif version == "3.6":
	os.system("ln -s /usr/local/python/bin/python3.6 /usr/bin/python")
else :
	print("需要手动配置python环境变量")

