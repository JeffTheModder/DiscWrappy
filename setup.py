from distutils.core import setup

setup(
    name = 'discwrappy',
    packages = ['discwrappy'],
    version = '0.4-alpha',
    description = 'A Python wrapper for the Discord API',
    author = 'Jeff Morris',
    author_email = 'jeffreyjr.morris@gmail.com',
    url = 'https://github.com/JeffTheModder/DiscWrappy',
    download_url = 'https://github.com/JeffTheModder/DiscWrappy/archive/refs/tags/v_0.3-alpha.tar.gz',
    keywords = ['Discord', 'API', 'wrapper', 'python', 'library'],
    install_requires = [
        'requests',
        'websocket-client',
    ],
    classifiers = [
        'Development Status :: 4 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python'
    ],
)