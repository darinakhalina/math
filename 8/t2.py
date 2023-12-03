import pandas as pd
import numpy as np
from scipy.stats import pearsonr

x = np.array([113,114,106,108,120,104,116,112,110,118,103,120])
y = np.array([10,15,20,15,24,11,20,20,18,24,14,27])
corr, _ = pearsonr(x, y)
print('Критерій кореляції пірсона: %.3f' % corr)