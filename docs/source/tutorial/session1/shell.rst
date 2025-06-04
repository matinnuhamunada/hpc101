Shell Scripting
-----------------


.. admonition:: Overview
   :class: Overview

    * **Time:** 30 min

    #. Learn about shell scripts and how to create them.
    #. Learn the differences between ``source`` and ``sh`` commands.

A shell script is a file containing a series of commands that can be executed in the terminal.
You can create a shell script to automate the creation of your directories and environment variables.

.. code-block:: bash
   :linenos:

    cd  /scratch/$PROJECT/$USER/hpc101
    ls
    cd session1
    cat env.sh

You can run the shell script using the following command:

.. code-block:: bash
   :linenos:

   sh env.sh

or

.. code-block:: bash
   :linenos:

   source env.sh

or

.. code-block:: bash
   :linenos:

   . env.sh

.. list-table:: Comparison between ``source`` and ``sh``
   :header-rows: 1
   :widths: 25 37 37

   * - Feature
     - ``source`` (or ``.``)
     - ``sh``
   * - Shell Environment
     - Runs script **in the current shell**
     - Runs script **in a new sub-shell**
   * - Persistence
     - Changes (e.g., variables, ``cd``) **persist**
     - Changes **do not persist** after exit
   * - Typical Use
     - Load config files, environment variables, functions
     - Run standalone shell scripts
   * - Syntax
     - ``source script.sh`` or ``. script.sh``
     - ``sh script.sh``
   * - Shebang Ignored?
     - Yes
     - No — uses shebang or defaults to ``sh``
   * - Performance
     - Slightly faster (no new process)
     - Slower (spawns a new shell process)



.. admonition:: Key Points
   :class: hint

   * A shell script is a file containing a series of commands that can be executed in the terminal.
   * You can run the shell script using the ``sh``, ``source``, or ``.`` commands.
