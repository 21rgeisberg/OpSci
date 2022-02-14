import pixellib
from pixellib.instance import instance_segmentation 
segment_image = instance_segmentation()
segment_image.load_model("mask_rcnn_coco.h5")
segment_image.segmentImage("semanticTestPhoto.jpeg", output_image_name = "newImage.jpg")

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import LassoSelector
# from matplotlib.path import Path