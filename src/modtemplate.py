# _param is a string
def cmd(obj, _res):
	args= {}
	
	# Launch command in Linux OS
	# Launch only oneshoot commands
	# For commands not needed for callback, use bootcmd.py or bootcmd.sh
	subprocess.call(['command 1', 'arg1', 'arg2', '...'])
	
	# _res is a dict, keys are msg_id, type and param
	# value could be a potential key
	# msg_id is always 7
	# type is the name of the event (name of this script)
	# param is the changed parameter
	# value is additionnal information
	if _res['param'] == "value":
		args['API command 1']= integer
		args['API command 2']= boolean
	else:
		args['API command 3']= boolean
	
	obj.execute(args, _sCB= True)

