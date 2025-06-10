Linux File Management
----------------------------------

.. admonition:: Overview
   :class: Overview

    * **Time:** 10 min

    #. Learn the file oragnisation in a Linux OS.
    #. Understand the difference between Unix and Linux.



.. admonition:: Explanation
   :class: attention

    Difference between Unix and Linux:

    .. list-table:: Unix vs Linux Comparison
       :widths: 20 30 30
       :header-rows: 1
    
       * - Feature
         - Unix
         - Linux
       * - Proprietary or Free?
         - Proprietary (mostly)
         - Free and open source
       * - Developed When?
         - 1970s
         - 1991
       * - Developed By
         - AT&T Bell Labs
         - Linus Torvalds + community
       * - Variants
         - AIX, HP-UX, Solaris, etc.
         - Ubuntu, Fedora, Debian, etc.
       * - Certification
         - Unix-certified by The Open Group
         - Not Unix-certified
    


Linux File System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    /
    ├── bin
    ├── boot
    ├── dev
    ├── etc
    ├── home
    │   ├── alice
    │   └── bob
    ├── lib
    ├── media
    ├── mnt
    ├── opt
    ├── proc
    ├── root
    ├── run
    ├── sbin
    ├── tmp
    ├── usr
    │   ├── bin
    │   ├── lib
    │   └── share
    └── var
        └── log




The Linux filesystem is organized as a hierarchical directory tree. Below is a breakdown of the top-level directories and their purposes according to the Filesystem Hierarchy Standard (FHS).

Root Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``/``
    The root of the filesystem. All other directories stem from here.

System and Boot Directories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``/bin``
    Essential user binaries needed for basic system functionality, such as ``ls``, ``cp``, and ``mv``.

``/sbin``
    Essential system binaries, typically used for system administration, such as ``fsck`` and ``reboot``.

``/boot``
    Contains files needed to boot the system, including the Linux kernel and bootloader configurations.

``/lib`` and ``/lib64``
    Shared libraries required by binaries in ``/bin`` and ``/sbin``. ``/lib64`` holds 64-bit libraries.

User and Software Directories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``/usr``
    Secondary hierarchy for read-only user data and installed software. Contains:
    
    - ``/usr/bin``: Non-essential user binaries.
    - ``/usr/lib``: Libraries for binaries in ``/usr/bin``.
    - ``/usr/share``: Architecture-independent shared data.

``/opt``
    Optional software packages from third-party vendors.

``/home``
    Home directories for all users (e.g., ``/home/alice``, ``/home/bob``).

``/root``
    Home directory of the root (superuser).

Configuration and Temporary Directories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``/etc``
    Host-specific configuration files.

``/tmp``
    Temporary files used by applications, typically cleared on reboot.

``/var``
    Variable data files, such as logs, mail, and spool directories.

Devices and Mount Points
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``/dev``
    Contains device files (e.g., ``/dev/sda``, ``/dev/null``), which represent hardware devices.

``/proc``
    Virtual filesystem providing process and kernel information as files (e.g., ``/proc/cpuinfo``).

``/sys``
    Virtual filesystem for exposing information about hardware devices and associated kernel modules.

``/run``
    Stores volatile runtime data like PID files and socket information.

``/mnt``
    Used for temporarily mounting filesystems, often by system administrators.

``/media``
    Mount point for removable media such as USB drives and CD-ROMs.


Extra HPC directories:

.. list-table:: HPC Directory Explanations
   :widths: 15 85
   :header-rows: 1

   * - Directory
     - Explanation
   * - ``apps/``
     - Pre-installed or centrally maintained **software applications** available to all users (e.g. compilers, MPI, MATLAB, etc.). Often used with **modules** like ``module load``.
   * - ``g/``
     - Likely a **group-shared storage area**. Often used in universities or research orgs for shared group project files.
   * - ``scratch/``
     - High-performance **temporary workspace** for large files or experiments. Usually purged periodically.



.. admonition:: Key Points
   :class: hint

    #. Linux follows a hierarchical directory structure, starting from the root directory `/`.
    #. Key directories include `/bin`, `/sbin`, `/usr`, `/etc`, `/home`, and `/var`.
    #. Key HPC directories include `apps/`, `g/`,  and `scratch/`.