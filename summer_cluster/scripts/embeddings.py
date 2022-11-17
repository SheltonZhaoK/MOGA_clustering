# embeddings.py
import subprocess
import io
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# Define command and arguments
command ='Rscript'
path2script ='./embeddings2.R'
datasets = ["10X_LLU_A_cellranger2.0","10X_LLU_A_cellranger3.1","10X_LLU_A_umitools","10X_LLU_A_zumi",\
            "10X_LLU_B_cellranger2.0","10X_LLU_B_cellranger3.1","10X_LLU_B_umitools", "10X_LLU_B_zumi",\
            "10X_NCI_A_cellranger2.0", "10X_NCI_A_cellranger3.1", "10X_NCI_A_umitools", "10X_NCI_A_zumi",\
            "10X_NCI_B_cellranger2.0", "10X_NCI_B_cellranger3.1", "10X_NCI_B_umitools", "10X_NCI_B_zumi",\
            "10X_NCI_M_A_cellranger2.0", "10X_NCI_M_A_cellranger3.1", "10X_NCI_M_A_umitools", "10X_NCI_M_A_zumi",\
            "10X_NCI_M_A_umitools", "10X_NCI_M_A_zumi", "10X_NCI_M_B_cellranger2.0", "10X_NCI_M_B_cellranger3.1",\
            "10X_NCI_M_B_umitools", "10X_NCI_M_B_zumi", "C1_FDA_HT_A_featureCounts", "C1_FDA_HT_A_kallisto",\
            "C1_FDA_HT_A_rsem", "C1_FDA_HT_B_featureCounts", "C1_FDA_HT_B_kallisto", "C1_FDA_HT_B_rsem",\
            "C1_LLU_A_featureCounts", "C1_LLU_A_kallisto", "C1_LLU_A_rsem", "C1_LLU_B_featureCounts",\
            "C1_LLU_B_kallisto", "C1_LLU_B_rsem", "ICELL8_PE_A_featureCounts", "ICELL8_PE_A_kallisto",\
            "ICELL8_PE_A_rsem", "ICELL8_PE_B_featureCounts", "ICELL8_PE_B_kallisto", "ICELL8_PE_B_rsem",\
            "ICELL8_SE_A_featureCounts", "ICELL8_SE_A_kallisto", "ICELL8_SE_A_rsem", "ICELL8_SE_B_featureCounts",\
            "ICELL8_SE_B_kallisto", "ICELL8_SE_B_rsem"]

# Build subprocess command
for dataset in datasets:
   cmd = [command, path2script, dataset]

    # check_output will run the command and store to df
   data = subprocess.check_output(cmd, universal_newlines=True)
   embeddings = pd.read_csv(io.StringIO(data), sep='\s+', lineterminator='\n', skiprows=4, skipfooter = 2,  header=None, engine='python')
   print(embeddings)

