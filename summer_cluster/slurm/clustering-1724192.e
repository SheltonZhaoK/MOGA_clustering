2022-06-13 14:56:11.183260: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-06-13 14:56:11.183321: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/xxx.py", line 114, in <module>
    main(dirName,className)  
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/xxx.py", line 92, in main
    ga = run_so_gakmeans(datasets = data, numCenters = numCenters)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/numba/core/dispatcher.py", line 487, in _compile_for_args
    raise e
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/numba/core/dispatcher.py", line 420, in _compile_for_args
    return_val = self.compile(tuple(argtypes))
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/numba/core/dispatcher.py", line 965, in compile
    cres = self._compiler.compile(args, return_type)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/numba/core/dispatcher.py", line 125, in compile
    status, retval = self._compile_cached(args, return_type)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/numba/core/dispatcher.py", line 139, in _compile_cached
    retval = self._compile_core(args, return_type)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/numba/core/dispatcher.py", line 148, in _compile_core
    self.targetdescr.options.parse_as_flags(flags, self.targetoptions)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/numba/core/options.py", line 41, in parse_as_flags
    opt._apply(flags, options)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/numba/core/options.py", line 66, in _apply
    raise KeyError(m)
KeyError: "Unrecognized options: {'target'}. Known options are dict_keys(['_nrt', 'boundscheck', 'debug', 'error_model', 'fastmath', 'forceinline', 'forceobj', 'inline', 'looplift', 'no_cfunc_wrapper', 'no_cpython_wrapper', 'no_rewrites', 'nogil', 'nopython', 'parallel', 'target_backend'])"
