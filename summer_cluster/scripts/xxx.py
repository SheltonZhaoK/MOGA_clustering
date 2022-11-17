import os
import zipfile as zf
import sys
from reader import *
from preprocesser import *
from clusterer import *
from validator import *
from visualizer import *
import random
import numpy as np
from deap import base
from deap import creator
from deap import tools
from scipy.spatial import distance
from sklearn.cluster import KMeans
from numba import jit, cuda
import numba
def compute_euclidean_distance(x,y):
    return distance.euclidean(x, y)

def reshape_chromosome(chromosome, numCenter):
    listOfCenters = np.array(chromosome).reshape(numCenter,int(len(chromosome)/numCenter))
    return listOfCenters

def allocate_membership(data,listOfCenters):
    listMembership = []
    totalDistance = 0
    for i in range(0, len(data)):
        distance = []
        for j in range(0,len(listOfCenters)):
            distance.append(compute_euclidean_distance(data[i],listOfCenters[j]))
        minDistance = min(distance)
        listMembership.append(distance.index(minDistance))
        totalDistance += minDistance
    return listMembership, totalDistance

def fitness_function(pop):
    listOfCenters = reshape_chromosome(pop, numCenter)
    listMembership, totalDistance = allocte_membership(data,listOfCenters)
    return totalDistance

def unzip_file(dirName, className):
   zipData = zf.ZipFile(find_file_wExt(dirName,'zip'))
   zipInfos = zipData.infolist()
   for zipInfo in zipInfos:
      zipInfo.filename = className + '.dat'
      zipData.extract(zipInfo,path=dirName)
   dataFile = dirName + className + '.dat'
   return dataFile

def find_file_wExt(dirName, extension):
   fileName = ''
   for fileN in os.listdir(dirName):
      rootExt = os.path.splitext(fileN)
      if rootExt[1] == ('.' + extension):
         fileName = fileN
         break
   return dirName + fileName
 
def find_txt(dirName):
   txt = ''
   for fileName in os.listdir(dirName):
      rootExt = os.path.splitext(fileName)
      if rootExt[1] == '.txt':
         txt = fileName
         break
   return txt

#@numba.jit  
def main(dirName,className):
   realNum = True

   f = open(find_file_wExt(dirName,'txt'),encoding="utf8", errors='ignore',mode='r')
   lines = f.readlines()
   for line in lines:
      if '@attribute' in line:
         if not ('real' in line):
            if not (' ID ' in line): 
               realNum = False
               print('The data containing non real number can not be used')
               break
   
   if realNum:
      dataFile = find_file_wExt(dirName,'dat')
      if dataFile == dirName:
         dataFile = unzip_file(dirName,className)
      data = read_keel_data(dataFile)
      del data['did']
      numCenters = 5
      maxiter = 300
      #data = run_umap(normalize(data,'l2'))
      #data = normalize(data,'l2')
      #data = standardize(data)
      #data = run_umap(run_pca(standardize(data),2))
      data = run_umap(standardize(data))
      data.columns = ['UMAP_1','UMAP_2']
      ga = run_mo_gakmeans(datasets = data, numCenters = numCenters, numGen = 200, sizePop = 100)
      kmeans = run_kmeans(datasets = data, numCenters = numCenters, maxiter = maxiter)
      ga.assign_memberships(data)
      kmeans.assign_memberships(data)
      
      print('\nga')
      print('silhouette:' + str(silhouette(data,ga.memberships)))
      ga.print_report()
      print('kmeans')
      print('silhouette:' + str(silhouette(data,kmeans.memberships)))
      kmeans.print_report()

      plot_data(data, '/deac/csc/khuriGrp/zhaok220/clustering/output/StockPrice.svg')
      plot_data_clustering(data, ga.memberships,'umap','/deac/csc/khuriGrp/zhaok220/clustering/output/StockPrice_clustered.svg')
      
if __name__ == '__main__':
   path = '/deac/csc/khuriGrp/zhaok220/clustering/data/keel_benchmarks2/'
   dirName = path + sys.argv[1] + '/'
   #dirName = /deac/csc/khuriGrp/zhaok220/clustering/data/keel_benchmarks1/BalanceScale/
   className = sys.argv[1]
   main(dirName,className)  
