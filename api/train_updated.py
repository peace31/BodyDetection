import openpyxl as px
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier
import pickle
from api.models import UserInput


# Randorm forest algorithm
def random_forest_classifier(features, target):
    clf = RandomForestClassifier()
    clf.fit(features, target)
    return clf


# Create train data for women
def create_train_women():
    # A=np.zeros([2208,8])
    # women data
    women_count = UserInput.objects.filter(gender=1).count()
    if women_count == 0:
        return

    af=np.zeros([women_count,5])
    # women rating data
    scoref=np.zeros([women_count,1])

    # Scrapping data from Women Analysis sheet
    rownum=0
    for row in UserInput.objects.filter(gender=1).values('legs_body', 'shoulder_hips', 'body_waist', 'bust_waist', 'waist_hips', 'score'):
        legs_body = row['legs_body'] if row['legs_body'] else 0
        shoulder_hips = row['shoulder_hips'] if row['shoulder_hips'] else 0
        body_waist = row['body_waist'] if row['body_waist'] else 0
        bust_waist = row['bust_waist'] if row['bust_waist'] else 0
        waist_hips = row['waist_hips'] if row['waist_hips'] else 0
        score = row['score'] if row['score'] else 0

        af[rownum][0] = int(float(legs_body)*10000)/10000.0
        af[rownum][1] = int(float(shoulder_hips)*10000)/10000.0
        af[rownum][2] = int(float(body_waist)*10000)/10000.0
        af[rownum][3] = int(float(bust_waist)*10000)/10000.0
        af[rownum][4] = int(float(waist_hips)*10000)/10000.0
        scoref[rownum][0] = float(int(int(2*float(score)*10000)/10000.0))

        rownum += 1

    # Training Random Forest Algo for Women and creating Pickle Train_data_women

    af=af.reshape(-1,5)
    scoref=scoref.reshape(-1,1)

    trained_model_w = random_forest_classifier(af, scoref)#  create random forest model
    with open('train_data_women.pkl', 'wb') as output:
      pickle.dump(trained_model_w, output, pickle.HIGHEST_PROTOCOL)


# Create train data for men
def create_train_men():
    # A=np.zeros([2208,8])
    # mend data
    men_count = UserInput.objects.filter(gender=0).count()
    if men_count == 0:
        return

    af=np.zeros([men_count,5])
    # men rating data
    scoref=np.zeros([men_count,1])

    # Scrapping data from Women Analysis sheet
    rownum=0
    for row in UserInput.objects.filter(gender=0).values('legs_body', 'shoulder_hips', 'body_waist', 'bust_waist', 'waist_hips', 'score'):
        legs_body = row['legs_body'] if row['legs_body'] else 0
        shoulder_hips = row['shoulder_hips'] if row['shoulder_hips'] else 0
        body_waist = row['body_waist'] if row['body_waist'] else 0
        bust_waist = row['bust_waist'] if row['bust_waist'] else 0
        waist_hips = row['waist_hips'] if row['waist_hips'] else 0
        score = row['score'] if row['score'] else 0

        af[rownum][0] = int(float(legs_body)*10000)/10000.0
        af[rownum][1] = int(float(shoulder_hips)*10000)/10000.0
        af[rownum][2] = int(float(body_waist)*10000)/10000.0
        af[rownum][3] = int(float(bust_waist)*10000)/10000.0
        af[rownum][4] = int(float(waist_hips)*10000)/10000.0
        scoref[rownum][0] = int(int(2*float(score)*10000)/10000.0)

        rownum += 1

    # Training Random Forest Algo for men and creating Pickle Train_data_men

    af=af.reshape(-1,5)
    scoref=scoref.reshape(-1,1)

    trained_model_m = random_forest_classifier(af, scoref)#  create random forest model
    with open('train_data_men.pkl', 'wb') as output:
      pickle.dump(trained_model_m, output, pickle.HIGHEST_PROTOCOL)
