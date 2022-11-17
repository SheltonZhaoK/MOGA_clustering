import random
#import tensorflow
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
from numpy.random import seed
from statistics import mean

def set_seed(seed):
    random.seed(seed)
    #tensorflow.random.set_seed(seed)
    np.random.seed(seed)

def prepare_externalData(fileName):
    data = pd.read_csv(fileName)
    test_x, test_y = data[["Instance #", "Cluster #", "CPUs"]].to_numpy(), data[["mo-time"]].to_numpy()
    return test_x, test_y

def run_linearReregression(x,y):
    reg = LinearRegression().fit(x, y)
    return reg

def run_randomForest(x,y):
    y = y.ravel()
    rf = RandomForestRegressor(n_estimators = 10)
    rf.fit(x, y)
    return rf

def perform_crossValidation(data, target):
    target_mean = np.mean(target)
    baseLine_error = [abs(x - target_mean) for x in target.tolist()]
    
    kfold = KFold(n_splits=fold, shuffle=True)
    MAE_lReg = []
    MAE_fr = []
    i = 0
    random_forest = None
    linear_regression = None
    for train, test in kfold.split(data):

        train_x, train_y = data[train], target[train]
        test_x, test_y = data[test], target[test]

        linear_regression = run_linearReregression(train_x, train_y)
        random_forest = run_randomForest(train_x, train_y)

        MAE_lReg.append(mean_absolute_error(test_y, linear_regression.predict(test_x)))
        MAE_fr.append(mean_absolute_error(test_y, random_forest.predict(test_x)))

    print("Cross Validation====================")
    print("Average baseline: %.2f" % (np.mean(baseLine_error)))
    print("Average MAE_lReg: %.2f" % (np.mean(MAE_lReg)))
    print("Average MAE_fr: %.2f\n" % (np.mean(MAE_fr)))

def perform_externalValidation(data, target, test_x, test_y):
    target_mean = np.mean(test_y)
    baseLine_error = [abs(x - target_mean) for x in test_y.tolist()]
    linear_regression = run_linearReregression(data, target)
    random_forest = run_randomForest(data, target)
    MAE_lRef = mean_absolute_error(test_y, linear_regression.predict(test_x))
    MAE_rf = mean_absolute_error(test_y, random_forest.predict(test_x))
    print("Average baseline: %.2f" % (np.mean(baseLine_error)))
    print("lRef MAE: %.2f" % (MAE_lRef))
    print("rf MAE: %.2f\n" % (MAE_rf) )

def main(dirName, fileName, kidneyFile, reference_dir,fold):
    set_seed(0)

    data = pd.read_csv(dirName + fileName)
    data, target = data[["size", "numLabels", "CPUs"]].to_numpy(), data[["time"]].to_numpy()
    
    perform_crossValidation(data, target)

    print("External Validation=================")
    print("scRNA-seq Reference Datasets")
    test_x, test_y = prepare_externalData(reference_dir + "/referenceDataset_total.csv")
    perform_externalValidation(data, target, test_x, test_y)

    return 

if __name__ == '__main__':
    dirName = '/deac/csc/khuriGrp/zhaok220/clustering_2/'
    fileName = 'data/synthetic_results.csv'
    kidneyFile = '/deac/csc/khuriGrp/zhaok220/clustering_2/output/kidney/kidney_results.csv'
    reference_dir = '/deac/csc/khuriGrp/zhaok220/clustering_2/data'
    fold = 5
    main(dirName, fileName, kidneyFile, reference_dir,fold)
   
