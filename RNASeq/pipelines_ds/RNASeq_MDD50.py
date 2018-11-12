import numpy as np
import pandas as pd
from sklearn.cluster import FeatureAgglomeration
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from tpot.builtins import DatasetSelector

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=50)

# Average CV score on the training set was:0.752695652173913
exported_pipeline = make_pipeline(
    DatasetSelector(sel_subset=12, subset_list="module23.csv"),
    FeatureAgglomeration(affinity="euclidean", linkage="average"),
    RandomForestClassifier(bootstrap=False, criterion="entropy", max_features=0.45, min_samples_leaf=9, min_samples_split=6, n_estimators=100)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)