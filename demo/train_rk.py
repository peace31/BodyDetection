import openpyxl as px
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier
import pickle
# read xlsx file
W = px.load_workbook('trainingdata.xlsx')
# read each sheet from excel file
pw = W.get_sheet_by_name(name = 'Women Analysis')
pm = W.get_sheet_by_name(name = 'Men Analysis')
# scrapping needed ratios
A=np.zeros([2208,8])
# mend data
ab=np.zeros([1774,5])
# women data
af=np.zeros([2208,5])
# women rating data
scoref=np.zeros([2208,1])
# men rating data
scoreb=np.zeros([1774,5])

# scrapping needed ratios for Women analysis data
rownum=0
colnum=0
for row in pw.iter_rows():
    if(rownum<3 or rownum>2210):
        rownum+=1
        continue
    for k in row:
        if(colnum<5):
            af[rownum -3][colnum] =int( float(k.internal_value)*10000)/10000.0
        else :
            scoref[rownum - 3][0] = int(2*float(k.internal_value)*10000)/10000.0

        colnum+=1
        continue
           
    colnum = 0
    rownum+=1



# randorm forest algorithm
def random_forest_classifier(features, target):
        clf = RandomForestClassifier()
        clf.fit(features, target)
        return clf



# sex=1 for male, sex=0 for female
sex=0


test=af[-2,:] #[0.5039,2.602,1.1129,5.434,0.8408]# testing data
test=test.reshape(1,-1)

if(sex==0):

    #for i in range(5):
        #train_x=af[:,:]# training data
        #train_x=train_x.reshape(-1,1)
        #train_y=scoref[:,:-1]# label data
        #train_y=train_y.reshape(-1,1)
        af=af.reshape(-1,5)
        scoref=scoref.reshape(-1,1)
    
        trained_model = random_forest_classifier(af, scoref)#  creat random forest model
        print(trained_model)
        with open('train_data_rk' + str(sex) + '.pkl', 'wb') as output:
            pickle.dump(trained_model, output, pickle.HIGHEST_PROTOCOL)
        prediction = trained_model.predict(test)
        print(prediction)
        #Model.append(trained_model)
   
    





