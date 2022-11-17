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

def main(dirName, jobId):
   report = pd.DataFrame(columns = ['Benchmark', 'Instance #', 'Attribute #',\
         'Cluster #','ga-sw', 'k-sw', 'phg-sw'])
  
   numCenters_list = []
   phgMembership_list = [] 
   
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
            data = run_umap(standardize(data))

            phgMembership = run_phenograph(data)
            phgMembership_list.append(phgMembership)
            numCenters = len(np.unique(phgMembership))
            numCenters_list.append(numCenters)
   
   numCenters_list = scale(numCenters_list, 3, 10)
   numCenters_list = list(map(int, numCenters_list))
   index = 0
   #i = 0
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
            data = run_umap(standardize(data))
            numCenters = numCenters_list[index]
            #numCenters = 6
            ga = run_so_gakmeans(data,numCenters,numGen = 200, sizePop = 200)
            ga.assign_memberships(data)
            kmeans = run_kmeans(data, numCenters, maxiter = 200)
            kmeans.assign_memberships(data)

            silhouette_ga = silhouette(data, ga.memberships)
            silhouette_k  = silhouette(data, kmeans.memberships) 
            silhouette_phg = silhouette(data, phgMembership_list[index])            
            report.loc[len(report)] = [className, data.shape[0],data.shape[1], numCenters,"{:.2f}".format(silhouette_ga), \
         "{:.2f}".format(silhouette_k), "{:.2f}".format(silhouette_phg)]
            index+=1
            #i+=1
            #if i ==1:
               #break
   fileName = '/deac/csc/khuriGrp/zhaok220/clustering/output/keel_report_so_scaled_'+str(jobId)+'.csv'
   report.to_csv(fileName)  

if __name__ == '__main__':
   dirName = '/deac/csc/khuriGrp/zhaok220/clustering/data/keel_benchmarks1/'
   #dirName = /deac/csc/khuriGrp/zhaok220/clustering/data/keel_benchmarks1/BalanceScale/
   jobId = sys.argv[1]
   main(dirName, jobId)  
