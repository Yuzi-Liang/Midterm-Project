import numpy as np
from datetime import *

def dateConvert(date_frame):
    """
    Convert the original date to time difference to 2014.05.01
    """
    date_frame = np.array(date_frame)

    date0 = datetime.strptime('20140501', "%Y%m%d")
    for i in range(0, len(date_frame)):
        # print(type(date_frame[i]))
        # print(type(date0))
        date_frame[i] = datetime.strptime(date_frame[i], "%Y%m%dT000000") - date0
        date_frame[i] = date_frame[i].days
    return date_frame.astype(float)


def renovatedTime(sale_date, yr_built, yr_renovated):
    output = np.array([0] * len(sale_date))
    sale_date = np.array(sale_date)
    yr_built = np.array(yr_built)
    yr_renovated = np.array(yr_renovated)
    for i in range(0, len(sale_date)):
        if yr_renovated[i] != 0:
            temp = datetime.strptime(str(yr_renovated[i]), "%Y")
            output[i] = (datetime.strptime(str(sale_date[i]), "%Y%m%dT000000") - temp).days
        else:
            temp = datetime.strptime(str(yr_built[i]), "%Y")
            output[i] = (datetime.strptime(str(sale_date[i]), "%Y%m%dT000000") - temp).days
    return output.astype(float)

def isRenovated(yr_renovated):
    output = np.array([0] * len(yr_renovated))
    for i in range(0, len(yr_renovated)):
        if yr_renovated[i] != 0:
            output[i] = '0'
        else:
            output[i] = '1'
    return output.astype(int)