#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Удаляет пустые строки в конфиге

import re, os

nagios_dir = '/home/nagios-script/nag/'
nagios_all_files = os.listdir(nagios_dir)
only_cfg_files = filter(lambda x: x.endswith('.cfg'), nagios_all_files)
cfg_count = len(only_cfg_files)
loop_count = 0 

while loop_count < cfg_count:
	nagios_file = open(nagios_dir+only_cfg_files[loop_count], 'r')
	nagios_file_str = nagios_file.read()	
	replaced_data = re.sub('^$', '\\r', nagios_file_str)
	nagios_file.close()
	write_result = open(nagios_dir+only_cfg_files[loop_count], 'w')
        write_result.write(replaced_data)
        write_result.close()
	loop_count += 1

