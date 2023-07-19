# Image-Manipulation-Detection

**Introduction**

Image manipulation detection is a crucial area of research and development in the field of computer vision and digital forensics. The primary objective of this project is to create a comprehensive solution for detecting various types of image manipulations. The task is divided into two phases: Phase 1 involves type prediction, and Phase 2 involves mask prediction. The repository contains the necessary code, models, and data files to perform these predictions successfully.

**Why Image Manipulation Detection is Important?**

In today's digital age, images play a significant role in various domains, including media, social networking, journalism, and law enforcement. With the increasing accessibility of sophisticated image editing tools, the risk of image manipulation and forgery has grown substantially. Identifying manipulated images is essential for the following reasons:

**Preserving Authenticity**: 

n many applications, it is crucial to ensure that images are authentic and have not been altered maliciously or unintentionally. This is especially important in forensic investigations, journalism, and legal proceedings.

**Misinformation Detection:**

With the prevalence of fake news and misinformation, detecting manipulated images is essential in preventing the spread of false information and maintaining trust in media sources.

Security and Privacy: Manipulated images can be used to deceive people, perpetrate fraud, or compromise privacy. Detecting such manipulations is vital for safeguarding individuals and organizations.

Intellectual Property Protection: Image manipulation can be used to infringe upon the copyrights and intellectual property rights of creators. Detection helps in preserving the rights of content creators.

**Types to Predict**

The project focuses on predicting three main types of image manipulations:

**Authentic (Real)**: Authentic images are unaltered and considered genuine. These are images that have not undergone any malicious or deceptive manipulations.

**Copy-Moved**: Copy-moved image manipulation involves duplicating a region from one part of an image and pasting it onto another part, effectively creating a clone-like effect. This type of manipulation is commonly used to conceal or duplicate objects within an image.

**Spliced**: Splicing manipulation involves combining multiple parts of different images to create a new composite image. This type of manipulation is often used to create hoaxes or composite images with false context.

**Repository Structure**

The repository is structured as follows:

phase1/: Contains the code, Jupyter Notebook (phase1.ipynb), JSON, and .h5 files related to the type prediction phase.
phase2/: Contains the code, Jupyter Notebooks (phase2_copy_move.ipynb, phase2_splice.ipynb), JSON, and .h5 files related to the mask prediction phase.
flask_app/: Includes the code for deploying the image manipulation detection visually using Flask, HTML, and CSS.

**Predicted Outputs**

real for a_0001

<img width="960" alt="image" src="https://github.com/Grunt-prog/Image-Manipulation-Detection/assets/86661317/34413e1c-de9c-48e3-a5b3-19e7526872f5">

real for a_0005

<img width="960" alt="image" src="https://github.com/Grunt-prog/Image-Manipulation-Detection/assets/86661317/77491e48-2c43-4388-904d-417b0ccb5688">

Copy-moved for c_0015

<img width="960" alt="image" src="https://github.com/Grunt-prog/Image-Manipulation-Detection/assets/86661317/bc349d42-aba7-4dd0-92dc-94df2e5a19b9">

Copy-moved for c_0023

<img width="960" alt="image" src="https://github.com/Grunt-prog/Image-Manipulation-Detection/assets/86661317/bc349d42-aba7-4dd0-92dc-94df2e5a19b9">

spliced for s_0022

<img width="960" alt="image" src="https://github.com/Grunt-prog/Image-Manipulation-Detection/assets/86661317/4de9cae5-e034-42fd-89f8-522aa64f2112">

spliced for s_0031

<img width="960" alt="image" src="https://github.com/Grunt-prog/Image-Manipulation-Detection/assets/86661317/7237cf70-0919-4425-9439-b2d0707faa7b">

**Conclusion**
Detecting image manipulation is an essential aspect of ensuring authenticity, preventing misinformation, and protecting intellectual property rights.

**References**

Research Paper - "https://www.researchgate.net/publication/332561655_Image_forgery_detection_using_error_level_analysis_and_deep_learning"




