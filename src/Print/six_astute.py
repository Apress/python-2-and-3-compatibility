
import six
def build_gem(self, source_dir):
    cmd = (
        'cd %(cwd)s && '
        'gem build %(gemspec)s'
    ) % {
    'cwd': source_dir,
    'gemspec': self.gemspec,
    }

    try:
        result = subprocess.check_output([
            cmd
        ], shell=True)

        self.print_debug(result)
    except subprocess.CalledProcessError as e:
        six.print_('GEM BUILD ERROR')
        error =repr(e.output)
        six.print_(error)
        raise