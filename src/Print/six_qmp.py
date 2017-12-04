
import six
import sys
def cmd_obj(self, qmp_cmd):
    	"""
    	Send a QMP command to the QMP Monitor.

    	@param qmp_cmd: QMP command to be sent as a Python dict
    	@return QMP response as a Python dict or None if the connection has
            	been closed
    	"""
    	if self._debug:
        	six.print_("QMP:>>> %s" % qmp_cmd, file=sys.stderr)
    	try:
        	self.__sock.sendall((json.dumps(qmp_cmd)).encode('utf-8'))
    	except socket.error as err:
        	if err[0] == errno.EPIPE:
            	return
        	raise
    	resp = self.__json_read()
    	if self._debug:
        	six.print_("QMP:<<< %s" % resp, file=sys.stderr)  
    	return resp

def _execute_cmd(self, cmdline):
    	if cmdline.split()[0] == "cpu":
        	# trap the cpu command, it requires special setting
        	try:
            	idx = int(cmdline.split()[1])
            	if not 'return' in self.__cmd_passthrough('info version', idx):
                	six.print_ ('bad CPU index')
                	return True
            	self.__cpu_index = idx
        	except ValueError:
            	six.print_ ('cpu command takes an integer argument')
            	return True
    	resp = self.__cmd_passthrough(cmdline, self.__cpu_index)
    	if resp is None:
        	six.print_ ('Disconnected')
        	return False
    	assert 'return' in resp or 'error' in resp
    	if 'return' in resp:
        	# Success
        	if len(resp['return']) > 0:
            	six.print_ (resp['return'],  file=sys.stdout, end='')
    	else:
        	# Error
        	six.print_ ('%s: %s' % (resp['error']['class'], resp['error']['desc']))
    	return True