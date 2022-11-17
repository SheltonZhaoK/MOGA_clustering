/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/deap/creator.py:138: RuntimeWarning: A class named 'FitnessMin' has already been created and it will be overwritten. Consider deleting previous creation of that class or rename it.
  warnings.warn("A class named '{0}' has already been created and it "
/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/deap/creator.py:138: RuntimeWarning: A class named 'Individual' has already been created and it will be overwritten. Consider deleting previous creation of that class or rename it.
  warnings.warn("A class named '{0}' has already been created and it "
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering_1/scripts/pop_iter_scrna.py", line 26, in <module>
    main(dirName,dataName)
  File "/deac/csc/khuriGrp/zhaok220/clustering_1/scripts/pop_iter_scrna.py", line 19, in main
    report.columns = [100,200,300,400,500,600,700,800]
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/generic.py", line 5596, in __setattr__
    return object.__setattr__(self, name, value)
  File "pandas/_libs/properties.pyx", line 70, in pandas._libs.properties.AxisProperty.__set__
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/generic.py", line 769, in _set_axis
    self._mgr.set_axis(axis, labels)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/internals/managers.py", line 214, in set_axis
    self._validate_set_axis(axis, new_labels)
  File "/deac/csc/khuriGrp/software/zhaok220/lib/python3.8/site-packages/pandas/core/internals/base.py", line 69, in _validate_set_axis
    raise ValueError(
ValueError: Length mismatch: Expected axis has 2 elements, new values have 8 elements
