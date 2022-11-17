rm(list = ls())
gc()

library(scrnabench)
library(Matrix)
names = commandArgs(trailingOnly = TRUE)

datasets = load_data(path = '/deac/csc/khuriGrp/zhaok220/clustering/data')
dataList = extract_datasets(c(names))
dataList = filter_data(dataList)
dataList = annotate_datasets(dataList)
dataList = run_log(dataList)
dataList = select_hvg(dataList)
dataList = scale_data(dataList)
dataList = run_pca(dataList,numComponents=10)
dataList = run_umap(dataList,numDimensions=10)


data = Seurat::Embeddings(dataList[[1]],'umap')
print(data)

