from PIL import Image 
from PIL import ImageFilter 
import os 
from tqdm import tqdm
import cv2
import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from detectron2.structures import Boxes
from google.colab.patches import cv2_imshow


input_path = '/home/euiseokjeong/Desktop/ES_Object_Detection/detectron2/imlab_data/screen_shots_cropped/'
output_path = '/home/euiseokjeong/Desktop/ES_Object_Detection/detectron2/imlab_data/output_200825/'

screen_shots_list = os.listdir(input_path)
data_pd = []

cfg = get_cfg()
# add project-specific config (e.g., TensorMask) here if you're not running a model in detectron2's core library
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7 # set threshold for this model
# Find a model from detectron2's model zoo. You can use the https://dl.fbaipublicfiles... url as well
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
predictor = DefaultPredictor(cfg)

screen_shots_list = os.listdir(input_path)

#object detecting and save as csv file

data_pd = pd.DataFrame(columns=['file name', 'class number', 'score', 'x1', 'y1', 'x2', 'y2'])

data_pd.to_csv(f'{output_path}/data_using_append.csv')

for i, name in tqdm(enumerate(screen_shots_list)):
    im = cv2.imread(input_path + name)
    outputs = predictor(im)

    #get class, location of box
    box = outputs["instances"].pred_boxes

    if len(box) > 0:
        #get class, location of box
        class_num = outputs["instances"].pred_classes
        score = outputs["instances"].scores

        print("File: " + name)

        # make file_name dataframe
        file_name = []
        for i in range(len(class_num)):
            file_name.append(name)

        #convert to dataframe
        box_pd = pd.DataFrame(box.tensor.detach().cpu().numpy())
        class_num_pd = pd.DataFrame(class_num.detach().cpu().numpy())
        score_pd = pd.DataFrame(score.detach().cpu().numpy())
        file_name_pd = pd.DataFrame(file_name)

        file_name_pd.columns = ['file name']
        class_num_pd.columns = ['class number']
        score_pd.columns = ['score']
        box_pd.columns = ['x1', 'y1', 'x2', 'y2']

        box_class_pd = pd.concat([file_name_pd, class_num_pd, score_pd, box_pd], axis = 1)

        box_class_pd.to_csv(f'{output_path}/data_using_append.csv', mode='a', header=False)

    else:
        pass

