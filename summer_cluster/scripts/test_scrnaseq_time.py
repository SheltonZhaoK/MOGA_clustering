import os, sys

from reader import *
from clusterer import *
from validator import *
from visualizer import *
from preprocesser import *

def main(dirName,jobID,ntasks,ncpus):
   report = pd.DataFrame(columns = ['Benchmark', 'Instance #',
         'Cluster #','mo-time'])
   #membershipReport = {}
   
   numCenters_list = []
   phgMembership_list = []
   for dataset in os.listdir(dirName):
      dataFile = dirName + dataset
      data, cellId = read_scrnaseq_data(dataFile)
      phgMembership = run_phenograph(data)
      phgMembership_list.append(phgMembership)
      numCenters = len(np.unique(phgMembership))
      print(numCenters)
      numCenters_list.append(numCenters)
   
   numCenters_list = scale(numCenters_list, 3, 10)
   numCenters_list = list(map(int, numCenters_list))
   print(numCenters_list)
   index = 0
   for dataset in os.listdir(dirName):   
   
      dataFile = dirName + dataset
      print(dataFile)
      data, cellId = read_scrnaseq_data(dataFile)
      numCenters = numCenters_list[index]
      
      moga = run_mo_gakmeans(datasets = data, numCenters = numCenters, numGen = 350, sizePop = 600)
      #soga = run_so_gakmeans(datasets = data, numCenters = numCenters, numGen = 350, sizePop = 600)

      report.loc[len(report)] = [dataset, data.shape[0], numCenters,moga.time]
      index += 1

   report.to_csv('/deac/csc/khuriGrp/zhaok220/clustering/output/time_comparison_MO_' + str(ntasks)+ '_'\
+str(ncpus) + '_'+str(jobID)+'.csv')
   print(report)
if __name__ == '__main__':
   dirName = "/deac/csc/khuriGrp/zhaok220/clustering/data/scrna_benchmarks_umap/"
   jobID = sys.argv[1]
   ntasks = sys.argv[2]
   ncpus = sys.argv[3]
   main(dirName,jobID,ntasks,ncpus)
