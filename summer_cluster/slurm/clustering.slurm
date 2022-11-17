#!/bin/bash
#SBATCH --job-name="clustering"
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=30           # Number of tasks (MPI processes)
#SBATCH --cpus-per-task=1          # Number of threads per task (OMP threads)
#SBATCH --time=7-00:00:00
#SBATCH --mem=64gb
#SBATCH --output="clustering-%j.o"
#SBATCH --error="clustering-%j.e"
#SBATCH --mail-user=zhaok220@wfu.edu
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --account="khuriGrp"
#SBATCH --partition=medium

source /deac/csc/khuriGrp/software/zhaok220/bin/activate 

#python3 /deac/csc/khuriGrp/zhaok220/clustering/scripts/pop_iter_scrna.py 10X_NCI_M_A_cellranger3.1_tsne.csv
#python3 /deac/csc/khuriGrp/zhaok220/clustering/scripts/test_keel.py
#python3 /deac/csc/khuriGrp/zhaok220/clustering/scripts/test_scrnaseq.py
#python3 /deac/csc/khuriGrp/zhaok220/clustering/scripts/pop_iter_scrna.py C1_LLU_A_rsem_umap.csv
#python3 /deac/csc/khuriGrp/zhaok220/clustering/scripts/pop_iter_scrna.py 10X_NCI_M_A_cellranger3.1_umap.csv
#python3 /deac/csc/khuriGrp/zhaok220/clustering/scripts/test_metamorphic.py
python3 /deac/csc/khuriGrp/zhaok220/clustering_1/scripts/pop_iter_scrna.py
#python3 /deac/csc/khuriGrp/zhaok220/clustering/scripts/test_scrnaseq_time.py
slurm_mem_report

exit 0

