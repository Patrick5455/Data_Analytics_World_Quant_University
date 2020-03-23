import pandas as pd
import numpy as np
from string import ascii_letters, digits
import datetime
import csv

usernames = ['alices36', 'bob_smith', 'eve']
passswords = [''.join(np.random.choice(list(ascii_letters+digits),8)) for x in range(3)]
emails = ['pat@gmail.com', 'bat@gmail.com', 'cat@gmail.com']
creation_dates = [datetime.datetime.now().date() - datetime.timedelta(int(x)) for  x in np.random.randint(0,1500,3)]

df = pd.DataFrame({'Username': usernames, 'Password': passswords, 'Creation Date': pd.to_datetime(creation_dates)})
#print(df)
# alternatively
df_alt = pd.DataFrame((list(zip(usernames, emails, passswords, creation_dates))), columns= ['Username', 'Email', 'Password',
                                                                                            'Date'])

print(df_alt, end='\n\n')

# adding a new row using the loc method
df_alt.loc[3]=['Chinedu', 'chi@gmail.com','1776tyiS', '2019-02-21']
print(df_alt)

#adding a new column
ages = []
df_alt['Age'] =  [np.random.choice([20*x+5 for x in range(1,len(df_alt))])  for i in range(len(df_alt))]
print(df_alt, end='\n\n')

# removing a row
df_alt.drop(3, inplace=True) # no need to specify axis
print(df_alt, end='\n\n')

# removing a column
df_alt.drop('Age', axis=1, inplace=True) # specify axis
print(df_alt, end='\n\n')

# giving index useful names after creation of dataframe
df_alt.set_index('Username', inplace=True)
df_alt.index.name = 'users'
print(df_alt, end='\n\n')

# giving index useful names before creation of dataframe
df = pd.DataFrame({'Username': usernames, 'Password': passswords, 'Creation Date': pd.to_datetime(creation_dates)},
                  index=usernames)
df.index.name = 'users'
print(df, end='\n\n')
print(df.dtypes, end='\n\n')

#reset index
df.reset_index(inplace=True)
df_alt.reset_index(inplace=True)
print(df, end='\n\n')

#multiple indexing
df_alt.set_index('users', 'Email', inplace=True)
print(df_alt, end='\n\n')
#users and email are no longer part of the columns
print(df_alt.dtypes, end='\n\n')

# python indexing is very useful for certain kinds of calculation
series_a = pd.Series ({'a':1, 'b':2, 'c':3 })
series_b = pd.Series ({'c':1, 'b':2, 'a':3 })

print(series_a, end='\n\n')
print(series_b, end='\n\n')

print(series_a+series_b)


# Reading data from file We can also construct a DataFrame using data stored in a file or recieved from a website.
# The data source might be JSON, HTML, CSV, Excel, Python, Pickle, or evem a database connection. Each format will
# have its own method for reading and writing data that take different arguments. The arguments of these methods
# usually depend on the particular formatting of the file. For example, the values in a CSV might be separated by
# commas, or semi-colon. It might have a header or it might not.

# with open ('./Data/csv_sample.txt', 'r') as f:
#     print(f.read())

with open('./pandas_data/FL_insurance_sample.csv','r') as f:
    print(f.read())


