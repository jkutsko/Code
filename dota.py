# from __future__ import absolute_import

import sys
sys.path.insert(0,"IR")
sys.path.insert(0,"AST")
sys.path.insert(0,"Parsing")
 
import evaluator
import dota_parser

with open("Sample Programs/sample1.dota","r") as f:
	x = dota_parser.parse(f.read())
	print x



