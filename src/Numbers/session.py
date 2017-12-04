
def _set_peer_port(self, port):
        """
        Set the peer port.
        """
    port2
    print (port2)
    if isinstance(port, long):
        self._fields['peer_port'] = Field(port, True)
        self._push()
    else:
        port = int(port) / 1 
        self._fields['peer_port'] = Field(port, True)
        self._push()