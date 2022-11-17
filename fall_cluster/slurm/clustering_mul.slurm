#!/bin/bash
#SBATCH --job-name="clustering"
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --cpus-per-task=1      
#SBATCH --time=7-00:00:00
#SBATCH --mem=12gb
#SBATCH --output="clustering-%A_%a.o"
#SBATCH --error="clustering-%A_%a.e"
#SBATCH --mail-user=zhaok220@wfu.edu
#SBATCH --mail-type=END,FAIL,ARRAY_TASKS
#SBATCH --account="khuriGrp"
#SBATCH --partition='medium'
#SBATCH --array=0-29

source /deac/csc/khuriGrp/software/zhaok220/bin/activate 

python3 /deac/csc/khuriGrp/zhaok220/clustering_2/scripts/test_synthetic_time.py ${SLURM_ARRAY_TASK_ID} 5 32 1

slurm_mem_report -g

exit 0

