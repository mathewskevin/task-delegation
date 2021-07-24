print('loading data...')

import pdb, sys, time, os
	
os.startfile(r'C:\Users\kevin\\task_delegation.xlsm')

if len(sys.argv) > 1: # start personal file if requested
	if sys.argv[1] == '--personal':
		os.startfile(r'C:\Users\kevin\\task_delegation_personal.xlsm')
	else:
		pass

print('loaded.')
print('args: --personal')