import pandas as pd

x = pd.DataFrame({'a': [1, 2, 3, ], 'b': [4, 5, 6, ], 'c': [7, 8, 9]})
print(x)


class User(object):
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def parse(self, text):
        # parse the text
        user = User(self.name, self.username, self.password)
        return user


class Record(object):
    def __init__(self, posttype, text):
        self.posttype = posttype
        self.text = text

    def parse(self, text):
        # parse the text
        record = Record()
        return record


import numpy as np

y = np.array([[[123],[4567],[789]]])+6

print(y)
