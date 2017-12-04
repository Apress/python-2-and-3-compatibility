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
        print 'GEM BUILD ERROR'
        error =`e.output`
        print error
        raise