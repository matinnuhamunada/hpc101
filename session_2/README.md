Using modules in server:

```bash
module list

# choosing python
which python
module load

# choosing modules
module avail gromac*

# unloading modules
module unload python*

# or
module purge
```

# Using Job Schedulers

```mermaid
ssh to login node
submitting job from the login node to the compute node
```

```bash
cd /scratch/he61/$USER
cd hpc101/session_2/

# there is a pbs script
```