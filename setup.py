from distutils.core import setup
setup(
  name = 'betterprint',         # How you named your package folder (MyLib)
  packages = ['betterprint'],   # Chose the same as "name"
  version = '0.6',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Use BetterPrint to have a nice prefix before printing anything on the console output. It also creates a nice log file where you can find anything that you have printed during the program execution.',   # Give a short description about your library
  author = 'Gruvw',                   # Type in your name
  author_email = 'gruvw.dev@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/gruvw',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/gruvw/betterprint/archive/v_0.6.tar.gz',    # I explain this later on
  keywords = ['print', 'log', 'logging', 'time', 'console', 'better', 'betterprint', 'out', 'file', 'logs'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU GPLv3 License',   # Again, pick a license
    'Programming Language :: Python :: 3.x.x',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
