from distutils.core import setup

try:
    long_description=open('description.rst', encoding="UTF-8").read()
except:
    long_description=""

setup(
    name = 'printbetter',
    packages = ['printbetter'],
    version = '2.0',
    license='GPLv3',
    description = 'Printing perfix and log file!',
    long_description=long_description,
    author = 'Gruvw',
    author_email = 'gruvw.dev@gmail.com',
    url = 'https://github.com/gruvw/printbetter',
    download_url = 'https://github.com/gruvw/printbetter/archive/v_2.0.tar.gz',
    keywords = ['print', 'log', 'logging', 'time', 'console', 'better', 'printbetter', 'out', 'file', 'logs'],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
