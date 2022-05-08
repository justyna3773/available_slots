import os
import glob
from time import time
import numpy as np
import pandas as pd
from datetime import datetime
import datetime as dt
path = "./"

availabilities = []
all_availabilities = {}
for filename in glob.glob(os.path.join(path, '*.txt')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        availabilities = f.readlines()
        final_availabilities = []
        for line in availabilities:
            line = line.strip()
            line_processed = list((line.strip()).split(" "))
            line_processed.remove('-')
            line_processed = [
                x+' '+y for x, y in zip(line_processed[0::2], line_processed[1::2])]
            line_processed[0] = datetime.strptime(
                line_processed[0], "%Y-%m-%d %H:%M:%S")
            line_processed[1] = datetime.strptime(
                line_processed[1], "%Y-%m-%d %H:%M:%S")
            line_processed.append(filename)

            final_availabilities.append(line_processed)
        #all_availabilities[filename] = final_availabilities


print(final_availabilities)


def find_common_times(time_window, n_people, all_availabilities):
    # calculating time window to see which time windows do not meet the requirements
    all_df = pd.DataFrame(
        all_availabilities, columns=['Start', 'Stop', 'Filename'])
    all_df['Duration'] = all_df['Stop'] - all_df['Start']
    all_df['Duration'] = all_df['Duration'].dt.total_seconds()
    # eliminate all time windows which do not meet basic requirements
    new_df = all_df.loc[all_df['Duration'] > time_window]
    new_df = new_df.sort_values(by=['Start'])
    print(new_df)

    return new_df


print(find_common_times(2000.0, 1, final_availabilities))
