from flask import Flask
from flask import make_response, request, current_app
from flask import *
from flask import send_from_directory
from PIL import Image
import requests
import cPickle
from io import BytesIO
import os
import sys
import numpy as np
from skimage import io
from config import load_config
sys.path.append('/home/ubuntu/flaskapp/nnet')
import predict 
sys.path.append('/home/ubuntu/flaskapp/util')
import visualize
sys.path.append('/home/ubuntu/flaskapp/dataset')
import pose_dataset
#from api.models import Post, UserInput

app = Flask(__name__)

def get_image_response(image_path, sex, bf_flag, picture):
    try:
        # sex=1 for male, sex=0 for female
        #sex=1
        # if image is front image, bf_flag=0, else 1
        #bf_flag=1
        # Read image from file
        #file_name = "./demo/1.jpg"
        # image_path = '.' + image_path
        # image_path = "./demo/1.jpg"
        print('image_path = ', image_path)
        print('sex =', sex)
        print('bf_flag = ', bf_flag)
        # return "ok"
        image = io.imread(image_path)
        # return "ok"
        # image = cv2.imread(image_path)
        image=np.array(image)
        # return "ok"
        image_batch =pose_dataset. data_to_input(image)
        cfg = load_config("/home/ubuntu/flaskapp/demo/pose_cfg.yaml")
        print('image_batch = ', image_batch)
        print('image = ', image)
        
        sess, inputs, outputs = predict.setup_pose_prediction(cfg)
        
        # Compute prediction with the CNN
        outputs_np = sess.run(outputs, feed_dict={inputs: image_batch})

        print('outputs_np = ', outputs_np)
        scmap, locref, _ = predict.extract_cnn_output(outputs_np, cfg)
        print('scmap = ', scmap)
        print('locref = ', locref)

        # Extract maximum scoring location from the heatmap, assume 1 person
        pose = predict.argmax_pose_predict(scmap, locref, cfg.stride)
        print('pose = ', pose)

        # Visualise
        LB_ratio,SH_ratio,CW_ratio,BW_ratio,WH_ratio,ratio = visualize.show_heatmaps(image, pose,sex,bf_flag)
        if(LB_ratio==0 and SH_ratio==0 and CW_ratio==0 and BW_ratio==0 and WH_ratio):
            return 0,0,0,0,0,[],0
            # return "ok"
        # visualize.waitforbuttonpress()
        # return "sys.path()"
        score = 0
        # return "ok1"
        # if picture == 0: # if picture is Mine
        #     test=[[LB_ratio,SH_ratio,CW_ratio,BW_ratio,WH_ratio]]

        #     if sex == 1 or sex == '1':
        #         sex = 'men'
        #     else:
        #         sex = 'women'

        #     Model = cPickle.load(open('/home/ubuntu/flaskapp/demo/train_data_'+sex+'.pkl', 'rb'))
        #     # return sex
        #     prediction = (Model.predict(test))/2 # dividing by 2 since RFA training was done with integers by doubling the original score
        #     score = prediction[0]

        return LB_ratio,SH_ratio,CW_ratio,BW_ratio,WH_ratio,ratio,score
    except:
        # return "ok12"
        return 0,0,0,0,0,[],0

@app.route('/')
def hello_world():
  return 'Hello from Flask!'
@app.route('/user-inputs',methods=['POST'])
def main():
    if(request.method=='POST'):
        # print('post method called...')
        # print('request...', request)
        # print('request body',request.get_json())
        # print('request data',request.data)
        # print('request form',request.form)
        # print('request files..', request.files)
        image_path = request.form['image_path']
        sex = int(str(request.form['sex']))
        bf_flag = int(str(request.form['bf_flag']))
        picture = int(str(request.form['picture']))
        # r=get_image_response(image_path, sex, bf_flag, picture)
        # return r
        # store image in database
        #iuser_input = UserInput.objects.create(user_id=1, image=image_path, picture=picture, angle=bf_flag)
        #Post.objects.create(user_id=1, input_id=user_input.id)

        LB_ratio,SH_ratio,CW_ratio,BW_ratio,WH_ratio,ratio,score=get_image_response(image_path, sex, bf_flag, picture)
        if(LB_ratio==0.0 and SH_ratio==0.0 and CW_ratio==0.0 and BW_ratio==0 and WH_ratio==0):
            return json.dumps({})
        # return str(LB_ratio)
        bust_waist = round(CW_ratio, 2)
        waist_hips = round(WH_ratio, 2)
        legs_body = round(LB_ratio, 2)
        body_waist = round(BW_ratio, 2)
        shoulder_hips = round(SH_ratio, 2)
        score = round(score, 2)
        ratios = ratio
        json_data = json.dumps({'bust_waist': bust_waist, 'waist_hips': waist_hips,'legs_body':legs_body,'legs_body':legs_body,'body_waist':body_waist,'shoulder_hips':shoulder_hips,'score':score,'ratios':ratios})
        print('json data = ', json_data)
        return json_data
    return None
# @app.route('/main', methods=['POST'])
# def main():
if __name__ == '__main__':
  app.run()
