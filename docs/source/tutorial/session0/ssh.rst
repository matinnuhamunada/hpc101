Secures Shell
----------------------------------

.. admonition:: Overview
   :class: Overview

    * **Time:** 30 min

    #. Learn how to use SSH for secure remote access.
    #. Learn how to copy files using SCP.
    #. Understand the basics of SSH keys for authentication.


SSH and SCP
^^^^^^^^^^^^
SSH (Secure Shell) is a protocol used to securely connect to remote systems over a network. SCP (Secure Copy Protocol) is used to securely transfer files between systems.
Here are some basic commands to get started with SSH and SCP:


.. list-table:: Basic SSH and SCP Commands
   :widths: 30 70
   :header-rows: 1

   * - Command
     - Description
   * - ``ssh user@hostname``
     - Connect to a remote system using SSH.
   * - ``scp /path/to/source_file user@hostname:/path/to/destination_file``
     - Copy a file to a remote system using SCP.

 
SSH Keys for Passwordless Login
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SSH keys provide a secure way to log into a remote system without using a password. Here's how to create and transfer SSH keys for passwordless login:

.. code-block:: bash

    # Step 1: Generate an SSH key pair
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

    # Step 2: Copy the public key to the remote system
    ssh-copy-id user@hostname

    # Step 3: Test the passwordless login
    ssh user@hostname

.. important::

    * Ensure that the SSH server on the remote system is configured to accept key-based authentication.
    * The public key is stored in the `~/.ssh/authorized_keys` file on the remote system.
    * The private key remains on your local machine and should be kept secure.
    * If you have multiple SSH keys, you can specify which key to use with the `-i` option:
    ssh -i /path/to/private_key user@hostname



.. admonition:: Key Points
   :class: hint

    * SSH provides a secure way to access remote systems.
    * SCP allows for secure file transfers between systems.
    * SSH keys enhance security and convenience by enabling passwordless login.
