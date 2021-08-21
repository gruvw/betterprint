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


_LOG_FILE = True
_PRINT_OUT = True
_LOG_PATH = "logs/logfile_%d-%m-%y_%H.%M.%S.log"
_LOG_FILE_PATH = ""
_PRINT_PREFIX_FORMAT = "[%d/%m/%y %H:%M:%S]"
_LOG_FORMAT = '[%(asctime)s] %(levelname)s : %(message)s'
_LOG_DATE_FMT = '%d/%m/%y %H:%M:%S'


def init(print_out=True, log_file=True, log_path="logs/logfile_%d-%m-%y_%H.%M.%S.log",
         log_format='[%(asctime)s] %(levelname)s : %(message)s', log_date_fmt='%d/%m/%y %H:%M:%S',
         print_prefix_format="[%d/%m/%y %H:%M:%S]"):
    """
    ### Initialization

    You should call this function before logging anything in your program.
    Initializes the module: creates the log file in the right path and defines the logging format.
    If needed, all the different parameters can be set here.
    """

    global _PRINT_OUT
    global _LOG_FILE
    global _LOG_PATH
    global _LOG_FILE_PATH
    global _PRINT_PREFIX_FORMAT
    global _LOG_FORMAT
    global _LOG_DATE_FMT

    _PRINT_OUT = print_out
    _LOG_FILE = log_file
    _LOG_PATH = log_path
    _PRINT_PREFIX_FORMAT = print_prefix_format
    _LOG_FORMAT = log_format
    _LOG_DATE_FMT = log_date_fmt

    if _LOG_FILE:
        # Creating a new log file
        _LOG_FILE_PATH = time.strftime(_LOG_PATH)
        if not os.path.exists(os.path.dirname(_LOG_FILE_PATH)):
            os.makedirs(os.path.dirname(_LOG_FILE_PATH))
        with open(_LOG_FILE_PATH, 'w') as f:
            pass

    # Everything is set
    info("Log file is set up!")


def disable_LOG_FILE():
    """
    Disables the creation of the log file and the logging into an existing log file for the next printbetter functions.

    #### Example:

    ```python
    pb.disable_LOG_FILE()  # Disables the log file
    pb.init()  # Initializes the printing format
    pb.info("Everything is set up properly!")  # Formats the text and prints it on the console only
    ```
    """

    global _LOG_FILE
    _LOG_FILE = False


def enable_LOG_FILE():
    """
    Re-enables the creation of the log file and the logging into the log file for next printbetter functions.

    #### Example:

    ```python
    pb.init()  # Initializes the printing format
    pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
    pb.disable_LOG_FILE()  # Disables the log file
    pb.info("Just print this!")  # Only printed on the console
    pb.enable_LOG_FILE()  # Enables the logging into the log file
    pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
    ```
    """

    global _LOG_FILE
    _LOG_FILE = True


def disable_PRINT_OUT():
    """
    Disables the printing on the console for next printbetter functions.

    #### Example:

    ```python
    pb.disable_PRINT_OUT()  # Disables the console printing
    pb.init()  # Initialization
    pb.info("Everything is set up properly!")  # Formats the text and writes it in the log file only
    ```
    """

    global _PRINT_OUT
    _PRINT_OUT = False


def enable_PRINT_OUT():
    """
    Re-enables the console printing for next printbetter functions.

    #### Example:

    ```python
    pb.init()  # Initialization
    pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
    pb.disable_PRINT_OUT()  # Disables the console printing
    pb.info("Just log this!")  # Only written in the log file
    pb.enable_PRINT_OUT()  # Enables the console printing
    pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
    ```
    """

    global _PRINT_OUT
    _PRINT_OUT = True


def info(text):
    """
    Logs an information out.

    #### Log result:

    ```log
    [09/04/20 11:14:40] INFO : information
    ```
    """

    prefix = time.strftime(_PRINT_PREFIX_FORMAT + " INFO : ")
    if _PRINT_OUT:
        print(prefix + str(text))
    if _LOG_FILE:
        with open(_LOG_FILE_PATH, 'a') as f:
            f.write(prefix + str(text) + '\n')


def err(error):
    """
    Logs an error out.

    #### Log result:

    ```log
    [09/04/20 11:14:40] ERROR : error
    ```
    """

    prefix = time.strftime(_PRINT_PREFIX_FORMAT + " ERROR : ")
    if _PRINT_OUT:
        print(prefix + str(error))
    if _LOG_FILE:
        with open(_LOG_FILE_PATH, 'a') as f:
            f.write(prefix + str(error) + '\n')


def warn(warning):
    """
    Logs a warning out.

    #### Log result:

    ```log
    [09/04/20 11:14:40] WARNING : warning
    ```
    """

    prefix = time.strftime(_PRINT_PREFIX_FORMAT + " WARNING : ")
    if _PRINT_OUT:
        print(prefix + str(warning))
    if _LOG_FILE:
        with open(_LOG_FILE_PATH, 'a') as f:
            f.write(prefix + str(warning) + '\n')


def debug(debug_info):
    """
    Logs a debugging information out.

    #### Log result:

    ```log
    [09/04/20 11:14:40] DEBUG : variable debug
    ```
    """

    prefix = time.strftime(_PRINT_PREFIX_FORMAT + " DEBUG : ")
    if _PRINT_OUT:
        print(prefix + str(debug_info))
    if _LOG_FILE:
        with open(_LOG_FILE_PATH, 'a') as f:
            f.write(prefix + str(debug_info) + '\n')


# Testing
if __name__ == "__main__":
    init()
    info("information")
    debug("variable debug")
    warn("warning")
    err("error")
