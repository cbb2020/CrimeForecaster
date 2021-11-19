import numpy as np

cpath = '/opt/shared/PyCharmProjects/CrimeForecaster/Code/CrimeForecaster/CRIME-LA/8/'
file = cpath + 'test.npz'
data = np.load(file)
print(data.files)
print(data['x'].shape)
# print(data['x'][0])
print(data['y'].shape)
# print(data['y'][0])