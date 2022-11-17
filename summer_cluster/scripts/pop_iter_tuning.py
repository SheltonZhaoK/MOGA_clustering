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
      
      fitness = []
      numCenters = 6
      sizePopulations = [20, 40, 60, 80, 100]
      data = run_umap(run_pca(standardize(data), 2))
      for sizePop in sizePopulations:
         ga = run_ga(datasets = data, numCenters = numCenters, sizePop = sizePop, numGen = 150)
         fitness.append(ga.fitness)
      report = pd.DataFrame(fitness)
      report = report.T
      report.columns = [20, 40, 60, 80, 100] 
      fileName = "../output/pop_iter_tuning/manuscript_report_%s.csv" % (className)
      report.to_csv(fileName)
      print('done')
 
if __name__ == '__main__':
   path = '../data/keel_benchmarks2/'
   dirName = path + sys.argv[1] + '/'
   className = sys.argv[1]
   main(dirName,className)  
