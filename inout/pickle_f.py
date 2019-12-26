import pickle
dict_1 = {'a':1, 'b':2}

f = open('./test_file', 'wb')

pickle.dump(dict_1, f)

f.close()
