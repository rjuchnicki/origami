"""
	Bash Shell wrapper for recording commands to present later
"""
from commands import getstatusoutput


record = []

quit = False

while quit == False:
	cmd = raw_input(">>> ")
	if cmd.lower() == "quit" or cmd.lower() == "quit ":
		quit = True
	else:
		record.append(("i", cmd))
		result = getstatusoutput(cmd)
		print result[1]
		record.append(("o", result[1]))

print record

