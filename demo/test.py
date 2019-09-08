import numpy as np
import pickle
test=[[0.5239,2.0802,1.1129,6.134,0.8408]]# testing data
sex=0
with open('train_data_rk'+str(sex)+'.pkl', 'rb') as input:
    Model = pickle.load(input)

predictions = Model.predict(test)
print(predictions)
