import openpyxl as px
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle


# randorm forest algorithm
def random_forest_classifier(features, target):
    clf = RandomForestClassifier()
    clf.fit(features, target)
    return clf
def load_data(sex, filename):

    # read xlsx file
    W = px.load_workbook('trainingdata.xlsx')
    # read each sheet from excel file
    if (sex == 0):
        pw = W.get_sheet_by_name(name='Women Analysis')
    else:
        pw = W.get_sheet_by_name(name='Men Analysis')
    # scrapping needed ratios
    A = np.zeros([2208, 8])
    # women data
    af = np.zeros([2208, 5])
    # women rating data
    scoref = np.zeros([2208, 1])
    # scrapping needed ratios for Women analysis data
    rownum = 0
    colnum = 0
    for row in pw.iter_rows():
        if (rownum < 3 or rownum > 2210):
            rownum += 1
            continue
        for k in row:
            if (colnum < 5):
                af[rownum - 3][colnum] = float(k.internal_value)
            else:
                scoref[rownum - 3][0] = 2 * float(k.internal_value)

            colnum += 1
            continue

        colnum = 0
        rownum += 1

    af = af.reshape(-1, 5)
    scoref = scoref.reshape(-1, 1)

    trained_model = random_forest_classifier(af, scoref)  # creat random forest model
    print(trained_model)
    with open('train_data_rk' + str(sex) + '.pkl', 'wb') as output:
        pickle.dump(trained_model, output, pickle.HIGHEST_PROTOCOL)






    # Model.append(trained_model)







