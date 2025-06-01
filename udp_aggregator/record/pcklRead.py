import pickle

# File paths
pickle_file = 'recorded-2025-05-08-18:40:49.pckl'  # Replace with your pickle file path
output_txt = 'output.txt'     # Replace with desired output text file path

try:
    # Read the pickle file
    with open(pickle_file, 'rb') as file:
        data = pickle.load(file)
    
    # Save contents to text file
    with open(output_txt, 'w', encoding='utf-8') as file:
        # Convert data to string and write
        file.write(str(data))
    
    print(f"Successfully read {pickle_file} and saved to {output_txt}")

except FileNotFoundError:
    print(f"Error: The file {pickle_file} was not found")
except pickle.UnpicklingError:
    print("Error: Failed to unpickle the file. It may be corrupted")
except Exception as e:
    print(f"An error occurred: {str(e)}")