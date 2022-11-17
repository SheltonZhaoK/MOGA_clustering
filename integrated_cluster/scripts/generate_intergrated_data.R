library(scrnabench)
names <- c('10X_LLU_A_cellranger2.0', 'ICELL8_SE_A_featureCounts','10X_LLU_A_zumi','C1_FDA_HT_A_kallisto')
datasets <- load_data(path = '/deac/csc/khuriGrp/zhaok220/clustering/data')
dataList <- extract_datasets(c(names))

#without harmony
#set.seed(1)
#dataList = extract_common_genes(dataList)
#dataList = merge_datasets(dataList)
#dataList = filter_data(dataList)
#dataList = annotate_datasets(dataList)
#dataList = run_log(dataList)
#dataList = select_hvg(dataList)
#dataList = scale_data(dataList)
#dataList = run_pca(dataList, numComponents = 10)
#dataList <- run_umap(dataList, reductionType = 'pca', numDimensions = 10)
#dataList <- run_tsne(dataList, reductionType = 'pca', numDimensions = 10)
#dataList <- run_kmeans_clustering(dataList, reductionType = 'pca', 10)
#dataList <- run_kmeans_clustering(dataList, reductionType = 'umap', 10)
#dataList <- run_kmeans_clustering(dataList, reductionType = 'tsne', 10)
#data <- Seurat::Embeddings(dataList[[1]],'umap')
#cell_line <- dataList[[1]]@meta.data[rownames(data),]$CELL_LINE
#data <- cbind(data, cell_line)
#clusters <- dataList[[1]]@meta.data[rownames(data),]$KMEANS_CLUSTER_UMAP
#data <- cbind(data, clusters)
#id <- dataList[[1]]@meta.data[rownames(data),]$ID
#data <- cbind(data, id)
#data <- as.data.frame(data)
#file = '/deac/csc/khuriGrp/zhaok220/data_intergration/data/intergration_without_harmony.csv'
#write.csv(data,file, row.names = TRUE)


#with harmony
set.seed(1)
dataList <- run_harmony_integration_workflow(dataList, method = 'kmeans', numberClusters = 10)
data <- Seurat::Embeddings(dataList[[1]],'umap')
cell_line <- dataList[[1]]@meta.data[rownames(data),]$CELL_LINE
data <- cbind(data, cell_line)
clusters <- dataList[[1]]@meta.data[rownames(data),]$KMEANS_CLUSTER_UMAP
data <- cbind(data, clusters)
id <- dataList[[1]]@meta.data[rownames(data),]$ID
data <- cbind(data, id)
data <- as.data.frame(data)
file = '/deac/csc/khuriGrp/zhaok220/data_intergration/data/intergration_with_harmony.csv'
write.csv(data,file, row.names = TRUE)
