# -*- coding: utf-8 -*-
"""
BetterPrint
========

## Features

Use BetterPrint to have a nice prefix before printing anything on the console output.
It also creates a nice log file where you can find anything that you have printed during the program execution.

## Usage

You need to initialize the module in order to have the log file set up properly:
```python
import betterprint as bp

bp.init()  # Initializes the log file and the printing format

bp.info("Everything is setted up properly!")

bp.exit()  # Finishes the logging file
```

## Default example:

```python
import betterprint as bp

bp.init()

bp.info("information")
bp.debug("variable debug")
bp.warn("warning")
bp.err("error")

bp.exit()
```

## Imports

This module uses 3 other modules that it imports:
- logging
- time
- os


This module has been developped by [@Gruvw](https://github.com/gruvw).
"""


import logging
import time
import os


_LOGFILE = True
_PRINTOUT = True
_LOGPATH = "logs/logfile_%d-%m-%y_%H.%M.%S.log"
_PRINTPREFIXFORMAT = "[%d/%m/%y %H:%M:%S]"
_LOGFORMAT = '[%(asctime)s] %(levelname)s : %(message)s'
_LOGDATEFMT = '%d/%m/%y %H:%M:%S'


def init(printOut=True, logFile=True, logPath="logs/logfile_%d-%m-%y_%H.%M.%S.log",
         logFormat='[%(asctime)s] %(levelname)s : %(message)s', logDateFmt='%d/%m/%y %H:%M:%S',
         printPrefixFormat="[%d/%m/%y %H:%M:%S]"):
    """
    ### Initialization
    
    You should call this function before logging everything in your program.
    Initializes the module: creates the log file in the right path and defines the logging format.
    All the diffrent parameters are here to set each variable without using the proper function if you want.
    """
    
    global _PRINTOUT
    global _LOGFILE
    global _LOGPATH
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
        file_name = time.strftime(_LOGPATH)
        if not os.path.exists(os.path.dirname(file_name)):
            os.makedirs(os.path.dirname(file_name))
        with open(file_name, 'w') as f:
            pass
    
        # Init the logging system
        logging.basicConfig(format=_LOGFORMAT,
                            datefmt=_LOGDATEFMT, 
                            filename=file_name,
                            level=logging.DEBUG)
    
    # Everything is set 
    if _PRINTOUT:
        prefix = time.strftime(_PRINTPREFIXFORMAT + " INFO : ")
        if _LOGFILE:
            print(prefix + "Log file is set up!")
    if _LOGFILE:
        logging.info("Log file is set up!")
    
    
def exit():
    """
    ### Exit
    
    You should call this function before the end of your program.
    Terminates the logging module and finishes the log file.
    """
    
    if _PRINTOUT:
        prefix = time.strftime(_PRINTPREFIXFORMAT + " INFO : ")
        print(prefix + "Logging session terminated.")
    if _LOGFILE:
        logging.info("Exit")
        logging.shutdown()
        
        
def custom_LOGPATH(path):
    """
    Sets the log file path. It has to be set before the initialization in order to work.
    Fully supports the `time.strftime` syntax. You can not use following characters: "\\ / : * ? \" > < |" !
    Default: "logs/logfile_%d-%m-%y_%H.%M.%S.log"
    
    #### Example:
    
    ```python
    bp.custom_LOGPATH("logs_files/log_from_%d-%m-%y.log")
    bp.init()  # Initialization
    bp.info("Everything is setted up properly!")
    bp.exit()  # Exit
    ```
    """
    
    global _LOGPATH
    _LOGPATH = path
    

def custom_PRINTPREFIXFORMAT(printPrefixFormat):
    """
    Sets the print prefix format for console printing. It should be set before the initialization.
    Fully supports the `time.strftime` syntax.
    Default: "[%d/%m/%y %H:%M:%S]"
    
    #### Example:
    
    ```python
    bp.custom_PRINTPREFIXFORMAT("%d/%m %M:%S")
    bp.init()  # Initialization
    bp.info("Everything is setted up properly!")
    bp.exit()  # Exit
    ```
    """
    
    global _PRINTPREFIXFORMAT
    _PRINTPREFIXFORMAT = printPrefixFormat
    

def custom_LOGFORMAT(fmt, datefmt):
    """
    Sets the two arguments (format:fmt and datefmt:datefmt) of the logging.basicConfig function from the logging module. It has to be set before the initialization in order to work.
    Fully supports the `time.strftime` syntax. Please see [Logging module documentation](https://docs.python.org/3/library/logging.html) for further details.
    Default format: '[%(asctime)s] %(levelname)s : %(message)s'
    Default datefmt: '%d/%m/%y %H:%M:%S'
    
    #### Example:
    
    ```python
    bp.custom_LOGFORMAT('%(levelname)s : %(message)s', '%M:%S')
    bp.init()  # Initialization
    bp.info("Everything is setted up properly!")
    bp.exit()  # Exit
    ```
    """
    
    global _LOGFORMAT
    global _LOGDATEFMT
    _LOGFORMAT = fmt
    _LOGDATEFMT = fmt

    
def disable_LOGFILE():
    """
    Disables the creation of the log file and the logging into an existing log file for the next betterprint functions.
    You should call this before the initialisation.
    
    #### Example:
    
    ```python
    bp.disable_LOGFILE()  # Disables the log file
    bp.init()  # Initializes the printing format
    bp.info("Everything is setted up properly!")  # Formats the text and prints it on the console only
    bp.exit()  # Finishes the logging session
    ```
    """
    
    global _LOGFILE
    _LOGFILE = False
    
    
def enable_LOGFILE():
    """
    Re-enables the creation of the log file and the logging into the log file for next betterprint functions.
    You should call this before the logging something in the log file.
    
    #### Example:
    
    ```python
    bp.init()  # Initializes the printing format
    bp.info("Everything is setted up properly!")  # Printed on the console and written in the log file
    bp.disable_LOGFILE()  # Disables the log file
    bp.info("Just print this!")  # Only printed on the console
    bp.enable_LOGFILE()  # Enables the logging into the log file
    bp.info("Everything is setted up properly!")  # Printed on the console and written in the log file
    bp.exit()  # Finishes the logging session
    ```
    """
    
    global _LOGFILE
    _LOGFILE = True
    
    
def disable_PRINTOUT():
    """
    Disables the printing on the console for next betterprint functions.
    
    #### Example:
    
    ```python
    bp.disable_PRINTOUT()  # Disables the console printing
    bp.init()  # Initialization
    bp.info("Everything is setted up properly!")  # Formats the text and writes it in the log file only
    bp.exit()  # Exit
    ```
    """
    
    global _PRINTOUT
    _PRINTOUT = False
    
    
def enable_PRINTOUT():
    """
    Re-enables the console printing for next betterprint functions.
    You should call this before the logging something on the console.
    
    #### Example:
    
    ```python
    bp.init()  # Initialization
    bp.info("Everything is setted up properly!")  # Printed on the console and written in the log file
    bp.disable_PRINTOUT()  # Disables the console printing
    bp.info("Just log this!")  # Only written in the log file
    bp.enable_PRINTOUT()  # Enables the console printing
    bp.info("Everything is setted up properly!")  # Printed on the console and written in the log file
    bp.exit()  # Finishes the logging session
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
    
    if _PRINTOUT:
        prefix = time.strftime(_PRINTPREFIXFORMAT + " INFO : ")
        print(prefix + text)
    if _LOGFILE:
        logging.info(text)


def err(error):
    """
    Logs an error out.
    
    #### Log result:
    
    ```log
    [09/04/20 11:14:40] ERROR : error
    ```
    """
    
    if _PRINTOUT:
        prefix = time.strftime(_PRINTPREFIXFORMAT + " ERROR : ")
        print(prefix + error)
    if _LOGFILE:
        logging.error(error)


def warn(warning):
    """
    Logs a warning out.
    
    #### Log result:
    
    ```log
    [09/04/20 11:14:40] WARNING : warning
    ```
    """
    
    if _PRINTOUT:
        prefix = time.strftime(_PRINTPREFIXFORMAT + " WARNING : ")
        print(prefix + warning)
    if _LOGFILE:
        logging.warning(warning)
    
    
def debug(debug_info):
    """
    Logs a debugging information out.
    
    #### Log result:
    
    ```log
    [09/04/20 11:14:40] DEBUG : variable debug
    ```
    """
    
    if _PRINTOUT:
        prefix = time.strftime(_PRINTPREFIXFORMAT + " DEBUG : ")
        print(prefix + debug_info)
    if _LOGFILE:
        logging.debug(debug_info)


# Testing
if __name__ == "__main__":
    init()
    info("information")
    debug("variable debug")
    warn("warning")
    err("error")
    exit()
