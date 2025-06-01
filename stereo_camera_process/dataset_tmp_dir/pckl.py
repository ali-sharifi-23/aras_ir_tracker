import pickle

# Load the pickle file
file_path = 'seq_8.pckl'

with open(file_path, 'rb') as file:
    data = pickle.load(file)

print(data)
with open('output.txt', 'w') as f:
    f.write(str(data))
