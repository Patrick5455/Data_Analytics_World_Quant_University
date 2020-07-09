# pickle file is a very important file format unique to python.
# a pickle file is an exmaple of what is claled serilaization.  often in prigramming language, we may be working with complex objects that are stored in memory but we may need to transfer this object form comoputer to another. Or we may simply need to persist those objects to disk so we can shut down our interpreter and then work iwth them again in a future interpreter session.
# An example of this is if we are working with a machine leaarning model. that we have spend  a long time training on some training data. We may want ot serialize it to disk so we can load it in and mae predictions oin the future or perform additionla trianing. Or we may want to serialize it to send it to a number of different computers servinf web applications where this model will be used to make predictions that ysers of the web app will eventually see.

#

#
pickle_example = ['hello', {'a': 23, 'b': True}, (1, 2, 3), [['dogs', 'cats'], None]]

# # we can't save this as text
# with open('./Data/pickle_example.txt', 'w') as f:
#     f.write(pickle_example)


import pickle

# we can save it as a pickle
with open('./Data/pickle_example.pkl', 'wb') as f:
    pickle.dump(pickle_example, f)

with open('./Data/pickle_example.pkl', 'rb') as f:
    reloaded_example = pickle.load(f)

print(reloaded_example == pickle_example)
