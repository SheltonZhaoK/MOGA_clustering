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

def run_linearReregression(x,y):
    reg = LinearRegression().fit(x, y)
    return reg

def run_randomForest(x,y):
    y = y.ravel()
    rf = RandomForestRegressor(n_estimators = 10)
    rf.fit(x, y)
    return rf

def prepare_data(synthetic_data, reference_data):
    data = pd.read_csv(synthetic_data)
    syn_data, syn_target = data[["size", "numLabels", "CPUs"]].to_numpy(), data[["time"]].to_numpy()

    data = pd.read_csv(reference_data)
    reference_data, reference_target = data[["Instance #", "Cluster #", "CPUs"]].to_numpy(), data[["mo-time"]].to_numpy()

    return syn_data, syn_target, reference_data, reference_target

def calculate_baseLine_err(target):
    mean = np.mean(target)
    err = [abs(x - mean) for x in target.tolist()]
    return np.mean(err)

def main(synthetic_data, reference_data, fold):
    set_seed(0)
    data = pd.read_csv(synthetic_data)[["size", "numLabels", "CPUs"]]
    features = data.columns.tolist()
    syn_data, syn_target, ref_data, ref_target = prepare_data(synthetic_data, reference_data)

    syn_baseLine_error = calculate_baseLine_err(syn_target)
    ref_baseLine_error = calculate_baseLine_err(ref_target)
    
    kfold = KFold(n_splits=fold, shuffle=True)
    MAE_syn_lReg = []
    MAE_syn_fr = []
    MAE_ref_lReg = []
    MAE_ref_fr = []

    random_forest = None
    linear_regression = None
    feature_importance = [0,0,0]

    for train, test in kfold.split(syn_data):

        train_x, train_y = syn_data[train], syn_target[train]
        test_x, test_y = syn_data[test], syn_target[test]
 
        linear_regression = run_linearReregression(train_x, train_y)
        random_forest = run_randomForest(train_x, train_y)
        fi = random_forest.feature_importances_
        feature_importance = [x + y for x, y in zip(feature_importance, fi)]

        MAE_syn_lReg.append(mean_absolute_error(test_y, linear_regression.predict(test_x)))
        MAE_syn_fr.append(mean_absolute_error(test_y, random_forest.predict(test_x)))

        MAE_ref_lReg.append(mean_absolute_error(ref_target, linear_regression.predict(ref_data)))
        MAE_ref_fr.append(mean_absolute_error(ref_target, random_forest.predict(ref_data)))
    
    feature_importance = [x / 5 for x in feature_importance]

    print("MAE_syn_lReg:",np.mean(MAE_syn_lReg))
    print("MAE_syn_fr:  ",np.mean(MAE_syn_fr))
    print("MAE_ref_lReg:",np.mean(MAE_ref_lReg))
    print("MAE_ref_fr:  ",np.mean(MAE_ref_fr))
    print("syn_baseLine_error:", syn_baseLine_error)
    print("ref_baseLine_error:", ref_baseLine_error)
    print("=====================================")
    print("features:           ",features)
    print("feature importance: ",feature_importance)

    return 

if __name__ == '__main__':
    synthetic_data = '/deac/csc/khuriGrp/zhaok220/clustering_2/data/synthetic_results.csv'
    reference_data = '/deac/csc/khuriGrp/zhaok220/clustering_2/data/referenceDataset_total.csv'
    fold = 5
    main(synthetic_data, reference_data, fold)
   
