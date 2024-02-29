commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]
command = input("Enter a command: ")
if (command not in commands):
    print("Not supported")
else:
    print("OK")
    