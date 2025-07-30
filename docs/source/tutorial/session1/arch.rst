Architecture of an HPC Machine
-----------------------------

.. admonition:: Overview
   :class: Overview

    * **Time:** 15 min

      #. Learn about the architecture of a High-Performance Computing (HPC) machine.
      #. Learn how to find the architecture of a node using ``lstopo`` command.


.. admonition:: Explanation
   :class: attention

   In computer science, ``architecture`` generally refers to the design and structure of a computer system
   — how its components are organized and how they interact. There are different types of architectures :
    
   * Computer Architecture: Refers to the design of a computer's hardware components.
   * System Architecture: Describes how the entire system (hardware + software) is organized.
   * Software Architecture: Refers to the high-level structure of software systems.
   * Network Architecture: Describes how different network components are organized and how they communicate.


Personal Computer (PC) Architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A laptop or desktop computer can be thought of as a single computing unit

.. image:: ./figs/architecture_pc.png
   :width: 600px
   :align: center
   :alt: PC architecture

HPC Architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlike a PC, an HPC machine is composed of multiple interconnected components designed to deliver 
significantly higher computational power. It typically consists of numerous nodes, with each node containing 
multiple CPUs, GPUs, and its own dedicated memory. In essence, an HPC machine functions as a large computing 
cluster.

.. important::

   A cluster is a group of interconnected computers or servers that work together as a single system to 
   perform tasks more efficiently, reliably, or quickly than a single machine could.

.. image:: ./figs/architecture_hpc.png
   :width: 600px
   :align: center
   :alt: HPC architecture

The architecture of an HPC machine typically includes:

* **Head Node**: The primary node that coordinates job scheduling and overall management of the HPC cluster.

* **Login Node**: The node where users log in to submit and manage their jobs, typically providing an interface for interaction with the cluster.

* **Data Transfer Node**: A node optimized for handling data transfers between the HPC cluster and external storage or networks, improving data throughput.

* **Admin Node**: A node dedicated to system administration tasks, such as monitoring system health and managing configurations.

* **File Systems**: The infrastructure that manages data storage and retrieval within the HPC cluster, crucial for efficient access to large datasets.

* **Storage**: The hardware or system responsible for storing data, including high-capacity solutions like Network Attached Storage (NAS) or Storage Area Network (SAN).

* **Compute Node**: The nodes where actual computational tasks are executed, performing the calculations and processing required for applications.

* **Network Switches**: Devices that route data between different nodes in the HPC cluster, ensuring efficient communication and data transfer.



Architecture of a Node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can find architecture of a node using the command ``lstopo`` on Gadi.

.. code-block:: bash
   :linenos:

   lstopo 


If you want to save the output as an image, you can use the ``--of`` option to specify the output format, 
such as PNG.

.. code-block:: bash
   :linenos:

   lstopo --of png topology.png 


.. admonition:: Key Points
   :class: hint
   
   * Each node in an HPC system can have multiple CPUs, GPUs, and independent memory.
   * The architecture of an HPC machine includes various components such as head nodes, login nodes, compute nodes, and storage systems.
   * lstopo is a command-line tool that provides a graphical representation of the hardware topology of a system.
   * It shows the arrangement of CPUs, memory, and other components in a node.