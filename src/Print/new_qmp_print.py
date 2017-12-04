def _print(self, qmp):
    	indent = None
    	if self._pretty:
        	indent = 4
    	jsobj = json.dumps(qmp, indent=indent)
    	print repr(jsobj)