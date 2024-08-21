import pickle

# Load the pickle file
file_path = 'recorded-2024-08-20-18:07:37.pckl'

with open(file_path, 'rb') as file:
    data = pickle.load(file)

print(data)
