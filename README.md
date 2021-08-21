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
```

## ✏️ Default example

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

## Documentation

The full documentation 📄 below comes directly from the code's docstring. It makes the documentation readable directly from any compatible IDE or text editors. I recommend using [Visual Studio Code](https://code.visualstudio.com/).

### Initialization `init()`

You should call this function before logging anything in your program.
Initializes the module: creates the log file in the right path and defines the logging format.
If needed all the different parameters are here to set each variable without using the proper function.

#### Definition

```python
def init(print_out=True, log_file=True, log_path="logs/logfile_%d-%m-%y_%H.%M.%S.log",
         log_format='[%(asctime)s] %(levelname)s : %(message)s', log_date_fmt='%d/%m/%y %H:%M:%S',
         print_prefix_format="[%d/%m/%y %H:%M:%S]"):
```

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

### Disable the log file feature `disable_LOG_FILE()`

Disables the creation of the log file and the logging into an existing log file for the next printbetter functions.

#### Example

```python
pb.disable_LOG_FILE()  # Disables the log file
pb.init()  # Initializes the printing format
pb.info("Everything is set up properly!")  # Formats the text and prints it on the console only
```

### Enable the log file feature `enable_LOG_FILE()`

Re-enables the creation of the log file and the logging into the log file for next printbetter functions.

#### Example

```python
pb.init()  # Initializes the printing format
pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
pb.disable_LOG_FILE()  # Disables the log file
pb.info("Just print this!")  # Only printed on the console
pb.enable_LOG_FILE()  # Enables the logging into the log file
pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
```

### Disable the print feature `disable_PRINT_OUT()`

Disables the printing on the console for next printbetter functions.

#### Example

```python
pb.disable_PRINT_OUT()  # Disables the console printing
pb.init()  # Initialization
pb.info("Everything is set up properly!")  # Formats the text and writes it in the log file only
```

### Enable the print feature `enable_PRINT_OUT()`

Re-enables the console printing for next printbetter functions.

#### Example

```python
pb.init()  # Initialization
pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
pb.disable_PRINT_OUT()  # Disables the console printing
pb.info("Just log this!")  # Only written in the log file
pb.enable_PRINT_OUT()  # Enables the console printing
pb.info("Everything is set up properly!")  # Printed on the console and written in the log file
```

This module was developed by Lucas Jung alias [@Gruvw](https://github.com/gruvw).
Contact me directly on GitHub or via E-Mail at: gruvw.dev@gmail.com
