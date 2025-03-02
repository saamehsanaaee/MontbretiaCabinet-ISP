# Working Memory Architecture and Demand Model
This project is the result of work from the **Montbretia Cabinet** team during the Neuromatch Academy [Computational Neuroscience Course](https://compneuro.neuromatch.io/) and the Neuromatch Academy [Impact Scholars Program](https://impact-scholars.neuromatch.io/).

## Project Summary
(Abstract)

---

## Data
Main providers of our data have been the Human Connectome Project (HCP) and Neuromatch Academy (NMA).

We are using the HCP data subset that NMA has provided during the NMA Computational Neuroscience (CN) 2024 course. The data is a 100-subject subset of the original HCP young adult. The data subset is accessible in [Neuromatch OSF page](https://osf.io/hygbm/) and downloadable through codes provided in the [computational neuroscience course content](https://compneuro.neuromatch.io/projects/fMRI/README.html#:~:text=HCP%20task%20datasets,Murray%2C%20Saad%20Jbabdi) from NMA.
## Models
We created three different models.

The Working Memory Demand (WMD) model, a Multilayer Perceptron, was created during the NMA CN course in the summer of 2024 as our preliminary (or proof of concept) model. Entering the Impact Scholars Program (ISP), we then expanded this model to create an "improved" model, called Working Memory Architecture and Demand (WMAD) model. WMAD is comprised of two models, one is a (deep learning) GNN-LSTM model, and the other is a (statistical) GLM model.

The GNN-LSTM model has two purposes. First, it can act as the demand "sensor", just like WMD and predict demand of tasks when it recieves parcel-based BOLD signals. Second, it can identify significant WM parcels that contribute the most to WM function.

The GLM model looks at temporal WM activity data. It shows us when and where the WM activity is present, giving a temporal "map" of how WM information travels through the brain.

Combined, these two models give us insight into temporal and spatial activity of working memory and how it's structured while still fulfilling the role of a "task demand sensor".
### WMD (Preliminary) Model
### WMAD Model
#### GNN and LSTM
#### GLM
## Model Interpretation
### WM Architecture
### WM Demand
## Generalization of WMAD
### Presenting Emotion and Language Data to the Model

## Acknowledgements
Data were provided in part by the Human Connectome Project, WU-Minn Consortium (Principal Investigators: David Van Essen and Kamil Ugurbil; 1U54MH091657) funded by the 16 NIH Institutes and Centers that support the NIH Blueprint for Neuroscience Research; and by the McDonnell Center for Systems Neuroscience at Washington University.
In addition, we thank Neuromatch Academy and the Open Science Foundation for providing the HCP 100-subject data subset for this project.
Finally, we thank Linzan Liu and Matin Yousefabadi for their support, mentorship, and advising during the NMA CN course during the summer of 2024.
