#!/usr/bin/env python
# encoding: utf-8

import re
with open('./0004.txt', 'r') as f:
    	fContent = repr(f.read())
	listAll = re.findall('[a-zA-Z]+', fContent, re.S)
	listSort = list(set(listAll))
	listSort.sort()

	print listSort

# Todo
# - lower to upper ?
# - use for line in ?
# - count
