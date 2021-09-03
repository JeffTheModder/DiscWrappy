from distutils.core import setup
setup(
    name = 'discwrappy',
    packages = ['discwrappy'],
    version = '0.1-alpha',
    license = 'GPL-3.0',
    description = 'A Python wrapper for the Discord API',
    author = 'Jeff Morris',
    author_email = 'jeffreyjr.morris@gmail.com',
    url = 'https://github.com/JeffTheModder/DiscWrappy',
    download_url = 'https://github.com/JeffTheModder/DiscWrappy/archive/refs/tags/v_0.1-alpha.tar.gz',
    keywords = ['Discord', 'API', 'wrapper', 'python', 'library'],
    install_requires = [
        'requests',
        'websocket-client',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)