#!/bin/bash
#SBATCH --job-name="clustering"
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32          # Number of tasks (MPI processes)
#SBATCH --cpus-per-task=1          # Number of threads per task (OMP threads)
#SBATCH --time=7-00:00:00
#SBATCH --mem=32gb
#SBATCH --output="clustering-%j.o"
#SBATCH --error="clustering-%j.e"
#SBATCH --mail-user=zhaok220@wfu.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --account="khuriGrp"
#SBATCH --partition=medium

source /deac/csc/khuriGrp/software/zhaok220/bin/activate 

python3 /deac/csc/khuriGrp/zhaok220/kidney_cluster/scripts/test_kidney.py

slurm_mem_report

exit 0

