<div style="width: 100%;">
    <a href="#"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/SVGsHeader/driverDrowsinessDetection.svg" alt="Class Schedules" style="width: 100%"></a>
</div>
<br>

<div align = "center">

This project was developed as part of ENSE-412, a Machine Learning course within my engineering degree program. The Driver Drowsiness Detection System showcases the application of skills and knowledge acquired through my studies, reflecting a comprehensive approach to enhancing road safety by addressing the critical issue of driver fatigue.

</div>

<br>
<div style="width: 100%;">
    <a href="#"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/BrownSVGs/overview.svg" alt="Overview" style="width: 100%"></a>
</div>
<br>

This repository contains all the necessary components of the Driver Drowsiness Detection. This project aimed to  enhancing road safety by identifying signs of driver fatigue through image analysis. Utilizing machine learning algorithms and deep learning techniques, this system detects key fatigue indicators such as closed eyes and yawning.

<br>
<div style="width: 100%;">
    <a href="#"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/BrownSVGs/demo.svg" alt="Demo" style="width: 100%"></a>
</div>
<br>

<div align="center">
    <a href="#"><img src="Assets/DemoGif/driverDrowsinessDetection.gif" alt="Demo Gif"></a>
</div>

<br>
<div style="width: 100%;">
    <a href="#"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/BrownSVGs/technologiesUsed.svg" alt="Technologies Used" style="width: 100%"></a>
</div>
<br>

<h2 align = "center">Languages</h2>

<div align="center">
<table>
  <tr>
    <td>
      <a href="https://www.w3schools.com/python/"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/Badges/Languages/Middle/python.svg" alt="Python"></a>
    </td>
  </tr>
</table>
</div>

<h2 align = "center">Libraries and Frameworks</h2>

<div align = "center">
<table>
  <tr>
    <td>
      <a href="https://pandas.pydata.org/"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/Badges/MachineLearning/Left/pandas.svg" alt="Pandas"></a>
      <br>
      <a href="https://www.tensorflow.org/"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/Badges/MachineLearning/Left/tensorflow.svg" alt="Tensorflow"></a>
    </td>
    <td>
      <a href="https://numpy.org/"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/Badges/MachineLearning/Middle/numpy.svg" alt="Numpy"></a>
      <br>
      <a href="https://keras.io/"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/Badges/MachineLearning/Middle/keras.svg" alt="Keras"></a>
    </td>
    <td>
      <a href="https://matplotlib.org/"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/Badges/MachineLearning/Right/matplotlib.svg" alt="Matplotlib"></a>
      <br>
      <a href="https://pytorch.org/"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/Badges/MachineLearning/Right/pytorch.svg" alt="Pytorch">
    </td>
  </tr>
</table>
</div>

<br>
<div style="width: 100%;">
    <a href="#"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/BrownSVGs/contents.svg" alt="Contents" style="width: 100%"></a>
</div>
<br>

- <b>DriverDrowsinessDetection.ipynb:</b> Jupyter notebook detailing the model development process, including the exploration of machine learning algorithms like Random Forest, K-Nearest Neighbor (KNN), and Decision Trees, culminating in the implementation of a Convolutional Neural Network (CNN) using the VGG16 architecture.
- <b>model.h5:</b> The saved final CNN model that can be used for making predictions.
- <b>index.html and app.py:</b> Files constituting a Flask web application for local demonstration of the project, which was used to as a demo in the class presentation.
- <b>requirements.txt:</b> A list of Python libraries required to run the local demo.

<br>
<div style="width: 100%;">
    <a href="#"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/BrownSVGs/modelDetails.svg" alt="Model Details" style="width: 100%"></a>
</div>
<br>

The final model utilizes the VGG16 architecture as a feature extractor. The pre-trained VGG16 model was employed to capture complex features from the images, which was then used by custom layers to perform classification. This approach leverages the powerful feature detection capabilities of VGG16 without additional training on my part.

