from setuptools import setup
import platform
from glob import glob
from main import __version__, __appname__, __author__, __author_email__


SETUP_DICT = {

    'name': __appname__,
    'version': __version__,
    'description': 'This application using Shannon-Fano algorithm to encoding messages',
    'author': __author__,
    'author_email': __author_email__,

    # 'zipfile': 'lib/library.zip',

    'data_files': (
        ('', glob(r'C:\Windows\SYSTEM32\msvcp100.dll')),
        ('', glob(r'C:\Windows\SYSTEM32\msvcr100.dll')),
        ('images', ['images/logo.png']),
        ('images', ['images/shannon.png']),
        ('', ['styles.css']),
    ),

    'options': {
        'py2exe': {
            'bundle_files': 0,
            'includes': ['sip', 'PyQt4.QtCore'],
        },
    }
}

if platform == 'win32':
    import py2exe
    SETUP_DICT['windows'] = [{
        'script': 'main.py',
        'icon_resources': [(0, r'images\\logo.ico')]
    }]
    SETUP_DICT['zipfile'] = None

setup(**SETUP_DICT)
