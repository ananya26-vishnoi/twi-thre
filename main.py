import plotly.graph_objects as go
import numpy as np
from PIL import Image

# Load a sample 2D image
image_path = '2d_Avatar.png'  # Replace with the actual path to your image
image_data = np.array(Image.open(image_path).convert('L'))  # Convert to grayscale if needed

# Create a meshgrid for 3D plot
x, y = np.meshgrid(np.arange(image_data.shape[1]), np.arange(image_data.shape[0]))

# Create a 3D surface plot
fig = go.Figure(data=[go.Surface(z=image_data, colorscale='Viridis')])

# Set axis labels
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

# Show the 3D plot in a browser window
fig.show()
