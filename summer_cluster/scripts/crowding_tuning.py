import os
import zipfile as zf
import sys
from reader import *
from preprocesser import *
from clusterer_new import *
from validator import *
import random
import numpy as np
from deap import base
from deap import creator
from deap import tools
from scipy.spatial import distance
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

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

      etas = [0.02,0.04,0.06,0.08]
      data = run_umap(run_pca(standardize(data), 2))
      center = 6
      for eta in etas:
         ga = run_ga(data, center)
         plt.plot(ga.fitness)
         plt.title("crowding = %f" % (eta))
         plt.xlabel("number of iterations")
         plt.ylabel("fitness")
         fileName = "/deac/csc/khuriGrp/zhaok220/clustering/output/crowding_tuning/crowding_convergence_analysis_%s\
/crowding=%f.png" % (className, eta)
         plt.savefig(fileName)

if __name__ == '__main__':
   path = '/deac/csc/khuriGrp/zhaok220/clustering/data/keel_benchmarks2/'
   dirName = path + sys.argv[1] + '/'
   #dirName = /deac/csc/khuriGrp/zhaok220/clustering/data/keel_benchmarks1/BalanceScale/
   className = sys.argv[1]
   main(dirName,className)  
