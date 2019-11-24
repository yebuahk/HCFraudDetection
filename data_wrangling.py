"""
kevin Yebuah 11/23/19
detect provider fraud
"""

import numpy as np
import pandas as pd
import datetime
from scipy import stats

import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 150)

from itertools import cycle
from collections import Counter