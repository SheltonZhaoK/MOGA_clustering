2022-07-25 16:10:35.674064: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-07-25 16:10:35.674096: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_synthetic.py", line 53, in <module>
    main(dirName, fileName, labelName, jobId)
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_synthetic.py", line 18, in main
    moea = run_mo_gakmeans(data,numClusters,numGen = 350, sizePop = 600)
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/clusterer.py", line 245, in run_mo_gakmeans
    best_ind = select_best(pop)
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/clusterer.py", line 91, in select_best
    dbi_scores.append(dbi(data, membership))
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/validator.py", line 14, in dbi
    return davies_bouldin_score(data, labels)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/sklearn/metrics/cluster/_unsupervised.py", line 344, in davies_bouldin_score
    check_number_of_labels(n_labels, n_samples)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/sklearn/metrics/cluster/_unsupervised.py", line 33, in check_number_of_labels
    raise ValueError(
ValueError: Number of labels is 1. Valid values are 2 to n_samples - 1 (inclusive)
