import pickle
with open('basicModel_neutral_lbs_10_207_0_v1.0.0.pkl', 'rb') as f:
    data = pickle.load(f, encoding='latin1')
with open('basicModel_python3.pkl', 'wb') as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
