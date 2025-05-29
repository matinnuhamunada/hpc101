Interactive Jobs 
--------------------

.. admonition:: Overview
   :class: Overview

    * **Time:** 20 min

    #. Learn how to run interactive jobs on Gadi.
    #. Understand the benefits of interactive jobs compared to batch jobs.

Interactive jobs allow you to run commands directly on the compute nodes, providing a more interactive experience
compared to batch jobs. This is particularly useful for tasks that require user input or real-time feedback.
To start an interactive job on Gadi, you can use the `qsub` command with the `-I` option. This will allocate 
resources for an interactive session.

.. code-block:: bash
   :linenos:

    qsub -I -q normal  -P vp91 -l walltime=00:10:00,ncpus=48,mem=10GB

    module load python3/3.11.0
    which python3


In this command:
    * ``-I``: This option indicates that you want to start an interactive job.
    * ``-q normal``: Specifies the queue to use for the job, in this case, the `normal` queue.
    * ``-P vp91``: Specifies the project code for the job.
    * ``-l walltime=00:10:00``: Sets the maximum wall time for the job to 10 minutes.
    * ``-l ncpus=48``: Requests 48 CPU cores for the job.
    * ``-l mem=10GB``: Requests 10 GB of memory for the job.



After submitting the command, you will be allocated resources and dropped into a shell on one of the compute 
nodes. You can then run commands directly on the node, such as checking the Python version or running scripts.
To exit the interactive session, simply type `exit` or press `Ctrl+D`. This will terminate the interactive 
job and return you to your original shell.



.. admonition:: Key Points
   :class: hint

   * `qsub -I`: This command is used to submit an interactive job. 