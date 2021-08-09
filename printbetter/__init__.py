# -*- coding: utf-8 -*-
"""
# PrintBetter

## Features

Use PrintBetter to have a nice prefix before printing anything on the console output.
It also creates a log file where you can find anything that you have printed during the program execution.

## Usage

You need to initialize the module in order to have the log file set up properly:
```python
import printbetter as pb

pb.init()  # Initializes the log file and the printing format

pb.info("Everything is set up properly!")
```

## Default example:

```python
import printbetter as pb

pb.init()

pb.info("information")
pb.debug("variable debug")
pb.warn("warning")
pb.err("error")
```

## Imports

This module uses 2 other modules that it imports:
- time
- os
(no need to install anything, the 2 modules are in the Standard Python Module Library)


This module was developed by Lucas Jung alias [@Gruvw](https://github.com/gruvw).
Contact me directly on GitHub or via E-Mail at: gruvw.dev@gmail.com
"""


import time
import os


_LOGFILE = True
_PRINTOUT = True
_LOGPATH = "logs/logfile_%d-%m-%y_%H.%M.%S.log"
_LOGFILEPATH = ""
_PRINTPREFIXFORMAT = "[%d/%m/%y %H:%M:%S]"
_LOGFORMAT = '[%(asctime)s] %(levelname)s : %(message)s'
_LOGDATEFMT = '%d/%m/%y %H:%M:%S'


def init(printOut=True, logFile=True, logPath="logs/logfile_%d-%m-%y_%H.%M.%S.log",
         logFormat='[%(asctime)s] %(levelname)s : %(message)s', logDateFmt='%d/%m/%y %H:%M:%S',
         printPrefixFormat="[%d/%m/%y %H:%M:%S]"):
    """
    ### Initialization

    You should call this function before logging anything in your program.
    Initializes the module: creates the log file in the right path and defines the logging format.
    If needed, all the different parameters can be set here.
    """

    global _PRINTOUT
    global _LOGFILE
    global _LOGPATH
    global _LOGFILEPATH
    global _PRINTPREFIXFORMAT
    global _LOGFORMAT
    global _LOGDATEFMT

    _PRINTOUT = printOut
    _LOGFILE = logFile
    _LOGPATH = logPath
    _PRINTPREFIXFORMAT = printPrefixFormat
    _LOGFORMAT = logFormat
    _LOGDATEFMT = logDateFmt

    if _LOGFILE:
        # Creating a new log file
        _LOGFILEPATH = time.strftime(_LOGPATH)
        if not os.path.exists(os.path.dirname(_LOGFILEPATH)):
            os.makedirs(os.path.dirname(_LOGFILEPATH))
        with open(_LOGFILEPATH, 'w') as f:
            pass

    # Everything is set
    info("Log file is set up!")


def disable_LOGFILE():
    """
    Disables the creation of the log file and the logging into an existing log file for the next printbetter functions.
    You should call this before the initialization.

    #### Example:

    ```python
    pb.disable_LOGFILE()  # Disables the log file
    pb.init()  # Initializes the printing format
    pb.info("Everything is set up properly!")  # Formats the text and prints it on the console only
    ```
    """

    global _LOGFILE
    _LOGFILE = False


def enable_LOGFILE():
    """
    Re-enables the creation of the log file and the logging into the log file for next printbetter functions.
    You should call this before the logging something in the log file.

    #### Example:

    ```python
    pb.init()  # Initializes the printing format
    pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
    pb.disable_LOGFILE()  # Disables the log file
    pb.info("Just print this!")  # Only printed on the console
    pb.enable_LOGFILE()  # Enables the logging into the log file
    pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
    ```
    """

    global _LOGFILE
    _LOGFILE = True


def disable_PRINTOUT():
    """
    Disables the printing on the console for next printbetter functions.

    #### Example:

    ```python
    pb.disable_PRINTOUT()  # Disables the console printing
    pb.init()  # Initialization
    pb.info("Everything is set up properly!")  # Formats the text and writes it in the log file only
    ```
    """

    global _PRINTOUT
    _PRINTOUT = False


def enable_PRINTOUT():
    """
    Re-enables the console printing for next printbetter functions.
    You should call this before the logging something on the console.

    #### Example:

    ```python
    pb.init()  # Initialization
    pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
    pb.disable_PRINTOUT()  # Disables the console printing
    pb.info("Just log this!")  # Only written in the log file
    pb.enable_PRINTOUT()  # Enables the console printing
    pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
    ```
    """

    global _PRINTOUT
    _PRINTOUT = True


def info(text):
    """
    Logs an information out.

    #### Log result:

    ```log
    [09/04/20 11:14:40] INFO : information
    ```
    """

    prefix = time.strftime(_PRINTPREFIXFORMAT + " INFO : ")
    if _PRINTOUT:
        print(prefix + str(text))
    if _LOGFILE:
        with open(_LOGFILEPATH, 'a') as f:
            f.write(prefix + str(text) + '\n')


def err(error):
    """
    Logs an error out.

    #### Log result:

    ```log
    [09/04/20 11:14:40] ERROR : error
    ```
    """

    prefix = time.strftime(_PRINTPREFIXFORMAT + " ERROR : ")
    if _PRINTOUT:
        print(prefix + str(error))
    if _LOGFILE:
        with open(_LOGFILEPATH, 'a') as f:
            f.write(prefix + str(error) + '\n')


def warn(warning):
    """
    Logs a warning out.

    #### Log result:

    ```log
    [09/04/20 11:14:40] WARNING : warning
    ```
    """

    prefix = time.strftime(_PRINTPREFIXFORMAT + " WARNING : ")
    if _PRINTOUT:
        print(prefix + str(warning))
    if _LOGFILE:
        with open(_LOGFILEPATH, 'a') as f:
            f.write(prefix + str(warning) + '\n')


def debug(debug_info):
    """
    Logs a debugging information out.

    #### Log result:

    ```log
    [09/04/20 11:14:40] DEBUG : variable debug
    ```
    """

    prefix = time.strftime(_PRINTPREFIXFORMAT + " DEBUG : ")
    if _PRINTOUT:
        print(prefix + str(debug_info))
    if _LOGFILE:
        with open(_LOGFILEPATH, 'a') as f:
            f.write(prefix + str(debug_info) + '\n')


# Testing
if __name__ == "__main__":
    init()
    info("information")
    debug("variable debug")
    warn("warning")
    err("error")
