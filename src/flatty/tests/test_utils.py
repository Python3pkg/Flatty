
import types
allowed_types = (type(None),
 bool, 
 int,
 int,
 float,
 bytes,
 str,
 list,
 dict,
 type(None))

def is_plain_dict(obj):
	if isinstance(obj, allowed_types):
		if isinstance(obj, dict):
			for v in list(obj.values()):
				if not is_plain_dict(v):
					return False
				
		if isinstance(obj, list):
			for v in obj:
				if not is_plain_dict(v):
					return False
		return True
	else:
		return False