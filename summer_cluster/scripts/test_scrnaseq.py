import os, sys

from reader import *
from clusterer import *
from validator import *
from visualizer import *
from preprocesser import *

def main(dirName):
   report = pd.DataFrame(columns = ['Benchmark', 'Instance #', 'Attribute #',\
         'Cluster #','ga-sw', 'k-sw', 'phg-sw'])
   #membershipReport = {}
   
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
   #i = 0
   index = 0
   singletons = []
   for dataset in os.listdir(dirName):   
      dataFile = dirName + dataset
      print(dataFile)
      data, cellId = read_scrnaseq_data(dataFile)
      numCenters = numCenters_list[index]
      
      ga = run_so_gakmeans(datasets = data, numCenters = numCenters, numGen = 350, sizePop = 600)
      ga.assign_memberships(data)
      #membershipReport[dataset+"_memberships"] = np.array(ga.memberships)
      
      kmeans = run_kmeans(data, numCenters,maxiter = 350)
      kmeans.assign_memberships(data)
      
      silhouette_ga = silhouette(data, ga.memberships)
      silhouette_k  = silhouette(data, kmeans.memberships) 
      silhouette_phg = silhouette(data, phgMembership_list[index])
      
      report.loc[len(report)] = [dataset, data.shape[0],data.shape[1], numCenters,"{:.2f}".format(silhouette_ga), \
         "{:.2f}".format(silhouette_k), "{:.2f}".format(silhouette_phg)]
      #plot_data_clustering(data,ga.memberships,numCenters,'tsne','/deac/csc/khuriGrp/zhaok220/clustering/output/scrnaseq_clustering_tsne/'+dataset+'.png')
      #i += 1
      #if i == 1:
         #break
      index += 1
      
      count = 0
      clusters = set(ga.memberships)
      for cluster in clusters:
         if ga.memberships.count(cluster) == 1:
            count += 1
      singletons.append(count)
   report.to_csv('/deac/csc/khuriGrp/zhaok220/clustering/output/test.csv')
   singletons = pd.DataFrame(singletons)
   singletons.columns = ['number of singletons']
   singletons.index = report['Benchmark'].tolist()
   singletons.to_csv('/deac/csc/khuriGrp/zhaok220/clustering/output/singletons_so.csv')
   '''
   df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in membershipReport.items() ]))
   df.to_csv('/deac/csc/khuriGrp/zhaok220/clustering/output/phgMembership.csv')
   '''

if __name__ == '__main__':
   dirName = "/deac/csc/khuriGrp/zhaok220/clustering/data/scrna_benchmarks_umap/"
   main(dirName)
