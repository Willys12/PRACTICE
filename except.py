import sys
    
    
def linux_interaction():
    assert('Linux' in sys.platform), "Fuction can only run on Linux system"
    print('Doing something')
    
try:
    linux_interaction()
    
except AssertionError as error:
    print(error)
    print('linux_interaction() Linux function not executed')