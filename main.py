import sys
from program import *
from program.board import *

with open(sys.argv[1], "r") as f:
	script = f.read()
	f.close()

b = Board(script)