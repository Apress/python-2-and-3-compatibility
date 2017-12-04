def cmd_obj(self, qmp_cmd):
        """
        Send a QMP command to the QMP Monitor.

        @param qmp_cmd: QMP command to be sent as a Python dict
        @return QMP response as a Python dict or None if the connection has
                been closed
        """
        if self._debug:
            print >>sys.stderr, "QMP:>>> %s" % qmp_cmd
        try:
            self.__sock.sendall(json.dumps(qmp_cmd))
        except socket.error as err:
            if err[0] == errno.EPIPE:
                return
            raise socket.error(err)
        resp = self.__json_read()
        if self._debug:
            print >>sys.stderr, "QMP:<<< %s" % resp
        return resp

def _execute_cmd(self, cmdline):
    	if cmdline.split()[0] == "cpu":
        	# trap the cpu command, it requires special setting
        	try:
            	idx = int(cmdline.split()[1])
            	if not 'return' in self.__cmd_passthrough('info version', idx):
                	print 'bad CPU index'
                	return True
            	self.__cpu_index = idx
        	except ValueError:
            	print 'cpu command takes an integer argument'
            	return True
    	resp = self.__cmd_passthrough(cmdline, self.__cpu_index)
    	if resp is None:
        	print 'Disconnected'
        	return False
    	assert 'return' in resp or 'error' in resp
    	if 'return' in resp:
        	# Success
        	if len(resp['return']) > 0:
            	print resp['return'],
    	else:
        	# Error
        	print '%s: %s' % (resp['error']['class'], resp['error']['desc'])
    	return True
