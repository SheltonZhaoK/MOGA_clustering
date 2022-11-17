import os, sys

from reader import *
from clusterer import *
from validator import *
from visualizer import *
from preprocesser import *

def main():
   
#   report = pd.DataFrame(columns = ['Benchmark', 'k-sw_0','k-sw_1','k-sw_2','k-sw_3','k-sw_4','k-sw_5','k-sw_6'])
   #membershipReport = {}
   
   result = []
   benchmarks = []
   for i in range(0,7):
      dirName = "/deac/csc/khuriGrp/zhaok220/clustering/data/metamorphic_test/"
      dirName = dirName + str(i) + '/'
   
      sumList = [0]*48

      for j in range(0,30):
         print(i,j)
         silhouettes = []
         for dataset in os.listdir(dirName):
            if len(benchmarks) != 48:
               benchmarks.append(dataset)
            dataFile = dirName + dataset
            data, cellId = read_scrnaseq_data(dataFile)
            numCenters = 7
            
            #ga = run_mo_gakmeans(datasets = data, numCenters = numCenters, numGen = 350, sizePop = 600)
            #ga.assign_memberships(data)

            #kmeans = run_kmeans(data, numCenters,maxiter = 350)
            #kmeans.assign_memberships(data)
            
            memberships = run_phenograph(data)
            #silhouette_ga = silhouette(data, ga.memberships)
            silhouette_phg  = silhouette(data, memberships) 
            
            silhouettes.append(silhouette_phg)
             
         sumList = [sumList[i]+silhouettes[i] for i in range(0,len(silhouettes))]
      
      averageList = []
      for i in range(0,len(sumList)):
         averageList.append(sumList[i]/30)
      
      result.append(averageList)
      print(result) 
   result = pd.DataFrame(result).T
   result.columns = ['MR0','MR1','MR2','MR3','MR4','MR5','MR6']
   #result.columns = ['MR0','MR1']
   result.index = benchmarks
   result.to_csv('/deac/csc/khuriGrp/zhaok220/clustering/output/metamorphic_test_phenograph.csv')
   print(result)
   
if __name__ == '__main__':
   main()
