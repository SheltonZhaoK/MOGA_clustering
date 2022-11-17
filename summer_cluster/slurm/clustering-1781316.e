2022-07-16 01:02:36.418968: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-07-16 01:02:36.418996: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_synthetic.py", line 31, in <module>
    main(dirName, fileName, labelName)
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_synthetic.py", line 19, in main
    nmi = [nmi(labels, ga.memberships) , nmi(labels, kmeans_cluster), nmi(labels, seurat_cluster) ]
UnboundLocalError: local variable 'nmi' referenced before assignment
