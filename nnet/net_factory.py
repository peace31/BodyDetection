import os
import sys

sys.path.append('/home/ubuntu/flaskapp/nnet')
from pose_net import PoseNet


def pose_net(cfg):
    cls = PoseNet(cfg)
        
    return cls
