import os, sys
import zipfile as zf

from reader import *
from preprocesser import *
from clusterer import *
from validator import *

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

def main(dirName):
   report = pd.DataFrame(columns = ['Benchmark','raw', 'pca',\
   'umap', 'pca_umap'])
   
   for className in os.listdir(dirName):
      realNum = True
      if not (className == 'All.zip'):
         f = open(find_file_wExt(dirName + className +'/','txt'),encoding="utf8", errors='ignore',mode='r')
         lines = f.readlines()
         for line in lines:
            if '@attribute' in line:
               if not ('real' in line):
                  if not (' ID ' in line): 
                     realNum = False
                     print('Benchmark %s is invalid.' % (className))
                     break
         
         if realNum:
            dataFile = find_file_wExt(dirName + className +'/','dat')
            if dataFile == dirName + className +'/':
               dataFile = unzip_file(dirName + className +'/',className)
            data = read_keel_data(dataFile)
            print('Benchmark %s is valid.' % (className))
            del data['did']
            
            data_raw = standardize(data)
            data_pca = run_pca(data_raw, 2)
            data_umap = run_umap(data_raw)
            data_pca_umap = run_umap(data_pca)
            numCenters = 5
            
            kmeans_raw = run_kmeans(data_raw, numCenters)
            kmeans_pca = run_kmeans(data_pca, numCenters)
            kmeans_umap = run_kmeans(data_umap, numCenters)
            kmeans_pca_umap = run_kmeans(data_pca_umap, numCenters)  
            
            report.loc[len(report)] = [className, silhouette(data_raw,kmeans_raw.memberships),\
            silhouette(data_pca, kmeans_pca.memberships), silhouette(data_umap, kmeans_umap.memberships),\
            silhouette(data_pca_umap, kmeans_pca_umap.memberships)]
   report.to_csv('/deac/csc/khuriGrp/zhaok220/clustering/output/dataTypes_report_2.csv')  

if __name__ == '__main__':
   dirName = '/deac/csc/khuriGrp/zhaok220/clustering/data/keel_benchmarks1/'
   #dirName = /deac/csc/khuriGrp/zhaok220/clustering/data/keel_benchmarks1/BalanceScale/
   main(dirName)  
