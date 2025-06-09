Exercise 8
-----------------

.. admonition:: Exercise
   :class: todo

   **Time:** 30 min

   * Run the job notebook ``numba_gpu.ipynb`` in ``hpc101/session_5``. 
   

Launch Jupyter Notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Login to ARE using  http://are.nci.org.au
    * The user name is your NCI username.
    * The password is your NCI password.

2. Start the Jupyter notebook

    .. image:: ./figs/jupyter.png
       :width: 100%
       :align: center
       :alt: Jupyter Notebook on ARE

3. Launch the Jupyter notebook using

``Walltime (hours)``: 3 hours
``Queue`` : gpuvolta
``Compute Size`` : 1gpu
``Project`` : vp91
``Storage`` : gdata/vp91+scratch/vp91
``Modules`` : python3/3.11.0 cuda/12.8.0
``Python or Conda virtual environment base`` : /g/data/vp91/Training-Venvs/intro-to-numba


Exercise 9
-----------------

.. admonition:: Exercise
   :class: todo

   **Time:** 30 min

  * Run the job ``parallel_add.pbs`` in ``hpc101/session_5``. It runs the program ``parallel_add.py``.