import pandas as pd
import numpy as np


# In a table like pandas Dataframe, each row is analogous to an object and the column in each row
# can be said to be the attribute of the object(row).

def gen_football_team(n_players, mean_shoe, mean_jersey):
    shoe_sizes = np.random.normal(size=n_players, loc=mean_shoe, scale=.15 * mean_shoe)
    jersey_sizes = mean_jersey / mean_shoe * shoe_sizes + np.random.normal(size=n_players, scale=.05 * mean_jersey)

    return shoe_sizes, jersey_sizes


players = ['Ronaldinho', 'Pele', 'Lionel Messi', 'Zinedine Zidane', 'Didier Drogba', 'Ronaldo', 'Yaya Toure',
           'Frank Rijkaard', 'Diego Maradona', 'Mohamed Aboutrika', "Samuel Eto'o", 'George Best', 'George Weah',
           'Roberto Donadoni']

shoes, jerseys = gen_football_team(len(players), 10, 100)

df = pd.DataFrame({'shoe_size': shoes, 'jersey_size': jerseys}, index=players)

print('All The Dataframe:\n', df, end='\n\n')

# The columns are sort of key to the dataframe. Hence we can slice column series from the DataFrame
print( 'Shoe Size Data Series:\n', (df['shoe_size']), end='\n\n')
print('Forloop Print for Jersey Size:\n')
print([i for i in df['jersey_size']], end='\n\n')

# The output of printing the column above is known as a pandas series.
# There is a pandas dataFrame object(ROWS & COLUMNS)
# There is also a  pandas  series object (A SINGLE COLUMN)

# check the type to confirm it is a pandas series
print('Confirm column is a series in pandas:\n')
print(type(df['shoe_size']), end='\n\n')

# since data series are built on numPy array, we can easily use some numPy functions on them.
print("Logarithm function applied:\n", np.log(df), end='\n\n')

print('mean function applied:\n', df.mean(), end='\n\n')
# in contrast with numPy, does not calculate the mean for all the values. It only calculates
# the mean of each series (columns)

# to retrieve rows by name, we use loc method of DataFrame.
print('Ronaldinho:\n', df.loc['Ronaldinho'], end='\n\n')
# loc is very flexible, we can retrieve rows for a column
print('Ronaldinho and George Best by Shoe Size:\n', df.loc[['Ronaldinho', 'George Best'], 'shoe_size',], end='\n\n')
print('Ronaldinho to George Best:\n', df.loc['Ronaldinho': 'George Best', 'shoe_size'], end='\n\n')

# position based indexing; we simplu use iloc
print('Range 0 - 5:\n', df.iloc[:5], end='\n\n')
print('Range 2 - 4:\n', df.iloc[2:4, 0], end='\n\n')

# head and tail slicing
print('Head of dataFrame\n', df.head(), end='\n\n')  # first five rows
print('Tail of dataFrame\n', df.tail(), end='\n\n')  # last five rows

# we can increase the number of heads and tails
print('Head of dataFrame (7) \n', df.head(7), end='\n\n')  # increased to seven
print('Tail of dataFrame (8) \n', df.tail(8), end='\n\n')  # increased to eight

# adding a new column
print("Adding a new Column:\n")
x = df['position'] = np.random.choice(['goaltender', 'defense', 'midefield', 'attack'])
print(df['position'], end='\n\n')

# adding a new row
print('Adding a new row:\n')
y = df.loc['Dylan'] = {'jersey_size': 10, 'shoe_size':9, 'position': 'midfield'}
print(df.loc['Dylan'])

print('All The Dataframe:\n', df, end='\n\n')

# remove elements from the dataFrame
print('Dropping row Dylan:\n',df.drop('Dylan'), end='\n\n') # row
# drop a column
print('Dropping column Position:\n',df.drop('position', axis=1), end='\n\n')

# Notice when we executed df.drop('position, axis=1'), there was an entry for Dylan even though we had just executed
# df.drop('Dylan'). We have to be careful using drop: many DataFrame functions return a copy of the DataFrame. In
# order to make the change permanent, we either need to reassign df to the copy returned by df.drop() or we have to
# use the keyword inplace

# using reassignment
df = df.drop('Dylan')
print('Permanent Drop - Row Dylan:\n', df, end='\n\n')

# using inplace = True
print('Permanent drop - Column position:', end='\n')
print(df.drop('position', axis=1, inplace=True), end='\n\n')


print("All The DataFrame (Column position and Row Dylan absent)\n", df, end='\n\n')

print(pd.__version__)

