# Installations and imports
import os
import tarfile

import numpy as np
import pandas as pd
import seaborn as sns
import nibabel as nb
import matplotlib.pyplot as plt

from sklearn.decomposition import FastICA

# ------------------------------------------------------------------------------------------------

# Accessing the timeseries data and creating the numpy array of subjectID-ROI-timeseries

# Subject IDs
subjectIDs = np.loadtxt("E:\HCP_1200\HCP1200_Parcellation_Timeseries_Netmats\HCP_PTN1200\subjectIDs.txt", dtype = int)
ID_count = len(subjectIDs)
print(subjectIDs)

# Parcels
parcels = 0 # will be replaced
parcel_count = 360 # will be replaced

# Time series
timeSeries = 0 # will be replaced
timeSeries_count = 10 # will be replaced

# ------------------------------------------------------------------------------------------------

# Creating the numpy array for the "raw" data

# Empty Array (subjects, parcels, timeseries)
HCP_TimeSeries_raw_Array = np.zeros((ID_count, parcel_count, timeSeries_count))

# Insert values into the array
### IDs
for i, sIDs in enumerate(subjectIDs):
    HCP_TimeSeries_raw_Array[i, 0, 0] = sIDs
### Parcels
# Parcel codes will be inserted here.
### TimeSeries
# Time series codes will be inserted here.

# Save the array
np.save("NMA-ISP\HCP_TimeSeries_raw_Array.npy", HCP_TimeSeries_raw_Array)
print(HCP_TimeSeries_raw_Array)