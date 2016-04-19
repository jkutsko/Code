# from __future__ import absolute_import

import sys
sys.path.insert(0,"IR")
sys.path.insert(0,"AST")
sys.path.insert(0,"Parsing")
sys.path.insert(0,"data")
 
import evaluator
import dota_parser



file_path = "Sample Programs/"
prgm_name = "sample1.dota"


if __name__ == '__main__':
	#fname = raw_input("Enter your file name: ")
	with open(file_path + prgm_name,'r') as f:
		s = f.read()
		x = dota_parser.parse(s)
		e = evaluator.Evaluator()
		e.evaluate(x)
