# COMP4471_2020Fall

Team Member: HUANG, Qiucan; CHEN, Sida; LIN, Yifei

**What is the problem that you will be investigating? Why is it interesting?**

**What reading will you examine to provide context and background?**
The link following is some paper we found about Autonomous Vehicles. Most of them are reviews of this field which can provide enough background. Others focus on the prediction and postures estimation which is the target of our project.

[Computer Vision for Autonomous Vehicles: Problems, Datasets and State of Art](https://arxiv.org/pdf/1704.05519.pdf)  
[Self-Driving Cars: A Survey](https://arxiv.org/pdf/1901.04407.pdf)  
[A Review of Tracking, Prediction and Decision Making Methods for Autonomous Driving](https://arxiv.org/pdf/1909.07707.pdf)  
[Human Motion Trajectory Prediction: A Survey](https://arxiv.org/pdf/1905.06113.pdf)  
[Deep Learning-based Vehicle Behaviour Prediction For Autonomous Driving Applications: A Review](https://arxiv.org/pdf/1912.11676.pdf)  

**What data will you use? If you are collecting new data, how will you do it?**
We will use the dataset provided [here](https://www.kaggle.com/c/lyft-motion-prediction-autonomous-vehicles/data)

**What method or algorithm are you proposing? If there are existing implementations, will you use them and how? How do you plan to improve or modify such implementations? You don't have to have an exact answer at this point, but you should have a general sense of how you will approach the problem you are working on.**

We don't have exact idea about what method or algorithm we will used.
But according to our experience, to predict the motion of an object in video, we usually use EKF(Extend Kalman Filter) and Optical Flow to estimate the motion. Here we may try this traditional method and the [baseline model](https://www.kaggle.com/pestipeti/pytorch-baseline-train) provided by Lyft first.

**How will you evaluate your results? Qualitatively, what kind of results do you expect (e.g. plots or figures)? Quantitatively, what kind of analysis will you use to evaluate and/or compare your results (e.g. what performance metrics or statistical tests)?**
