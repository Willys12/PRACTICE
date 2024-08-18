#my command interpreter
import cmd

print(dir(cmd.Cmd))

class MyCommand(cmd.Cmd):
    prompt = "(commands) > "
    
    #defining commands
    def do_quit(self, arg):
        """This quits the interpreter"""
        return True
    
    #Aliasing
    do_exit = do_quit
    

MyCommand().cmdloop()