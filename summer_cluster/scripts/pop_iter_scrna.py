import os, sys

from reader import *
from clusterer import *
from validator import *
from visualizer import *

def main(dirName, dataName):
   fitness = []
   sizePopulations = [100,200,300,400,500,600,700,800] #
   data, cellId = read_scrnaseq_data(dirName+dataName)
   phgMembership = run_phenograph(data)
   numCenters = len(np.unique(phgMembership))
   for sizePop in sizePopulations:
      ga = run_so_gakmeans(datasets = data, numCenters = numCenters, sizePop = sizePop, numGen = 400)
      fitness.append(ga.fitness)
   report = pd.DataFrame(fitness)
   report = report.T
   report.columns = [100,200,300,400,500,600,700,800]
   fileName = "/deac/csc/khuriGrp/zhaok220/clustering_1/output/pop_iter_%s.csv" % (dataName)   
   report.to_csv(fileName)   

if __name__ == '__main__':
   dirName = "/deac/csc/khuriGrp/zhaok220/clustering_1/data/scrna_benchmarks_umap/"
   dataName = "10X_NCI_M_A_cellranger3.1_umap.csv"
   main(dirName,dataName)
