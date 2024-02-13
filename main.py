# import cv2
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt

# # Install dependencies
# # pip install opencv-python numpy matplotlib

# def convert_to_3d(image_path):
#     # Read the 2D image
#     img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#     # Create a 3D surface plot using matplotlib
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')

#     # Generate X and Y coordinates based on the image size
#     x = np.arange(0, img.shape[1], 1)
#     y = np.arange(0, img.shape[0], 1)
#     x, y = np.meshgrid(x, y)

#     # Normalize pixel values to the range [0, 1]
#     z = img / 255.0

#     # Extrude the image based on pixel values
#     ax.plot_surface(x, y, z, cmap='viridis')

#     # Show the 3D plot
#     plt.show()

# # Example usage
# convert_to_3d('2d_Avatar.png')



# Greyscale 3D plot

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D


# def convert_to_3d(image_path):
#     # Read the 2D image
#     img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#     # Create a 3D meshgrid
#     x = np.arange(0, img.shape[1], 1)
#     y = np.arange(0, img.shape[0], 1)
#     x, y = np.meshgrid(x, y)

#     # Normalize pixel values to the range [0, 1]
#     z = img / 255.0

#     # Create a 3D plot without using scatter
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot_wireframe(x, y, z, cmap='viridis', linewidth=0.5)

#     # Show the 3D plot
#     plt.show()

# # Example usage
# convert_to_3d('2d_Avatar.png')


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
