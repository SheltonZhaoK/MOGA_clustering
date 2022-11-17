2022-06-10 13:53:39.560093: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-06-10 13:53:39.560147: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/internals/construction.py", line 982, in _finalize_columns_and_data
    columns = _validate_or_indexify_columns(contents, columns)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/internals/construction.py", line 1030, in _validate_or_indexify_columns
    raise AssertionError(
AssertionError: 5 columns passed, passed data had 150 columns

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/pop_iter_tuning.py", line 80, in <module>
    main(dirName,className)  
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/pop_iter_tuning.py", line 71, in main
    report = pd.DataFrame(fitness, columns =['20', '40', '60', '80', '100']) 
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/frame.py", line 721, in __init__
    arrays, columns, index = nested_data_to_arrays(
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/internals/construction.py", line 519, in nested_data_to_arrays
    arrays, columns = to_arrays(data, columns, dtype=dtype)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/internals/construction.py", line 883, in to_arrays
    content, columns = _finalize_columns_and_data(arr, columns, dtype)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/internals/construction.py", line 985, in _finalize_columns_and_data
    raise ValueError(err) from err
ValueError: 5 columns passed, passed data had 150 columns
