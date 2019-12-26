import pickle, pprint

f = open('./test_file', 'rb')
pprint.pprint(pickle.load(f))

f.close()
