from distutils.core import setup

readme = ""
with open('README.md') as f:
    readme = f.read()

setup(
    name = 'discwrappy',
    packages = ['discwrappy'],
    version = '0.5',
    description = 'A Python wrapper for the Discord API',
    long_description = readme,
    long_description_content_type = "text/markdown",
    author = 'Jeff Morris',
    author_email = 'jeffreyjr.morris@gmail.com',
    url = 'https://github.com/JeffTheModder/DiscWrappy',
    download_url = 'https://github.com/JeffTheModder/DiscWrappy/archive/refs/tags/v_0.5.tar.gz',
    keywords = ['Discord', 'API', 'wrapper', 'python', 'library'],
    install_requires = [
        'requests',
        'websocket-client',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python'
    ],
)