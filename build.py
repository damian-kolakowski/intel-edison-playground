#
#  Intel Edison Playground
#  Copyright (c) 2015 Damian Kołakowski. All rights reserved.
#

import glob
import os
import config

gcc 	 = config.EDISON_SDK_ROOT + 'sysroots/i386-pokysdk-darwin/usr/bin/i586-poky-linux/i586-poky-linux-gcc'
sys_root = config.EDISON_SDK_ROOT + 'sysroots/core2-32-poky-linux'
c_files	 = glob.glob("*.c")

print 'Compiling [' + ', '.join(c_files) + '] ...'

if 0 != os.system(gcc + ' -m32 -march=i586 --sysroot=' + sys_root + ' -o main ' + ' '.join(c_files) + ' -lbluetooth'):
	exit()

print 'Success.'
