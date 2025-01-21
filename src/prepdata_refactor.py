import csv
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.preprocessing import OneHotEncoder

DATA_FOLDER = Path("datasets")

def loadCsv(file_path):
    data = []
    with file_path.open('r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(np.array(row))
    data = np.array(data)
    (n, d) = data.shape
    return data, n, d

def oneHotEncodeColumns(data, columnsCategories):
    # ...existing code...
    dataCategories = data[:, columnsCategories]
    dataEncoded = OneHotEncoder(sparse_output=False).fit_transform(dataCategories)
    columnsNumerical = [i for i in range(data.shape[1]) if i not in columnsCategories]
    dataNumerical = data[:, columnsNumerical]
    return np.hstack((dataNumerical, dataEncoded)).astype(float)

# Smaller specialized loaders
def _abalone_loader(dataset):
    data = pd.read_csv(DATA_FOLDER / "abalone.data", header=None)
    data = pd.get_dummies(data, dtype=float)
    if dataset == 'abalone8':
        y = np.array([1 if elt == 8 else 0 for elt in data[8]])
    elif dataset == 'abalone17':
        y = np.array([1 if elt == 17 else 0 for elt in data[8]])
    else:  # abalone20
        y = np.array([1 if elt == 20 else 0 for elt in data[8]])
    X = np.array(data.drop([8], axis=1))
    return X, y

def _autompg_loader():
    data = pd.read_csv(DATA_FOLDER / "auto-mpg.data", header=None, sep=r'\s+')
    data = data.replace('?', np.nan).dropna().drop([8], axis=1).astype(float)
    y = np.array([1 if elt in [2, 3] else 0 for elt in data[7]])
    X = np.array(data.drop([7], axis=1))
    return X, y

def _australian_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'australian.data')
    X = data[:, np.arange(d-1)].astype(float)
    y = data[:, d-1].astype(int)
    y[y != 1] = 0
    return X, y

def _balance_loader():
    data = pd.read_csv(DATA_FOLDER / "balance-scale.data", header=None)
    y = np.array([1 if elt == 'L' else 0 for elt in data[0]])
    X = np.array(data.drop([0], axis=1))
    return X, y

def _bankmarketing_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'bankmarketing.csv')
    X = data[:, np.arange(0, d-1)]
    X = oneHotEncodeColumns(X, [1, 2, 3, 4, 6, 7, 8, 10, 15])
    y = data[:, d-1]
    y[y == "no"] = "0"
    y[y == "yes"] = "1"
    y = y.astype(int)
    return X, y

def _bupa_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'bupa.dat')
    X = data[:, np.arange(d-1)].astype(float)
    y = data[:, d-1].astype(int)
    y[y != 1] = 0
    return X, y

def _german_loader():
    data = pd.read_csv(DATA_FOLDER / 'german.data-numeric', header=None, sep=r'\s+')
    y = np.array([1 if elt == 2 else 0 for elt in data[24]])
    X = np.array(data.drop([24], axis=1))
    return X, y

def _glass_loader():
    data = pd.read_csv(DATA_FOLDER / 'glass.data', header=None, index_col=0)
    y = np.array([1 if elt == 1 else 0 for elt in data[10]])
    X = np.array(data.drop([10], axis=1))
    return X, y

def _hayes_loader():
    data = pd.read_csv(DATA_FOLDER / 'hayes-roth.data', header=None)
    y = np.array([1 if elt == 3 else 0 for elt in data[5]])
    X = np.array(data.drop([0, 5], axis=1))
    return X, y

def _heart_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'heart.data')
    X = data[:, np.arange(d-1)].astype(float)
    y = data[:, d-1].astype(int)
    y[y != 2] = 0
    y[y == 2] = 1
    return X, y

def _iono_loader():
    data = pd.read_csv(DATA_FOLDER / 'ionosphere.data', header=None)
    y = np.array([1 if elt == 'b' else 0 for elt in data[34]])
    X = np.array(data.drop([34], axis=1))
    return X, y

def _libras_loader():
    data = pd.read_csv(DATA_FOLDER / 'movement_libras.data', header=None)
    y = np.array([1 if elt == 1 else 0 for elt in data[90]])
    X = np.array(data.drop([90], axis=1))
    return X, y

def _newthyroid_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'newthyroid.dat')
    X = data[:, np.arange(d-1)].astype(float)
    y = data[:, d-1].astype(int)
    y[y < 2] = 0
    y[y >= 2] = 1
    return X, y

def _pageblocks_loader():
    data = pd.read_csv(DATA_FOLDER / 'page-blocks.data', header=None, sep=r'\s+')
    y = np.array([1 if elt in [2, 3, 4, 5] else 0 for elt in data[10]])
    X = np.array(data.drop([10], axis=1))
    return X, y

def _pima_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'pima-indians-diabetes.data')
    X = data[:, np.arange(d-1)].astype(float)
    y = data[:, d-1]
    y[y != '1'] = '0'
    y = y.astype(int)
    return X, y

def _satimage_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'satimage.data')
    X = data[:, np.arange(d-1)].astype(float)
    y = data[:, d-1].astype(int)
    y[y != 4] = 0
    y[y == 4] = 1
    return X, y

def _segmentation_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'segmentation.data')
    X = data[:, np.arange(1, d)].astype(float)
    y = data[:, 0]
    y[y == "WINDOW"] = '1'
    y[y != '1'] = '0'
    y = y.astype(int)
    return X, y

def _sonar_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'sonar.dat')
    X = data[:, np.arange(d-1)].astype(float)
    y = data[:, d-1]
    y[y != 'R'] = '0'
    y[y == 'R'] = '1'
    y = y.astype(int)
    return X, y

def _spambase_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'spambase.dat')
    X = data[:, np.arange(d-1)].astype(float)
    y = data[:, d-1].astype(int)
    y[y != 1] = 0
    return X, y

def _splice_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'splice.data')
    X = data[:, np.arange(1, d)].astype(float)
    y = data[:, 0].astype(int)
    y[y == 1] = 2
    y[y == -1] = 1
    y[y == 2] = 0
    return X, y

def _vehicle_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'vehicle.data')
    X = data[:, np.arange(d-1)].astype(float)
    y = data[:, d-1]
    y[y != "van"] = '0'
    y[y == "van"] = '1'
    y = y.astype(int)
    return X, y

def _wdbc_loader():
    data, n, d = loadCsv(DATA_FOLDER / 'wdbc.dat')
    X = data[:, np.arange(d-1)].astype(float)
    y = data[:, d-1]
    y[y != 'M'] = '0'
    y[y == 'M'] = '1'
    y = y.astype(int)
    return X, y

def _wine_loader():
    data = pd.read_csv(DATA_FOLDER / 'wine.data', header=None)
    y = np.array([1 if elt == 1 else 0 for elt in data[0]])
    X = np.array(data.drop([0], axis=1))
    return X, y

def _wine4_loader():
    data = pd.read_csv(DATA_FOLDER / 'winequality-red.csv', sep=';')
    y = np.array([1 if elt == 4 else 0 for elt in data.quality])
    X = np.array(data.drop(["quality"], axis=1))
    return X, y

def _yeast_loader(dataset):
    data = pd.read_csv(DATA_FOLDER / 'yeast.data', header=None, sep=r'\s+')
    data = data.drop([0], axis=1)
    if dataset == 'yeast3':
        y = np.array([1 if elt == 'ME3' else 0 for elt in data[9]])
    else:  # yeast6
        y = np.array([1 if elt == 'EXC' else 0 for elt in data[9]])
    X = np.array(data.drop([9], axis=1))
    return X, y

dataset_loaders = {
    'abalone8': _abalone_loader,
    'abalone17': _abalone_loader,
    'abalone20': _abalone_loader,
    'autompg': _autompg_loader,
    'australian': _australian_loader,
    'balance': _balance_loader,
    'bankmarketing': _bankmarketing_loader,
    'bupa': _bupa_loader,
    'german': _german_loader,
    'glass': _glass_loader,
    'hayes': _hayes_loader,
    'heart': _heart_loader,
    'iono': _iono_loader,
    'libras': _libras_loader,
    'newthyroid': _newthyroid_loader,
    'pageblocks': _pageblocks_loader,
    'pima': _pima_loader,
    'satimage': _satimage_loader,
    'segmentation': _segmentation_loader,
    'sonar': _sonar_loader,
    'spambase': _spambase_loader,
    'splice': _splice_loader,
    'vehicle': _vehicle_loader,
    'wdbc': _wdbc_loader,
    'wine': _wine_loader,
    'wine4': _wine4_loader,
    'yeast3': _yeast_loader,
    'yeast6': _yeast_loader
}

def data_recovery(dataset):
    loader = dataset_loaders.get(dataset)
    if not loader:
        raise ValueError(f"Unrecognized dataset: {dataset}")
    return loader(dataset)