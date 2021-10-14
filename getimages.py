import numpy as np
import pandas as pd
import wget

df = pd.read_csv("kjacob-challenge-filenames.csv", header=None)
names = np.array(df.iloc[:, 0])
url = 'https://cs7ns1.scss.tcd.ie/2122/kjacob/pi-project2/'

# play=[]
# for i in range(10):
#   play.append(names[i])
#
# print(len(play))

print('Beginning file download with wget module')
try:
    for j in range(len(names)):
        wget.download(url + names[j], 'test/')

except Exception as exc:
    print('Exception details ' + str(exc) + ' Name of file= ' + names[j])
