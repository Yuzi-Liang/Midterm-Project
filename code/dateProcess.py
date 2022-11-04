import pandas as pd
import numpy as np
from datetime import *

def dateConvert(date_frame):
    """
    Convert the original date to time difference to 2014.05.01
    """
    date_frame = np.array(date_frame)
    date0 = datetime.strptime('20140501', "%Y%m%d")
    for i in range(0, len(date_frame)):
        date_frame[i] = datetime.strptime(date_frame[i], "%Y%m%dT000000") - date0
        date_frame[i] = date_frame[i].days
    return date_frame.astype(float)