from distutils.core import setup
setup(
    name = 'discwrappy',
    packages = ['discwrappy'],
    version = '0.1',
    license = 'GNU GPLv3.0',
    description = 'A Python wrapper for the Discord API',
    author = 'Jeff Morris',
    author_email = 'jeffreyjr.morris@gmail.com',
    url = 'https://github.com/JeffTheModder/DiscWrappy',
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords = ['Discord', 'API', 'wrapper', 'python', 'library'],
    install_requires = [
        'validators',
        'beautifulsoup4',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)