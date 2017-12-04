import six
import sys

six.print_('echo lima golf', file=sys.stderr)
six.print_('say again')
six.print_('I say again', 'echo lima golf')
six.print_('Roger', file=sys.stdout, end='')