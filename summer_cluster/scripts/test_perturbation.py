import random, copy
import pandas as pd
import numpy as np
from clusterer import *
from validator import *

def copy_list(alist):
   newList = []
   for i in range(0, len(alist)):
      newList.append(alist[i])
   return newList

def main():
   random.seed(1)
   report = []
   silhouettes = [] 
   dataList = [
                [[2,6],[3,4],[3,8],[4,7],[6,2],[6,4],[7,3],[7,4],[8,5],[7,6]],\
               [[7, 4], [6, 4], [7, 3], [6, 2], [2, 6], [3, 4], [7, 6], [3, 8], [4, 7], [8, 5]],\
               [[5,6],[7,4],[7,8],[9,7],[13,2],[13,4],[15,3],[15,4],[17,5],[15,6]],\
               [[2, 6], [3, 4], [3, 8], [4, 7], [6, 2], [6, 4], [7, 3], [7, 4], [8, 5], [7, 6], [4,7]],\
               [[6,2],[4,3],[8,3],[7,4],[2,6],[4,6],[3,7],[4,7],[5,8],[6,7]],\
               [[2, 6,1], [3, 4,1], [3, 8,1], [4, 7,1], [6, 2,1], [6, 4,1], [7, 3,1], [7, 4,1], [8, 5,1], [7, 6,1]],\
             [[-2,6],[-3,4],[-3,8],[-4,7],[-6,2],[-6,4],[-7,3],[-7,4],[-8,5],[-7,6]]
            ]
   for data in dataList:
      datasets = pd.DataFrame(data)
      kObject =  run_kmeans(datasets = datasets, numCenters = 2,  maxiter = 5, random_state = 1)
      kObject.assign_memberships(datasets)
      report.append(kObject.memberships)
      silhouettes.append(silhouette(datasets, kObject.memberships))
   
   data = [[2,6],[3,4],[3,8],[4,7],[6,2],[6,4],[7,3],[7,4],[8,5],[7,6]]
   kObject =  run_kmeans(datasets = datasets, numCenters = 2,  maxiter = 5, random_state = 1)
   centers = kObject.centers
   for i in range (0, len(centers)):
      data[random.randint(0,len(data)-1)] = centers[i]
   data = pd.DataFrame(data) 
   kObject =  run_kmeans(datasets = data, numCenters = 2,  maxiter = 5, random_state = 1)
   kObject.assign_memberships(data)
   report.append(kObject.memberships)
   silhouettes.append(silhouette(data, kObject.memberships)) 
   
   print(report)
   print(silhouettes)

if __name__ == '__main__':
   random.seed(1)
   main()
