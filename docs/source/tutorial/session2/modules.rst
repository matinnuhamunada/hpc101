Modules
----------

.. admonition:: Overview
   :class: Overview

    * **Time:** 15 min

    #. Learn how to use modules to manage software on HPC systems.
    #. Understand how to load and unload modules.

.. note::
 1.  ``python3/3.11.0``
 2.  ``papi/7.0.1``
 3.  ``openmpi/4.0.1``
 4.  ``cuda/12.3.2``
 5.  ``gcc/14.2.0``

Finding Modules
^^^^^^^^^^^^^^^^^^^^^^^

Modules are how we manage software in most HPC machines. We can see all the available modules using the command

.. code-block:: console
    :linenos:
    
    module avail

This command lists all the available modules on the system that starts with the letter "p".

.. code-block:: console
    :linenos:   

    module avail p*



Loading Modules
^^^^^^^^^^^^^^^^^^^^^^^

If we want to load a module ``python3/3.11.0`` we can use the command

.. code-block:: console
    :linenos:

    module load python3/3.11.0


We can also load multiple modules at once.  


.. code-block:: console
    :linenos:
    
    module load papi/7.0.1 openmpi/4.0.1


Unloading Modules
^^^^^^^^^^^^^^^^^^^^^^^

If we want to unload the module use the command

.. code-block:: console
    :linenos:
    
    module unload python3/3.11.0

We can unload all the modules using the command

.. code-block:: console
    :linenos:
    
    module purge


.. admonition:: Key Points
   :class: hint

    * ``module avail``: This command lists all the available modules on the system.
    * ``module load <module_name>``: This command loads a specific module, making its software available for use.
    * ``module unload <module_name>``: This command unloads a specific module, removing its software from the environment.