<div style="width: 100%;">
    <a href="#"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/SVGsHeader/driverDrowsinessDetection.svg" alt="Class Schedules" style="width: 100%"></a>
</div>
<br>

<div align = "center">

This project was developed as part of ENSE-412, a Machine Learning course within my engineering degree program. The Driver Drowsiness Detection System showcases the application of skills and knowledge acquired through my studies, reflecting a comprehensive approach to enhancing road safety by addressing the critical issue of driver fatigue.

</div>
<br>
<div style="width: 100%;">
    <a href="#"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/BrownSVGs/demo.svg" alt="Demo" style="width: 100%"></a>
</div>
<br>

<div align="center">
  <img src="Assets/DemoGif/driverDrowsinessDetection.gif" alt="Demo Gif">
</div>

<br>
<div style="width: 100%;">
    <a href="#"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/BrownSVGs/overview.svg" alt="Overview" style="width: 100%"></a>
</div>
<br>

This repository contains all the necessary components of the Driver Drowsiness Detection. This project aimed to  enhancing road safety by identifying signs of driver fatigue through image analysis. Utilizing machine learning algorithms and deep learning techniques, this system detects key fatigue indicators such as closed eyes and yawning.

<br>
<div style="width: 100%;">
    <a href="#"><img src="https://raw.githubusercontent.com/ferasaljoudi/AssetsRepository/main/BrownSVGs/technologiesUsed.svg" alt="Technologies Used" style="width: 100%"></a>
</div>
<br>

<div align = "center">

  [![Python](https://img.shields.io/badge/-Python-1076AB?style=for-the-badge&logo=python&logoColor=F7DF1E)](https://www.w3schools.com/python/)
  [![TensorFlow](https://img.shields.io/badge/-TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
  [![Keras](https://img.shields.io/badge/-Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io/)
  [![NumPy](https://img.shields.io/badge/-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
  [![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=for-the-badge&logo=Matplotlib&logoColor=white)](https://matplotlib.org/)
  [![Pandas](https://img.shields.io/badge/-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

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

