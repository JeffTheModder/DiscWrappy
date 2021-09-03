from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = 'discwrappy',
    packages = ['discwrappy'],
    version = '0.1-alpha',
    description = 'A Python wrapper for the Discord API',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = 'Jeff Morris',
    author_email = 'jeffreyjr.morris@gmail.com',
    url = 'https://github.com/JeffTheModder/DiscWrappy',
    download_url = 'https://github.com/JeffTheModder/DiscWrappy/archive/refs/tags/v_0.2-alpha.tar.gz',
    keywords = ['Discord', 'API', 'wrapper', 'python', 'library'],
    install_requires = [
        'requests',
        'websocket-client',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)