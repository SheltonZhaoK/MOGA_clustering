#!/bin/bash
#SBATCH --job-name="clustering"
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8        
#SBATCH --time=7-00:00:00
#SBATCH --mem=64gb
#SBATCH --output="clustering-%j.o"
#SBATCH --error="clustering-%j.e"
#SBATCH --mail-user=zhaok220@wfu.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --account="khuriGrp"
#SBATCH --partition='medium'
#SBATCH --array=0-29%30
source /deac/csc/khuriGrp/software/zhaok220/bin/activate 
#python3 /deac/csc/khuriGrp/zhaok220/clustering/scripts/test_scrnaseq_mul.py 6  ${SLURM_ARRAY_TASK_ID}
#python3 /deac/csc/khuriGrp/zhaok220/clustering/scripts/test_keel_mul.py ${SLURM_ARRAY_TASK_ID} 
python3 /deac/csc/khuriGrp/zhaok220/clustering/scripts/test_scrnaseq_time.py ${SLURM_ARRAY_TASK_ID} 4 8 
#python3 /deac/csc/khuriGrp/zhaok220/clustering/scripts/test_synthetic.py ${SLURM_ARRAY_TASK_ID}
slurm_mem_report

exit 0

