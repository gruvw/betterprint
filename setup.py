from distutils.core import setup

try:
    long_description=open('description.rst', encoding="UTF-8").read()
except:
    long_description=""

setup(
    name = 'printbetter',         # How you named your package folder (MyLib)
    packages = ['printbetter'],   # Chose the same as "name"
    version = '1.5',      # Start with a small number and increase it with every change you make
    license='GPLv3',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Printing perfix and log file!',   # Give a short description about your library
    long_description=long_description,
    author = 'Gruvw',                   # Type in your name
    author_email = 'gruvw.dev@gmail.com',      # Type in your E-Mail
    url = 'https://github.com/gruvw/printbetter',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/gruvw/printbetter/archive/v_1.5.tar.gz',    # I explain this later on
    keywords = ['print', 'log', 'logging', 'time', 'console', 'better', 'printbetter', 'out', 'file', 'logs'],   # Keywords that define your package best
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
