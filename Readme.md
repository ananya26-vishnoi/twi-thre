# 3D Surface Plot with Plotly

This Python script generates a 3D surface plot using Plotly with a sample 2D image. The script utilizes the `plotly.graph_objects` library to create a meshgrid and visualize the image in 3D space.

## Prerequisites

Make sure you have the required libraries installed. You can install them using the following:

```
pip install plotly numpy Pillow
```

## Usage
1. Replace 'Bgrem_drawing.png' with the actual path to your image in the image_path variable.
2. Run the script.
```
python your_script_name.py
```

## Sample Image
The script loads a sample 2D image and converts it to grayscale. You can replace it with your own image for visualization.
<hr>

This is the 2d image.
<img src="./2d_Avatar.png">
This is a 3D image which is generated after the converter.
<img src="./3d image.png">
<img src="./3d image 2.png">


## Dependencies
Plotly
NumPy
Pillow (PIL Fork)
Acknowledgments
Plotly for providing a powerful graphing library.
NumPy for numerical computing in Python.
Pillow (PIL Fork) for image processing.