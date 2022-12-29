import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bath, bhk):
    load_saved_artifacts()
    try:
        location_index = __data_columns.index(location.lower())
    except:
        location_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if location_index>=0:
        x[location_index] = 1

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print('Loading saved artifacts!')
    global __locations
    global __data_columns
    global __model
    
    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open('./artifacts/model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('Loading Done!')

def get_location_names():
    load_saved_artifacts()
    return __locations

    
if __name__=='__main__':
    load_saved_artifacts()
    
    print(get_estimated_price('1st block jayanagar', 1000, 3, 3))