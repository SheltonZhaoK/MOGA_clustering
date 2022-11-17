/var/lib/slurmd/job1783211/slurm_script: line 15: $'\n#SBATCH --array=0-29%30\n': command not found
2022-07-24 02:38:20.859525: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-07-24 02:38:20.860072: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Traceback (most recent call last):
  File "/deac/csc/khuriGrp/zhaok220/clustering/scripts/test_scrnaseq_time.py", line 46, in <module>
    jobID = sys.argv[1]
IndexError: list index out of range
