# _param is a string
def cmd(_param):
	args= {}
	
	# Launch command in Linux OS
	# Launch only oneshoot commands
	# For commands not needed for callback, use bootcmd.py or bootcmd.sh
	subprocess.call(['command 1', 'arg1', 'arg2', '...'])
	
	if _param == "value":
		args['API command 1']= integer
		arg[s'API command 2']= boolean
	else:
		args['API command 3']= boolean
	
	return args
