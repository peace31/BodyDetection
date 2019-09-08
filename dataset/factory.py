import os
import sys

sys.path.append('/home/ubuntu/flaskapp/dataset')
import pose_dataset 

def create(cfg):
    dataset_type = cfg.dataset_type
    if dataset_type == "mpii":
        import mpii 
        data = mpii.MPII(cfg)
    elif dataset_type == "coco":
        import mscoco 
        data =mscoco. MSCOCO(cfg)
    elif dataset_type == "penn_action":
        import penn_action 
        data = penn_action.PennAction(cfg)
    elif dataset_type == "default":
        data = pose_dataset.PoseDataset(cfg)
    else:
        raise Exception("Unsupported dataset_type: \"{}\"".format(dataset_type))
    return data
