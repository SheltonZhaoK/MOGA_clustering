2022-07-25 11:40:20.008070: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-07-25 11:40:20.008150: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/deap/creator.py:138: RuntimeWarning: A class named 'Individual' has already been created and it will be overwritten. Consider deleting previous creation of that class or rename it.
  warnings.warn("A class named '{0}' has already been created and it "
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_synthetic.py", line 51, in <module>
    main(dirName, fileName, labelName)
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_synthetic.py", line 25, in main
    kmeans = run_kmeans(data, numCenters, 400)
NameError: name 'numCenters' is not defined
