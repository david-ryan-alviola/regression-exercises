import sklearn as skl
import pandas as pd

def generate_scaled_splits(train, validate, test, scaler=skl.preprocessing.MinMaxScaler()):
    scaler.fit(train)
    
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns)
    validate_scaled = pd.DataFrame(scaler.transform(validate), columns=validate.columns)
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns)
    
    return train_scaled, validate_scaled, test_scaled