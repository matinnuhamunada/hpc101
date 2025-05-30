Common CPU Terminology 
-----------------------------------


.. admonition:: Overview
   :class: Overview

    * **Time:** 10 min

    #. Understand common CPU terminologies.
    #. Learn about CPU, cores, and CPU die.

    
This section introduces some common terminologies with respect to CPU.



CPU (Central Processing Unit)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The **main processor** of a computer.
* Responsible for executing instructions (code).
* Can contain **multiple cores** inside a single chip or package.
* Often referred to as a **processor**.

**Example:**  
A computer might have **1 CPU** with **8 cores**.

Core
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* A **processing unit** inside a CPU.
* Each core can independently execute tasks.
* Modern CPUs typically have **multiple cores** to allow parallel processing (multitasking or multi-threaded applications).

**Example:**  
An Intel Core i7 CPU might have **6 cores**, allowing it to run 6 tasks simultaneously.

CPU Die
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The **physical piece of silicon** that contains the circuitry of one or more cores.
* Dies are manufactured on silicon wafers and later packaged into CPUs.
* A single die can hold multiple cores, caches, and other components.
* Some CPUs (like AMD’s multi-chip modules) may contain **multiple dies** inside one package.

Analogy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Think of it like this:

- **CPU** = An office building  
- **Cores** = Workers inside the building  
- **CPU Die** = The physical floor plan that holds the workers (and offices)


NUMA (Non-Uniform Memory Access)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**NUMA** is a memory architecture used in **multi-CPU (multi-socket)** systems to improve performance.

* Each CPU has its own **local memory**.
* Access to local memory is **faster** than access to memory attached to another CPU (remote memory).


CPU (Socket)
~~~~~~~~~~~~

* In NUMA systems, multiple CPU sockets exist on the motherboard.
* Each CPU/socket typically corresponds to one **NUMA node** with its own local memory.


.. image:: ./figs/gpu-node.png
   :width: 600px
   :align: center
   :alt: GPU Node Architecture

.. admonition:: Key Points
   :class: hint
    * A CPU is the main processor of a computer, often with multiple cores.
    * A core is a processing unit within a CPU that can execute tasks independently.
    * A CPU die is the physical silicon piece containing the cores and circuitry.
    * NUMA is a memory architecture that allows each CPU to have its own local memory, improving performance in multi-CPU systems.

