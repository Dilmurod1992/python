try:
    print(10/0)
except ZeroDivisionError:
    print("siz 0 ga bo'lishga urinyabsiz")


try:
    print(int('d'))
except ValueError:
    print("Faqat son kiriting")    



import os
file_path = 'Python_learning_file.txt'

if os.path.exists(file_path):
    print("Bunday fayl mavjud")
else:
    print("Bunday fayl mavjud emas")



son = input("Ikkita istalgan sonni kiriting:  ")

if son.isdigit():
    print(f"siz kiritgan sonlar: {son}")
else:
    print("Siz son kiritmadingiz")



def read_file(darsliklar):
    try:
        with open(darsliklar, 'r') as file:
            contents = file.read()
            print("File contents:\n", contents)
    except PermissionError:
        print(f"Rad etildi: Sizda  '{darsliklar}' faylini ochish uchun ruxsat yo'q.")
    except FileNotFoundError:
        print(f"Fayl topilmadi: '{darsliklar}' fayli mavjud emas.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

darsliklar = input("Ochmoqchi bo'lgan faylingizni kiriting: ")
read_file(darsliklar)



def access_list_element(my_list, index):
    try:
        print(f"Element at index {index}: {my_list[index]}")
    except IndexError:
        print(f"IndexError: Index {index} is out of range for the list.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example list
sample_list = [10, 20, 30, 40, 50]

# Example usage:
try:
    user_index = int(input("Enter the index of the element you want to access: "))
    access_list_element(sample_list, user_index)
except ValueError:
    print("Invalid input: Please enter an integer index.")



def main():
    try:
        user_input = input("Please enter a number: ")
        number = float(user_input)  
        print(f"You entered the number: {number}")
    except KeyboardInterrupt:
        print("\nInput cancelled by user.")
    except ValueError:
        print("That's not a valid number.")

if __name__ == "__main__":
    main()





try:
    
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    result = numerator / denominator
    print(f"Result: {result}")

except ArithmeticError as e:
    print(f"An arithmetic error occurred: {e}")





try:
    
    with open("darsliklar.txt", "r") as file:
        content = file.read()
        print("File content:\n", content)

except UnicodeDecodeError as e:
    print(f"Unicode decoding error occurred: {e}")
except FileNotFoundError:
    print("'Darsliklar' fayli topilmadi.")




try:
    my_list = [1, 2, 3, 4, 5]

    my_list.push(6)

except AttributeError as e:
    print(f"Attribute error occurred: {e}")




try:
    with open("masalalar.txt", "r") as file:
        content = file.read()
        print("File content:\n")
        print(content)

except FileNotFoundError:
    print("The file was not found.")



def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            print(f"First {n} lines of {filename}:\n")
            for i in range(n):
                line = file.readline()
                if not line:
                    break  
                print(line.strip())
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")


filename = "python_darsliklari.txt"
n = 5  
read_first_n_lines(filename, n)




with open ('8th_lesson/a\new_file.txt', 'a') as f:
    f.write("Bu qo'shish uchun yangi yozuv")




with open ('c:\\Users\\DILMUROD\Desktop\\For python lessons\\1st lesson\\8th lesson\\a\new_file.txt', 'r') as f:
    for line in f:
        print(line)



from collections import deque

def read_last_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            last_lines = deque(file, maxlen=n)
        
        print(f"Last {n} lines of '{filename}':\n")
        for line in last_lines:
            print(line.strip())

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = "new_file.txt"
n = 5  
read_last_n_lines(filename, n)



def read_file_to_list(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file]  
        return lines
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        return []

filename = "new_file.txt"  
line_list = read_file_to_list(filename)

print("Lines stored in list:")
print(line_list)





def read_file_to_string(filename):
    try:
        with open(filename, 'r') as file:
            content = ""
            for line in file:
                content += line
        return content
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        return ""

filename = "example.txt"
content_variable = read_file_to_string(filename)

print("Stored content:")
print(content_variable)




def read_file_to_array(filename):
    try:
        with open(filename, 'r') as file:
            
            array = [line.strip() for line in file]
        return array
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        return []


filename = "text_file.txt"  
lines_array = read_file_to_array(filename)

print("Lines stored in array:")
print(lines_array)




def find_longest_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()  
            max_length = max(len(word) for word in words)
            longest_words = [word for word in words if len(word) == max_length]
        
        print(f"Longest word(s) (length = {max_length}):")
        for word in longest_words:
            print(word)
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except ValueError:
        print("The file is empty or contains no valid words.")

filename = "text_file.txt"  
find_longest_words(filename)




def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        print(f"The file '{filename}' has {line_count} line(s).")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")

filename = "fruits.txt"  
count_lines(filename)



from collections import Counter
import string

def count_word_frequency(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()

        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translator).lower()

        words = cleaned_text.split()
        word_counts = Counter(words)

    
        print("Word frequencies:\n")
        for word, count in word_counts.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")


filename = "text_file.txt"  
count_word_frequency(filename)




import os

def get_file_size(filename):
    try:
        size = os.path.getsize(filename)
        print(f"The size of '{filename}' is {size} bytes.")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")


filename = "fruits.txt"  
get_file_size(filename)





def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(f"{item}\n")
        print(f"List written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

my_list = ["apple", "banana", "cherry", "date"]
filename = "fruits.txt"
write_list_to_file(filename, my_list)



def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        
        with open(destination_file, 'w') as dest:
            dest.write(content)

        print(f"Contents copied from '{source_file}' to '{destination_file}' successfully.")
    
    except FileNotFoundError:
        print(f"The source file '{source_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

source = "fruits.txt"
destination = "copy_fruits_file.txt"
copy_file(source, destination)




def combine_lines(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
            for line1, line2 in zip(f1, f2):
                combined_line = line1.strip() + " " + line2.strip() + "\n"
                out.write(combined_line)
        
        print(f"Lines combined and written to '{output_file}' successfully.")
    
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

file1 = "fruits.txt"
file2 = "text_file.txt"
output = "combined.txt"
combine_lines(file1, file2, output)




import random

def read_random_line(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            print("The file is empty.")
            return
        
        random_line = random.choice(lines)
        print("Random line:")
        print(random_line.strip())

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = "fruits.txt"  
read_random_line(filename)



def check_file_closed(filename):
    try:
        file = open(filename, 'r')
        print(f"Is the file closed? {file.closed}")  

        file.close()
        print(f"Is the file closed after closing? {file.closed}")  

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")

filename = "text_file.txt"  
check_file_closed(filename)





def remove_newlines(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read().replace('\n', '')

        with open(output_file, 'w') as outfile:
            outfile.write(content)

        print(f"Newline characters removed and saved to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = "text_file.txt"
output_file = "cleaned_example.txt"
remove_newlines(input_file, output_file)





def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
        print(f"The file '{filename}' contains {word_count} word(s).")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = input("Enter the filename: ")
count_words_in_file(filename)




import os

def extract_characters_from_files(file_list):
    characters = []

    for filename in file_list:
        try:
            with open(filename, 'r') as file:
                content = file.read()
                characters.extend(list(content))  # Add each character to the list
        except FileNotFoundError:
            print(f"The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred while reading '{filename}': {e}")
    
    return characters

files = ["text_file.txt", "fruits.txt", "copy_fruits.txt"]  
char_list = extract_characters_from_files(files)

print("Extracted characters:")
print(char_list)




import string

def generate_alphabet_files():
    for letter in string.ascii_uppercase:  
        filename = f"{letter}.txt"
        try:
            with open(filename, 'w') as file:
                file.write(f"This is file {filename}\n")
            print(f"Created: {filename}")
        except Exception as e:
            print(f"Failed to create {filename}: {e}")

generate_alphabet_files()





import string

def write_alphabet_to_file(filename, letters_per_line):
    alphabet = string.ascii_lowercase  
    
    try:
        with open(filename, 'w') as file:
            for i in range(0, len(alphabet), letters_per_line):
                line = alphabet[i:i+letters_per_line]
                file.write(line + '\n')
        
        print(f"Alphabet written to '{filename}' with {letters_per_line} letter(s) per line.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = "alphabet.txt"
letters_per_line = 5 
write_alphabet_to_file(filename, letters_per_line)
