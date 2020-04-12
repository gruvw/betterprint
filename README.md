# PrintBetter

---

## Description

I created this module because I had had enough of writing and rewriting the same piece of code every time I needed to print something in Python 💢.
I wanted two things:

- To be able to keep what I had printed on the console after I having closed it -> log file 📁
- To see the time when the print was executed -> print prefix ⌚️

In addition to all that I added a simple and nice feature which is multiple print "types":

- Information [INFO] -> the basic one, replaces the old `print`
- Debugging [DEBUG] -> when you print something just to see a variable content, Oh yeah you need this!
- Warning [WARNING] -> when you need to show a warning
- Error [ERROR] -> when you need to display that an error occurred, so we do not need to use `raise` which prints a massive and ugly block of red code inside your clean and sweet console

It also had to be fully customizable because I hate it when I am forced to use some part of a module that I do not really like 💯.

Feel free to make a pull request if you have any upgrade idea.

That is it! A new way to print things in python! ✅

## Features

Use PrintBetter to have a nice prefix before printing anything on the console output.
It also creates a clean log file where you can find anything that you have printed during the program execution. 😊

## ⚡️ Quick Start
Installation is really simple:

```bash
pip install printbetter
```

## Usage

You need to initialize the module in order to have the log file set up properly:

```python
import printbetter as pb

pb.init()  # Initializes the log file and the printing format

pb.info("Everything is set up properly!")

pb.exit()  # Finishes the logging file
```

## ✏️ Default example

```python
import printbetter as pb

pb.init()

pb.info("information")
pb.debug("variable debug")
pb.warn("warning")
pb.err("error")

pb.exit()
```

## Imports

This module uses 3 other modules that it imports:

- logging
- time
- os

(no need to install anything, all the 3 modules are in the Standard Python Module Library)

## Documentation

The full documentation 📄 below comes directly from the code's docstring. It makes the documentation readable directly from any compatible IDE or text editors. I recommend using [Visual Studio Code](https://code.visualstudio.com/).

### Initialization `init()`

You should call this function before logging anything in your program.
Initializes the module: creates the log file in the right path and defines the logging format.
If needed all the different parameters are here to set each variable without using the proper function.

#### Definition

```python
def init(printOut=True, logFile=True, logPath="logs/logfile_%d-%m-%y_%H.%M.%S.log",
         logFormat='[%(asctime)s] %(levelname)s : %(message)s', logDateFmt='%d/%m/%y %H:%M:%S',
         printPrefixFormat="[%d/%m/%y %H:%M:%S]"):
```

### Exit `exit()`

You should call this function before the ending of your program.
Terminates the logging module and finishes the log file.

### Information `info(text)`

Logs an information out.

#### Log result

```log
[09/04/20 11:14:40] INFO : information
```

### Debug `debug(debug_info)`

Logs a debugging information out.

#### Log result

```log
[09/04/20 11:14:40] DEBUG : variable debug
```

### Warning `warn(warning)`

Logs a warning out.

#### Log result

```log
[09/04/20 11:14:40] WARNING : warning
```

### Error `err(error)`

Logs an error out.

#### Log result

```log
[09/04/20 11:14:40] ERROR : error
```

### Customize the log path `custom_LOGPATH(path)`

Sets the log file path. It has to be set before the initialization in order to work.
Fully supports the `time.strftime` syntax. You can not use following characters: "\\ / : * ? \" > < |" !
Default: "logs/logfile_%d-%m-%y_%H.%M.%S.log"

#### Example

```python
pb.custom_LOGPATH("logs_files/log_from_%d-%m-%y.log")
pb.init()  # Initialization
pb.info("Everything is set up properly!")
pb.exit()  # Exit
```

### Customize the print prefix `custom_PRINTPREFIXFORMAT(printPrefixFormat)`

Sets the print prefix format for console printing. It should be set before the initialization.
Fully supports the `time.strftime` syntax.
Default: "[%d/%m/%y %H:%M:%S]"

#### Example

```python
pb.custom_PRINTPREFIXFORMAT("%d/%m %M:%S")
pb.init()  # Initialization
pb.info("Everything is set up properly!")
pb.exit()  # Exit
```

### Customize the log format `custom_LOGFORMAT(fmt, datefmt)`

Sets the two arguments (format:fmt and datefmt:datefmt) of the logging.basicConfig function from the logging module. It has to be set before the initialization in order to work.
Fully supports the `time.strftime` syntax. Please see [Logging module documentation](https://docs.python.org/3/library/logging.html) for further details.
Default format: '[%(asctime)s] %(levelname)s : %(message)s'
Default datefmt: '%d/%m/%y %H:%M:%S'

#### Example

```python
pb.custom_LOGFORMAT('%(levelname)s : %(message)s', '%M:%S')
pb.init()  # Initialization
pb.info("Everything is set up properly!")
pb.exit()  # Exit
```

### Disable the log file feature `disable_LOGFILE()`

Disables the creation of the log file and the logging into an existing log file for the next printbetter functions.
You should call this before the initialization.

#### Example

```python
pb.disable_LOGFILE()  # Disables the log file
pb.init()  # Initializes the printing format
pb.info("Everything is set up properly!")  # Formats the text and prints it on the console only
pb.exit()  # Finishes the logging session
```

### Enable the log file feature `enable_LOGFILE()`

Re-enables the creation of the log file and the logging into the log file for next printbetter functions.
You should call this before the logging something in the log file.

#### Example

```python
pb.init()  # Initializes the printing format
pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
pb.disable_LOGFILE()  # Disables the log file
pb.info("Just print this!")  # Only printed on the console
pb.enable_LOGFILE()  # Enables the logging into the log file
pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
pb.exit()  # Finishes the logging session
```

### Disable the print feature `disable_PRINTOUT()`

Disables the printing on the console for next printbetter functions.

#### Example

```python
pb.disable_PRINTOUT()  # Disables the console printing
pb.init()  # Initialization
pb.info("Everything is set up properly!")  # Formats the text and writes it in the log file only
pb.exit()  # Exit
```

### Enable the print feature `enable_PRINTOUT()`

Re-enables the console printing for next printbetter functions.
You should call this before the logging something on the console.

#### Example

```python
pb.init()  # Initialization
pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
pb.disable_PRINTOUT()  # Disables the console printing
pb.info("Just log this!")  # Only written in the log file
pb.enable_PRINTOUT()  # Enables the console printing
pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
pb.exit()  # Finishes the logging session
```

This module was developed by Lucas Jung alias [@Gruvw](https://github.com/gruvw).
Contact me directly on GitHub or via E-Mail at: gruvw.dev@gmail.com
