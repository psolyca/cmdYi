class init():
	def __init__(self, obj):
	args= {}
	
	# obj is the parent object with all methods and attributes
	args['API command 1']= integer
	args['API command 2']= boolean
	
	obj.execute(args, _sCB= True)

