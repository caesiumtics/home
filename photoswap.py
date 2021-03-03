from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

# load and show an image with Pillow
from PIL import Image

"""
# Simple Streamlit app by KS
"""

with st.echo(code_location = 'below'):
    total_points = st.slider("Show image?", 0, 1, 0)
    
    # Open the image form working directory
    image = Image.open('kolala.jpeg')
    # summarize some details about the image
    print(image.format)
    print(image.size)
    print(image.mode)
    # show the image
    load_image.show()
