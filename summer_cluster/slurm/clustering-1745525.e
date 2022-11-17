2022-06-20 00:06:47.890444: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-06-20 00:06:47.890484: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_keel.py", line 82, in <module>
    main(dirName)  
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_keel.py", line 73, in main
    report.loc[len(report)] = [dataset, data.shape[0],data.shape[1], numCenters,"{:.2f}".format(silhouette_ga), \
NameError: name 'dataset' is not defined
