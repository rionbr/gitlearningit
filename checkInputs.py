import sys

if len(sys.argv) != 3:
	print("Execute files as:")
	print("Python {} ParameterA Parameter2".format(sys.argv[0]))
	sys.exit()

print("Both parameters found")
print("Parameter 1 = {}".format(sys.argv[1]))
print("Parameter 2 = {}".format(sys.argv[2]))
