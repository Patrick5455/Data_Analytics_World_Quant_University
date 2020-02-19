import pandas as pd
import numpy as np

arrays = {'Patrick' : [23, 'Semicolon', 1997], 'Mayowa': [21,'Unilag', 1999],
          'Bolu': [19, 'Waec', 2002]}

arrays = pd.DataFrame(arrays, index = ('Age', 'Education', 'D.O.B'))
print(pd.DataFrame(arrays, index = ('Age', 'Education', 'D.O.B')))

arraysFrame = pd.DataFrame(arrays)
print(type(arraysFrame))
print('Patrick:', end='\n')
print(arraysFrame['Patrick'])
print(type(arraysFrame['Patrick']))

print(arraysFrame.mean())

# retrieving row using  'loc'
print(arraysFrame.loc['Education', 'Patrick']) # retrieve the column of a row
print(arraysFrame.loc['Education']) # retrive only the row

# position based indexing
print(arraysFrame.iloc[:1])

# view toop of the dataframe
print(arraysFrame.head())
print(arraysFrame.tail())

#add a new column
arraysFrame['position'] = np.random.choice(["1st", "2nd", "3rd"], size=len(arraysFrame))
print(arraysFrame)
print(arraysFrame.loc['Education'])

#delete a row, we can use the drop method

arraysFrame.drop('Age')
print(arraysFrame)

# delate a column
arraysFrame.drop('position', axis=1, inplace = True)
print(arraysFrame)