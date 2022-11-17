import sys
from reader import *
from clusterer import *
from validator import *
from preprocesser import *
from reader import *
def main(dirName,fileName,labelName,jobId,nodes, tasks, cpus):
   result = pd.DataFrame(columns = ['instance #','labels #','moea-time','soea-time','moea-sil','moea-ARI','moea-NMI','soea-sil','soea-ARI',\
'soea-NMI','kmeans-sil','kmeasn-ARI','kmeans-NMI','phe-sil','phe-ARI','phe-NMI','seurat_sil','seurat-ARI','seurat-NMI','phe-clusters','seurat-clusters'])
   for i in range (1, 11): #11
      for j in range (1,7): #7
         data, cellId = read_scrnaseq_data(dirName + str(i) + 'k/' + fileName + str(j) + '.csv')   
         labels = pd.read_csv(dirName + str(i) + 'k/' + labelName + str(j) + '.txt', sep = '\t',engine='python')
         seurat_cluster = labels['seurat_cluster'].tolist()
         
         label = labels['labels'].tolist()
         numClusters = len(set(label))
         
         moea = run_mo_gakmeans(data,numClusters,numGen = 350, sizePop = 600)
         moea.assign_memberships(data)
        
         soea = run_so_gakmeans(data,numClusters,numGen = 350, sizePop = 600)
         soea.assign_memberships(data)
         
         pheMemberships = run_phenograph(data)
         
         kmeans = run_kmeans(data, numClusters, 350)
         kmeans.assign_memberships(data)
       
         sil = [silhouette(data, moea.memberships), silhouette(data, soea.memberships), silhouette(data, kmeans.memberships), silhouette(data, pheMemberships), silhouette(data, seurat_cluster)]
         NMI = [nmi(label, moea.memberships), nmi(label, soea.memberships), nmi(label, kmeans.memberships), nmi(label, pheMemberships), nmi(label, seurat_cluster)]
         ARI = [ari(label, moea.memberships), ari(label, soea.memberships), ari(label, kmeans.memberships), ari(label, pheMemberships), ari(label, seurat_cluster)]
        
         tempt = [len(data), numClusters, "{:.3f}".format(moea.time), "{:.3f}".format(soea.time)] 
         for j in range (0, 5):
            tempt.extend(["{:.3f}".format(sil[j]), "{:.3f}".format(ARI[j]), "{:.3f}".format(NMI[j])])
         tempt.extend([len(set(pheMemberships)), len(set(seurat_cluster))])
         result.loc[len(result)] = tempt
     #    print(tempt)
    #     print(result)
      #labels['MOEA'] = moea.memberships
      #labels['SOEA'] = soea.memberships
      #labels['PhenoGraph'] = pheMemberships
      
      #name = '/deac/csc/khuriGrp/zhaok220/clustering/output/synthetic_clusters_label_'+str(i)+'.csv'
      #labels.to_csv(name)
   name = '../output/time_analysis_{}_{}_{}_{}.csv'.format(jobId,nodes,tasks,cpus)
   #print('final')
   #print(result)
   result.to_csv(name) 
       
if __name__ == '__main__':
   dirName = '../data/synthetic_data/data_'
   fileName = 'synthetic_embeddings_'
   labelName = 'labels_'
   jobId = sys.argv[1]
   nodes = sys.argv[2]
   tasks = sys.argv[3]
   cpus  = sys.argv[4] 
   main(dirName, fileName, labelName, jobId, nodes, tasks, cpus)
   
