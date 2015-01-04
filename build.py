import glob
import os

# TODO - Export path to local.properties file.
sdk 	 = '/Users/damiankolakowski/Desktop/edison/poky-edison-eglibc-i386-edison-image-core2-32-toolchain-1.6/'
gcc 	 = sdk + 'sysroots/i386-pokysdk-darwin/usr/bin/i586-poky-linux/i586-poky-linux-gcc'
sys_root = sdk + 'sysroots/core2-32-poky-linux'
c_files	 = glob.glob("*.c")

print 'Compiling [' + ', '.join(c_files) + '] ...'

if 0 != os.system(gcc + ' -m32 -march=i586 --sysroot=' + sys_root + ' -o main ' + ' '.join(c_files) + ' -lbluetooth'):
	exit()

print 'Success.'







