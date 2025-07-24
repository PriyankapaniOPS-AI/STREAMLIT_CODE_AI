import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="PEACOCK Image ", layout="wide")

# Title
st.title("PEACOCK Image to grey colour image")

# Load image from URL
@st.cache_data
def load_image():
    url = "https://cdn.pixabay.com/photo/2024/04/13/10/20/peacock-8693634_1280.jpg"
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# Load and display image
peacock= load_image()
st.image(peacock, caption="Original peacock Image",use_column_width=True)

# Convert to NumPy array
peacock_np = np.array(peacock)
#R, G, B = peacock_np[:, :, 0], peacock_np[:, :, 1], peacock_np[:, :, 2]

# Display RGB channels

# Grayscale + Colormap
st.subheader("Colormapped Grayscale Image")

peacock_gray = peacock.convert("L")
peacock_gray_np = np.array(peacock_gray)

# Plot using matplotlib with colormap
st.image(peacock_gray_np,use_column_width=True)
plt.axis("off")
