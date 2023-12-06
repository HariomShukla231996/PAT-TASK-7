## Write a program using function to which we wil do the following-
## a. The function will create a text file with the current time stamp. 
## b. The file content should have the content of the current time stamp.

import datetime

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
with open("timestamp.txt", "w") as f:
    f.write(timestamp)
f.close()

## Write another python function to read from the text file. 
# The function will take the name of the text file and display the content of the file into the console.

def read_text_file(guviclass):
    try:
        with open(guviclass, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{guviclass}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")