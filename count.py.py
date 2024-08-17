from collections import defaultdict
import string
import os

def word_count(file_path):
    # Ensure the provided path is a file
    if not os.path.isfile(file_path):
        raise ValueError("The specified path is not a file. Please provide a valid file path.")
    
    # Create a dictionary to hold the word counts
    word_counts = defaultdict(int)

    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Remove punctuation and convert to lowercase
            line = line.translate(str.maketrans('', '', string.punctuation)).lower()
            words = line.split()

            # Count each word
            for word in words:
                word_counts[word] += 1

    return word_counts

def display_word_counts(word_counts):
    # Display the word counts sorted by occurrence
    for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
        print(f'{word}: {count}')

if __name__ == "__main__":
    file_path = input("Enter the path to your text file (e.g., E:\\task 1\\myfile.txt): ")
    try:
        word_counts = word_count(file_path)
        display_word_counts(word_counts)
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except PermissionError:
        print("Permission denied. Please check your file permissions or path.")
    except ValueError as e:
        print(e)
