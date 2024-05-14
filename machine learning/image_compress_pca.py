# https://www.enjoyalgorithms.com/blog/image-compression-using-pca
from PIL import Image, ImageOps
from sklearn.decomposition import PCA
import numpy as np
import os
import matplotlib.pyplot as plt

def img_data(imgPath, disp=True):
    orig_img = Image.open(imgPath)
    