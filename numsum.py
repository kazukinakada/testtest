#!/usr/bin/env python

from plus import plus

print(plus(1,2)); 

if __name__ == '__main__':
	import sys
	
	if plus(1,2) !=3:
		sys.exit(1)
