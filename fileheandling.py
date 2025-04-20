""" This is the task of 1 """

try:
    file1 = open('file.txt', 'w+')

    write = file1.write('Hello World\nThis code is read to line by line\nThe output is the same line print...')
    print(write)
    file1.close()

    file2 = open('file.txt', 'r')
    print(file2.read())
    file2.close()
except FileNotFoundError:
    print('File not found')
except Exception as e:
    print(f'This Error type are Different. {e}')

print("*" * 200)
print(" 2 Task \n","*" * 20)

""" This is the task of 2 """

def file_head():
    try:
        user_input = input('Enter the some text to file write: ')
        with open('output.txt', 'a') as file:
            file.write(user_input + "\n")
            file.close()

        user_append = input('Enter the some text to append to file: ')
        with open(r'output.txt', 'a') as file:
            file.write(user_append + "\n")
            file.close()

        with open(r'output.txt', 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print('File not found')

file_head()