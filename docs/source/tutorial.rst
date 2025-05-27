Tutorial
========

This tutorial provides an introduction to High-Performance Computing (HPC) concepts, tools, and practices. 
It covers topics such as HPC architecture, connecting to remote systems, using schedulers, running parallel 
jobs, and leveraging GPUs. Participants will gain hands-on experience with tools like SSH, Git, and text 
editors, as well as practical exercises on transferring files, setting environment variables, and running 
jobs on an HPC cluster. The tutorial is structured into multiple sessions, each focusing on specific aspects 
of HPC, with real-world use cases and examples.


.. list-table::
   :widths: 15 20 35 25 10 10
   :header-rows: 1

   * - Sessions (2 Hours each)
     - Topic
     - Details
     - Hands-on Component
     - Topic Time
     - Session Time (minutes)
   * - Session 0
     - Preface
     - Introduction to HPC, examples and use cases
     - 
     - 15
     - 120
   * - (Optional / prerequisite)
     - Introduction to UNIX command line
     - Commands required to work on an HPC machine.
     - Unix commands
     - 30
     - 
   * - 
     - Introduction to SSH and SCP
     - Transferring files to and from remote servers.
     - Login and transfer files
     - 30
     - 
   * - 
     - Introduction to text editors
     - Create and enter data into a text file using text editors.
     - VIM and Nano
     - 30
     - 
   * - 
     - Introduction to Git and GitHub
     - Pull a repo from GitHub and commit changes.
     - Pulling repo and local commits
     - 15
     - 
   * - Session 1
     - Use cases of HPC
     - Real-life examples of the use of high-performance computing
     - 
     - 10
     - 120
   * - 
     - Use of HPC for research
     - 
     - 
     - 10
     - 
   * - 
     - Why use a Cluster?
     - Why would I be interested in High Performance Computing (HPC)?
     - 
     - 5
     - 
   * - 
     - What can I expect to learn from this course?
     - 
     - 
     - 5
     - 
   * - 
     - HPC Architecture
     - How does the architecture of an HPC machine look like?
     - 
     - 10
     - 
   * - 
     - Connecting to a remote HPC system
     - How do I log in to a remote HPC system?
     - Using SSH to login to Gadi
     - 20
     - 
   * - 
     - 
     - 
     - Using Gadi terminal to login
     - 10
     - 
   * - 
     - 
     - 
     - SSH keys
     - 20
     - 
   * - 
     - Exploring Remote Resources
     - How does my local computer compare to the remote systems?
     - Explore Gadi Architecture
     - 15
     - 
   * - 
     - 
     - How does the login node compare to the compute nodes?
     - Explore directories
     - 10
     - 
   * - 
     - 
     - Are all compute nodes alike?
     - 
     - 5
     - 
   * - Session 2
     - Use cases of HPC
     - Examples of the use of HPC in various research fields
     - 
     - 10
     - 120
   * - 
     - Scheduler Fundamentals
     - What is a scheduler and why does a cluster need one?
     - Run a batch job on Gadi
     - 20
     - 
   * - 
     - 
     - How do I launch a program on a compute node?
     - Run an interactive job on Gadi
     - 15
     - 
   * - 
     - 
     - How do I capture the output of a program?
     - 
     - 20
     - 
   * - 
     - Environment Variables
     - How are variables set and accessed in the Unix shell?
     - Set environmental variables
     - 10
     - 
   * - 
     - 
     - How can I use variables to change how a program runs?
     - Run Jobs using Environment variables
     - 5
     - 
   * - 
     - Accessing software via Modules
     - How do we load and unload software packages?
     - Load and unload packages in Gadi
     - 40
     - 
   * - Session 3
     - Use cases of HPC
     - Examples of the use of HPC in various research fields
     - 
     - 10
     - 120
   * - 
     - Transferring files
     - How do I transfer files to (and from) the cluster?
     - Transfer files to and from Gadi
     - 20
     - 
   * - 
     - Running a parallel job
     - How do we execute a task in parallel?
     - Install Python packages
     - 20
     - 
   * - 
     - 
     - What are the different levels of parallelism?
     - Launch parallel jobs
     - 50
     - 
   * - 
     - 
     - What benefits arise from parallel execution?
     - 
     - 10
     - 
   * - 
     - 
     - What are the limits of gains from parallel execution?
     - 
     - 10
     - 
   * - Session 4
     - Use cases of HPC
     - Examples of the use of HPC in various research fields
     - 
     - 10
     - 120
   * - 
     - Single node parallelism
     - Overview / Recap of HPC Architecture
     - 
     - 20
     - 
   * - 
     - Introduction to Numba
     - Introduction to ARE
     - 
     - 30
     - 
   * - 
     - 
     - How to parallelise on a single node?
     - Run Jupyter notebooks
     - 60
     - 
   * - Session 5
     - Use cases of HPC
     - Examples of the use of HPC in various research fields
     - 
     - 10
     - 120
   * - 
     - Introduction to GPUs
     - How does GPUs work?
     - Run Jupyter notebooks
     - 110
     - 
   * - 
     - 
     - How to launch GPU kernels using Numba?
     - 
     - 
     - 
   * - Final Assessment
     - 
     - 
     - 
     - 
     - Two weeks



.. toctree::

    tutorial/intro.rst