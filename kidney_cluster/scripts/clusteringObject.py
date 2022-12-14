from math import dist

class ClusteringObject:
   def __init__(self, centers,  fitness, time, convergence):
      self.centers = centers
      self.memberships = []
      self.fitness = fitness
      self.time = time
      self.convergence = convergence

   def print_report(self):
      print('fitness: %s \ntime(second): %f ' % (str(self.intraclusterDistance), self.time))
      print("centers:", self.centers, '\n' )

   def assign_memberships(self, data):
      data = data.values.tolist()
      for i in range(0, len(data)):
         distanceList = []
         for j in range(0,len(self.centers)):
            distanceList.append(dist(data[i],self.centers[j]))
         minDistance = min(distanceList)
         self.memberships.append(distanceList.index(minDistance))
      
