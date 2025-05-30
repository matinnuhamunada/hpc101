Job Submission
-------------------

.. admonition:: Overview
   :class: Overview

    * **Time:** 20 min

    #. Learn how to submit jobs to the job scheduler.
    #. Understand the structure of a job script and its components.
    #. Learn how to check the status of submitted jobs.

In this section, we will learn how to submit jobs to the job scheduler. The job scheduler is responsible for 
managing and executing jobs on the cluster. It allocates resources, schedules jobs based on priority, and 
ensures efficient use of the cluster's computational power. Job submission is the process of sending a job 
to the job scheduler, which then queues the job for execution on the cluster.

Jobs are submitted to the job scheduler using a job script:

.. code-block:: bash
   :linenos:

    #!/bin/bash

    #PBS -N test_job
    #PBS -P vp91
    #PBS -q normal
    #PBS -l ncpus=48
    #PBS -l storage=scratch/vp91
    #PBS -l mem=16gb
    #PBS -l walltime=00:05:00
    #PBS -l wd

    module load python3/3.11.0

    which python3




Let's break down the job script:

    * ``#!/bin/bash``: This is the shebang line that tells the system to use the Bash shell to execute the script.
    * ``#PBS -N test_job``: This line sets the name of the job to `test_job`. This name will be used to identify the job in the queue.
    * ``#PBS -P vp91``: This line specifies the project code (in this case, `vp91`) that the job belongs to.
    * ``#PBS -q normal``: This line specifies the queue to which the job will be submitted. The `normal` queue is typically used for standard jobs.
    * ``#PBS -l ncpus=48``: This line requests 48 CPU cores for the job.
    * ``#PBS -l storage=scratch/vp91``: This line specifies the storage allocation for the job, in this case, it requests scratch storage for the project `vp91`.
    * ``#PBS -l mem=16gb``: This line requests 16 GB of memory for the job.
    * ``#PBS -l walltime=00:05:00``: This line specifies the maximum wall time for the job, which is 5 minutes in this case.
    * ``module load python3/3.11.0``: This line loads the Python module version 3.11.0, which is required for the job.
    * ``which python3``: This line prints the path to the Python executable that will be used in the job.
    * ``#PBS -l wd``: This line sets the working directory for the job to the directory from which the job was submitted.



.. admonition:: Explanation
   :class: attention

        * There are various queues available on Gadi, such as ``normal``, ``express``, and ``gpuvolta``. 
        * Each queue has different resource limits and priorities. 
        * The ``normal`` queue is typically used for standard jobs.
        * Each job should be submitted to a specific queue through a specific project. 
        * The project code is used to track resource usage and billing for the job.
        
        
.. admonition:: Explanation
    :class: attention

        * The number of cores available on Gadi is 48 per node. 
        * When you request ``ncpus=48``, you are requesting all the cores on a single node.
        

To submit the job script, you can use the ``qsub`` command:

.. code-block:: bash
    :linenos:
    
        cd /scratch/$PROJECT/$USER/hpc101/session_2
        cat test_job.pbs
        qsub test_job.pbs
        

.. admonition:: Explanation
    :class: attention

        * This command submits the job script ``test_job.pbs`` to the job scheduler. 
        * The job will be queued and executed when resources become available. 


You can check the status of your job using the ``qstat`` command:


.. code-block:: bash
    :linenos:

        qstat -u $USER




.. admonition:: Explanation
    :class: attention
    
        * This command lists all the jobs submitted by the current user. 
        * You can see the job ID, name, user, state, and other details.



The different states of a job can be:

* ``Q``: Queued - The job is waiting for resources to become available.
* ``R``: Running - The job is currently running on the cluster.       
* ``E``: Exiting - The job is in the process of exiting.
* ``H``: Held - The job is held and will not run until it is released.



.. admonition:: Key Points
    :class: hint
    
        * ``qsub`` is the command used to submit a job script to the job scheduler.
        * ``qstat`` is the command used to check the status of jobs in the queue.
