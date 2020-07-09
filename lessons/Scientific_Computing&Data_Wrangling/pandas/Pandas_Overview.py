# Pandas is a package for working with tabular data.
# A Dataframe is essentially a dictionary of data series.
# The DataFrane has an index given by the union of indices of its constittuent Series Since a DataFrame is a dict of
# Series.

# Understanding the structure of the DataFrame object as a dict of Series will help you avoid errors and
# help you think about how the DataFrame should behave when we begin doing more complicated analysis



import pandas as pd
import gzip
import simplejson as json

with gzip.open('./pandas_data/yelp.json.gz', 'r') as f:
    yelp_data = [json.loads(line) for line in f]

print(yelp_data[:5], end='\n\n')
# json is often used to represent data that is not easily represented by a table.
# Hence when we load this json file to a DataFrame, the presentation would not be as that of a typical table.
# DataFrame is not perfectly fit for data that is not flat.
yelp_df = pd.DataFrame(yelp_data)
print('Data From yelp:\n', yelp_df.head(), end='\n\n')

print('NAMES:\n', yelp_df['name'], end='\n\n')

# A datframe works similiar with a dictionary, we slice data using columns/series as keys.
# And when we attepmpt to slice data with a column/series not present in our DataFrame, we get a key error.

print(yelp_df['name'].head(), end='\n\n')

# We can check the data types of our series or column.

print('Various data types of our DataFrame Series', yelp_df.dtypes, end='\n\n')
# object is a catchall name to refer to any datType that takes an amount of block of memory we are not sure e.g list
# object dataType could refer to a data structure like dict, list, set.

# if it were a date series, we would have a datTime object.
from datetime import datetime

print(pd.Series([datetime.now(), datetime.now()]))

# An individual column is a Pandas Series. A Series has a name and a dtype (similiar to NumPy array).
# A DataFrame is essentially a dict of Series objects. The Series has an index attribute, which label the rows.
# The index is essentially a set of keys for referencing the rows.
# We can have an index composed of numbers, strings, timestamps, or any hashable Python object.
# The index will also have homogeneous type.

print(yelp_df['city'].index == yelp_df.index)

#  We can select a column and then a row using square bracket notation [column][row], but not the reverse([
# # row] [column]). This is becuase the DataFrane is a dictionary of series not a dictionary of rows.

print('Proper column and row access in a DataFrame:\n', yelp_df['city'][100], end='\n\n')

try:
    print(yelp_df[100]['city'], end='\n\n')

except:
    print("Improper access of rows and columns", end='\n\n')

# We first need to pull out a series before we can pull out a row however the loc method works around this. With the
# loc method, # we can access the hel  row first before accessing the column.

print('Accessing row first using the loc method:\n', yelp_df.loc[100, 'city'], end='\n\n')
# When using loc method we are obliged to specify a row # but it is optional to specify a column
print('Accessing row first using the loc method:\n', yelp_df.loc[100], end='\n\n')
print('Accessing row first using the loc method:\n', yelp_df.loc[100:101], end='\n\n')


# We can aggregate data ina DataFrame using methods like mean, sum, count, and std.
# To view a collection of summary statistics, we can use the describe method,

# The utility of a DataFrame comes from its ability to split data into groups, using the groupby method,
# and then perorm custom aggregation using the apply or aggregate method. This process of splitting data inito
# groups, applying an aggregation, and then collecting the result is well expalined in the Pandas Documentation.