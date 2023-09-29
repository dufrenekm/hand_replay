import pickle as pkl 
import os
import pandas as pd
# "/media/kyle/16ABA159083CA32B/kyle/live/2v2/1.1_1.1_1.1/N_2v2_1.1_1.1_1.1.pkl"
path_to = os.path.abspath(os.path.dirname(__file__))
# "/media/kyle/16ABA159083CA32B/kyle/replay/3v3_50.0.25.0.25.0_40.0.35.0.25.0_1.1_540/N_3v3_50.0.25.0.25.0_40.0.35.0.25.0_1.1_540.pkl"
file_path = os.path.join(path_to, "replay_data/N_2v2_50.50_50.50_1.1_63.pkl")

with open('test.pkl', 'rb') as f:
    data = pkl.load(f)
    print("hi")

df = pd.read_pickle(file_path)
#print(df[0:156])
print("here")
new_df = df[0:156]#.to_pickle('test.pkl')




with open('test.pkl', 'wb') as handle:
    pkl.dump(new_df, handle)