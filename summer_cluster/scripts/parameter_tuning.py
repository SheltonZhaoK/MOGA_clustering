import os
import zipfile as zf
import sys
from reader import *
from preprocesser import *
from clusterer import *
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
      
      report = pd.DataFrame(columns = ['indRate','mutPro', 'cxPro', 'fitness'])
      data = run_umap(run_pca(standardize(data), 2))
      
      indRates = [1]
      mutPros = [0.01, 0.03, 0.05, 0.07, 0.1, 0.2, 0.3, 0.4, 0.5]
      cxPros = [0.5,0.6,0.7,0.8,0.9,1]

      for indRate in indRates:
         for mutPro in mutPros:
            for cxPro in cxPros:
               ga = run_ga(datasets=data, numCenters=6, indPb=indRate, mutPb=mutPro, cxPb=cxPro)
               report.loc[len(report)] = [indRate, mutPro, cxPro, ga.fitness[len(ga.fitness)-1]]
               print(indRate, mutPro, cxPro, '==================================')
      fileName = '../output/parameter_tuning/parameter_tuning_%s.csv' % (className)
      report.to_csv(fileName)
 
if __name__ == '__main__':
   path = '../data/keel_benchmarks2/'
   dirName = path + sys.argv[1] + '/'
   className = sys.argv[1]
   main(dirName,className)  
