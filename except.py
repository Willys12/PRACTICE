import sys
    
    
def linux_interaction():
    assert('Linux' in sys.platform), "Fuction can only run on Linux system"
    print('Doing something')
    
try:
    linux_interaction()
    with open('file.log') as file:
        read_data = file.read()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('linux_interaction() Linux function not executed')