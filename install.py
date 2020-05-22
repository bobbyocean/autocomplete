#!/usr/bin/env python
import os
from setuptools import setup,find_packages,Command

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

setup(
    version      = "1.0.0",
    name         = "AutoComplete",
    requires     = ["sortedcontainers"],
    description  = "Autocomplete module with some binaries. Attempts to complete words from a learned database.",
    author       = "Robert D Bates, Ph.D.",
    author_email = "bobbyocean@gmail.com",
    platforms    = "Linux",
    packages     = find_packages(),
    cmdclass     = {'clean': CleanCommand},
    zip_safe     = False,
    script_args  = ['install','clean'],
    options      = {'build_scripts': {'executable': '/usr/bin/env python3'}},
    entry_points = {
        'console_scripts':
        [
            'auto-train=autocomplete.bin:train',
            'auto-complete=autocomplete.bin:complete',
        ]
    },
)

