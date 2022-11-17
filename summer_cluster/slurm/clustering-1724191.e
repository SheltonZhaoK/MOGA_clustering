2022-06-13 14:53:52.954120: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-06-13 14:53:52.954186: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/xxx.py", line 114, in <module>
    main(dirName,className)  
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/xxx.py", line 92, in main
    ga = run_so_gakmeans(datasets = data, numCenters = numCenters)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/numba/cuda/compiler.py", line 908, in __call__
    raise ValueError(missing_launch_config_msg)
ValueError: 
Kernel launch configuration was not specified. Use the syntax:

kernel_function[blockspergrid, threadsperblock](arg0, arg1, ..., argn)

See https://numba.readthedocs.io/en/stable/cuda/kernels.html#kernel-invocation for help.


