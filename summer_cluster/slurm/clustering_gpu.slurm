#!/bin/bash
#SBATCH --job-name="clustering"
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=5-00:00:00
#SBATCH --mem=32gb
#SBATCH --output="clustering-%j.o"
#SBATCH --error="clustering-%j.e"
#SBATCH --mail-user=zhaok220@wfu.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --account="khuriGrp"
#SBATCH --partition=gpu

source /deac/csc/khuriGrp/software/zhaok220/bin/activate 
python3 /deac/csc/khuriGrp/zhaok220/clustering/scripts/xxx.py StockPrice
slurm_mem_report

exit 0

