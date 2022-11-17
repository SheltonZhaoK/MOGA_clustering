import os, sys

from reader import *
from clusterer import *
from validator import *
from visualizer import *
from preprocesser import *

def main(dirName,mr,jobId):
   report = pd.DataFrame(columns = ['Benchmark', 'Instance #', 'Attribute #',\
         'Cluster #','ga-sw', 'k-sw', 'phg-sw'])

   numCenters_list = []
   phgMembership_list = []
   for dataset in os.listdir(dirName):
      dataFile = dirName + dataset
      data, cellId = read_scrnaseq_data(dataFile)
      phgMembership = run_phenograph(data)
      phgMembership_list.append(phgMembership)
      numCenters = len(np.unique(phgMembership))
      numCenters_list.append(numCenters)
   
   numCenters_list = scale(numCenters_list, 3, 10)
   numCenters_list = list(map(int, numCenters_list))
   
   index = 0
   for dataset in os.listdir(dirName):   
      dataFile = dirName + dataset
      print(dataFile)
      data, cellId = read_scrnaseq_data(dataFile)
      numCenters = numCenters_list[index]
      
      ga = run_so_gakmeans(datasets = data, numCenters = numCenters, numGen = 350, sizePop = 600)
      ga.assign_memberships(data)
      
      kmeans = run_kmeans(data, numCenters,maxiter = 350)
      kmeans.assign_memberships(data)
      
      silhouette_ga = silhouette(data, ga.memberships)
      silhouette_k  = silhouette(data, kmeans.memberships) 
      silhouette_phg = silhouette(data, phgMembership_list[index])
      
      report.loc[len(report)] = [dataset, data.shape[0],data.shape[1], numCenters,"{:.2f}".format(silhouette_ga), \
         "{:.2f}".format(silhouette_k), "{:.2f}".format(silhouette_phg)]

      index += 1

   fileName = '../output/mr_scrna_so_'+mr+'_'+str(jobId)+'.csv'
   report.to_csv(fileName)
   
   '''
   df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in membershipReport.items() ]))
   df.to_csv('/deac/csc/khuriGrp/zhaok220/clustering/output/phgMembership.csv')
   '''

if __name__ == '__main__':
   mr = sys.argv[1]
   dirName = '.../data/metamorphic_test/'+mr+'/'
   jobId = sys.argv[2]
   main(dirName,mr,jobId)
