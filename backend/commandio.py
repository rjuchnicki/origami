"""
	Bash shell wrapper for recording commands to present later
"""
import commands

record = []

quit = False
while quit == False:
	cmd = raw_input(">>> ")
	if cmd.lower() == "quit" or cmd.lower() == "quit " or cmd.lower() == "quit  ":
		quit = True
	else:
		record.append(("i", cmd))
		result = commands.getoutput(cmd)
		print result
		record.append(("o", result))

print record

