import os, sys

from reader import *
from clusterer import *
from validator import *
from visualizer import *

def main(path, filename):
   report = pd.DataFrame(columns = ['Benchmark', 'Instance #', 'Attribute #',\
         'Cluster #','ga-sw', 'ga-dbi','k-sw','k-dbi', 'phg-sw','phg-dbi'])
   membershipReport = {}

   dataFile = path+filename
   print(dataFile)
   data, cellId = read_scrnaseq_data(dataFile)
   
   #membershipReport[dataset] = np.array(cellId)
   phgMembership = run_phenograph(data)
   #numCenters = len(np.unique(phgMembership))
   #numCenters = int(len(np.unique(phgMembership)) * 0.5 )
   numCenters = 2
   ga = run_mo_gakmeans(datasets = data, numCenters = numCenters, numGen = 350, sizePop = 600 )
   ga.assign_memberships(data)
   #membershipReport[dataset+"_memberships"] = np.array(ga.memberships)
   
   kmeans = run_kmeans(data, numCenters,maxiter=350)
   kmeans.assign_memberships(data)
   
   silhouette_ga = silhouette(data, ga.memberships)
   silhouette_k  = silhouette(data, kmeans.memberships) 
   silhouette_phg = silhouette(data, phgMembership)
   
   dbi_ga = dbi(data, ga.memberships)
   dbi_k = dbi(data, kmeans.memberships)
   dbi_phg = dbi(data, phgMembership)
   
   report.loc[len(report)] = [filename, data.shape[0],data.shape[1], numCenters,"{:.2f}".format(silhouette_ga),"{:.2f}".format(dbi_ga), \
      "{:.2f}".format(silhouette_k),"{:.2f}".format(dbi_k), "{:.2f}".format(silhouette_phg),"{:.2f}".format(dbi_phg)]
   print(report)
   
   plot_data(data, '/deac/csc/khuriGrp/zhaok220/clustering/output/'+filename+'.svg')
   plot_data_clustering(data,ga.memberships,'umap', '/deac/csc/khuriGrp/zhaok220/clustering/output/' + filename + '_clustered'+'.svg')
   
if __name__ == '__main__':
   path = "/deac/csc/khuriGrp/zhaok220/clustering/data/scrna_benchmarks_umap/"
   filename =  sys.argv[1]
   main(path, filename)
