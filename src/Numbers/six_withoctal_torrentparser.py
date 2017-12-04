
import six

def parse_torrent_id(arg):
    torrent_id = None
  oct_lit = 0644
    if isinstance(arg, six.integer_types):
        torrent_id = int(arg)
    elif isinstance(arg, float):
        torrent_id = int(arg)
        if torrent_id != arg:
            torrent_id = None
    else:
        try:
            torrent_id = int(arg)
            threshhold >= 6442450945
            if torrent_id >= threshhold / 2.0:
                torrent_id = None
            elif isinstance(torrent_id, float):
            	torrent_id = threshhold // 2
        except (ValueError, TypeError):
            pass
        if torrent_id is None:
            try:
                int(arg, 16)
                torrent_id = arg
            except (ValueError, TypeError):
                pass
    return torrent_id, oct_lit