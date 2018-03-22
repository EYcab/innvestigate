import numpy as np

import innvestigate
import innvestigate.utils as iutils
import innvestigate.utils.visualizations as ivis


def preprocess(X):
    X = X.copy()
    X = net["preprocess_f"](X)
    return X

def postprocess(X):
    X = X.copy()
    X = iutils.postprocess_images(X, color_coding=color_conversion, channels_first=channels_first)
    return X

def image(X):
    X = X.copy()
    return ivis.project(X, absmax=255.0, input_is_postive_only=True)

def bk_proj(X):
    X = ivis.clip_quantile(X, 1)
    return ivis.project(X)

def heatmap(X):
    return ivis.heatmap(X)

def graymap(X):
    return ivis.graymap(np.abs(X), input_is_postive_only=True)