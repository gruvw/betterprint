PrintBetter
===========

Description
-----------

Use PrintBetter to have a nice prefix before printing anything on the
console output. It also creates a nice log file where you can find
anything that you have printed during the program execution. Take a look
at the `GitHub repository`_ to learn a bit more or to see the
documentation.

Default example:
----------------

.. code:: python

   import printbetter as pb

   pb.init()

   pb.info("information")
   pb.debug("variable debug")
   pb.warn("warning")
   pb.err("error")

This module was developed by `@Gruvw`_.

.. _GitHub repository: https://github.com/gruvw/printbetter/
.. _@Gruvw: https://github.com/gruvw
