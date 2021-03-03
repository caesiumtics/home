from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

# load and show an image with Pillow
from PIL import Image

# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot

"""
# Simple Streamlit app by KS
"""

with st.echo(code_location = 'below'):
    total_points = st.slider("Show image?", 0, 1, 0)
    
    # load image as pixel array
    image = image.imread('kolala.jpeg')
    # summarize shape of the pixel array
    print(image.dtype)
    print(image.shape)
    # display the array of pixels as an image
    pyplot.imshow(image)
    pyplot.show()
