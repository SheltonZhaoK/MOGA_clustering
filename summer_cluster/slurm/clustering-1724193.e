2022-06-13 14:57:36.398325: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-06-13 14:57:36.398517: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/xxx.py", line 114, in <module>
    main(dirName,className)  
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/xxx.py", line 92, in main
    ga = run_so_gakmeans(datasets = data, numCenters = numCenters)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/numba/core/dispatcher.py", line 471, in _compile_for_args
    error_rewrite(e, 'unsupported_error')
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/numba/core/dispatcher.py", line 409, in error_rewrite
    raise e.with_traceback(None)
numba.core.errors.UnsupportedError: Failed in nopython mode pipeline (step: analyzing bytecode)
Use of unsupported opcode (STORE_GLOBAL) found

File "../scripts/clusterer2.py", line 61:
def run_so_gakmeans(datasets, numCenters, indPb = 1.0, mutPb = 0.07, cxPb = 0.9,\
    <source elided>
   global data
   numCenter = numCenters
   ^

