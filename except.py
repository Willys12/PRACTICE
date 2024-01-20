def linux_interaction():
    assert('Linux' in sys.platform), "Fuction can only run on Linux system"
    print('Doing something')
    
try:
    linux_interaction()
    
except:
    print('Linux function not executed')