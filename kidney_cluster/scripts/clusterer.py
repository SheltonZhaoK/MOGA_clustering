import random, time, phenograph, yaml
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import multiprocessing 
from deap import base, creator, tools, algorithms
from scipy.spatial import distance
from sklearn.cluster import KMeans
from scoop import futures
from numba import jit, cuda
from math import dist

import clusteringObject as co
from validator import *

with open('/deac/csc/khuriGrp/zhaok220/clustering_1/scripts/ga_parameters.yaml') as file:
   params = yaml.load(file, Loader=yaml.FullLoader)['MOEA']

def reshape_chromosome(chromosome, numCenter):
   listOfCenters = np.array(chromosome).reshape(numCenter,int(len(chromosome)/numCenter)).tolist()
   return listOfCenters

def compute_total_intracluster_distance(data, listOfCenters):
   intraclusterDistance = 0
   for i in range(0, len(data)):
      distanceList = []
      for j in range(0,len(listOfCenters)):
         distanceList.append(dist(data[i],listOfCenters[j]))
      minDistance = min(distanceList)
      intraclusterDistance += minDistance
   return intraclusterDistance

def compactness(pop):
   listOfCenters = reshape_chromosome(pop, numCenter)
   intraclusterDistance = compute_total_intracluster_distance(data, listOfCenters)
   return intraclusterDistance,

def separation(pop):
   intraclusterDistance = 0
   interclusterDistance = 0
   listOfCenters = reshape_chromosome(pop, numCenter)
   k = len(listOfCenters)
   counts = [0] * k
   for i in range(0, len(data)):
         distanceList = []
         for j in range(0,len(listOfCenters)):
            distanceList.append(dist(data[i],listOfCenters[j]))
         minDistance = min(distanceList)
         intraclusterDistance += minDistance
         center = distanceList.index(minDistance)
         counts[center] += 1
   for i in range(0, k):
      interclusterDistance += counts[i] * dist(listOfCenters[i], dataCenter)
   return interclusterDistance,
   
def two_objectives(pop):
   intraclusterDistance = 0
   interclusterDistance = 0
   listOfCenters = reshape_chromosome(pop, numCenter)
   k = len(listOfCenters)
   counts = [0] * k
   for i in range(0, len(data)):
         distanceList = []
         for j in range(0,len(listOfCenters)):
            distanceList.append(dist(data[i],listOfCenters[j]))
         minDistance = min(distanceList)
         intraclusterDistance += minDistance
         center = distanceList.index(minDistance)
         counts[center] += 1
   for i in range(0, k):
      interclusterDistance += counts[i] * dist(listOfCenters[i], dataCenter)
   return intraclusterDistance, interclusterDistance, 

def compute_entropy(pop):
   entropy = 0
   memberships = assign_memberships(pop)
   total_number = len(memberships)
   df = pd.DataFrame()
   df["label"], df["label2mix"] = memberships, label2mix
   for center in pd.unique(df["label"]):
      cluster_entropy = 0
      data_cluster = df[df["label"] == center]
      memberNum = len(data_cluster)
      count_series = data_cluster["label2mix"].value_counts()
      for i in range(0, len(count_series)):
         probability = count_series.iloc[i]/memberNum
         cluster_entropy += probability * math.log2(probability)
      entropy += -(cluster_entropy) * (memberNum/total_number)
   return entropy

def three_objectives(pop):
   intraclusterDistance, interclusterDistance = two_objectives(pop)
   entropy = compute_entropy(pop)
   return intraclusterDistance, interclusterDistance, entropy,

def assign_memberships(pop):
   memberships = []
   centers = reshape_chromosome(pop, numCenter)
   for i in range(0, len(data)):
         distanceList = []
         for j in range(0,len(centers)):
            distanceList.append(dist(data[i],centers[j]))
         memberships.append(distanceList.index(min(distanceList)))
   return memberships

def setup_mo_ga(objectives, numAttribute, minNum, maxNum, indPb, mutPb, cxPb, numGen, sizePop, crowding, sizeTour):
   if objectives == 1:
      creator.create("Fitness", base.Fitness, weights = (-1.0,))
      creator.create("Individual", list, fitness=creator.Fitness)
      toolbox = base.Toolbox()
      toolbox.register("evaluate", compactness)
   elif objectives == 2:
      creator.create("Fitness", base.Fitness, weights = (-1.0,1.0,))
      creator.create("Individual", list, fitness=creator.Fitness)
      toolbox = base.Toolbox()
      toolbox.register("evaluate", two_objectives) #compactness, separation
      ref_points = tools.uniform_reference_points(2, sizePop) #change
      toolbox.register("NSGAselect", tools.selNSGA3, ref_points=ref_points)
   elif objectives == 3:
      creator.create("Fitness", base.Fitness, weights = (-1.0,1.0,1.0,)) # compactness, separation, entropy
      creator.create("Individual", list, fitness=creator.Fitness)
      toolbox = base.Toolbox()
      toolbox.register("evaluate", three_objectives)
      ref_points = tools.uniform_reference_points(3, sizePop) #change
      toolbox.register("NSGAselect", tools.selNSGA3, ref_points=ref_points)
   
   pool = multiprocessing.Pool()
   toolbox.register("map", pool.map)
   toolbox.register("attr_bool", random.uniform, minNum, maxNum)
   toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, numAttribute * numCenter)
   toolbox.register("population", tools.initRepeat, list, toolbox.individual)
   toolbox.register('mate', tools.cxOnePoint)
   toolbox.register('mutate', tools.mutPolynomialBounded, eta = crowding, low = minNum, up = maxNum, indpb = mutPb)
   toolbox.register("tourSelect", tools.selTournament, tournsize=sizeTour)
   toolbox.register('selBest', tools.selBest)
   return toolbox
 
def run_gaClustering(datasets, numCenters, objectives = None, indPb = params['indPb'], mutPb = params['mutPb'], cxPb = params['cxPb'], numGen = params['numGen'], sizePop = params['sizePop'], crowding = params['crowding']):
   global numCenter
   global data
   global dataCenter
   global label2mix

   if objectives == 1:
      print("-- %d objective --" % (objectives))
   elif objectives == 2:
      dataCenter = datasets.mean().to_list()
      print("-- %d objectives --" % (objectives))
   elif objectives == 3:
      label2mix = datasets.iloc[:,-1].to_list()
      datasets = datasets.drop(columns=datasets.columns[-1:], axis=1)
      dataCenter = datasets.mean().to_list()
      print("-- %d objectives --" % (objectives))
   else:
      sys.exit('Object Objective is N/A')

   numCenter = numCenters
   data = datasets.values.tolist()
   sizeTour = int(0.2 * sizePop)
   numAttribute = len(data[0])
   minNum = min([entry for sub in data for entry in sub])
   maxNum = max([entry for sub in data for entry in sub])
   
   toolbox = setup_mo_ga(objectives, numAttribute, minNum, maxNum, indPb, mutPb, cxPb, numGen, sizePop, crowding, sizeTour)
   '''
   Evolution starts
   '''
   start = time.time()
   print("-- Begin evolution --")
   pop = toolbox.population(n=sizePop)
   fitnesses = toolbox.map(toolbox.evaluate, pop)
   for ind, fit in zip(pop, fitnesses):
      ind.fitness.values = fit
   fits = [ind.fitness.values for ind in pop] 
   
   for gen in range(1, numGen+1):
      print("-- Generation %i --" % gen)
         
      offspring = toolbox.tourSelect(pop, len(pop))
      offspring = list(toolbox.map(toolbox.clone, offspring))   
      for child1, child2 in zip(offspring[::2], offspring[1::2]):
         if random.random() < cxPb:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

      for mutant in offspring:
         if random.random() < indPb:
            toolbox.mutate(mutant)
            del mutant.fitness.values
      
      invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
      fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
      for ind, fit in zip(invalid_ind, fitnesses):
         ind.fitness.values = fit
      
      if objectives > 1 :
         pop[:] = toolbox.NSGAselect(pop + offspring, sizePop)
      else:
         pop[:] = offspring

      #fits = [ind.fitness.values for ind in pop]
   
   print("-- End of (successful) evolution --")
   #best_ind = select_best(pop)
   end = time.time()
   best_ind = toolbox.selBest(pop, 1)[0]
   centers = reshape_chromosome(best_ind, numCenter)
   #print(centers)
   fitness = best_ind.fitness.values
   return co.ClusteringObject(centers, fitness, end-start , [])

def run_kmeans(datasets, numCenters, maxiter = 100):
   start = time.time()
   kmeans = KMeans(n_clusters = numCenters, max_iter = maxiter).fit(datasets)
   end = time.time()
   centers = kmeans.cluster_centers_.tolist()
   intraclusterDistance = compute_total_intracluster_distance(datasets.values.tolist(), centers)
   return co.ClusteringObject(centers, intraclusterDistance, end - start, [])

def run_phenograph(datasets):
   memberships, graph, Q = phenograph.cluster(datasets)
   return memberships
