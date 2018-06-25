# Global Reach
# Demonstrates global variables

def readGlobal():
    print(f"From inside the local scope of readGlobal(), value is: {value}")

def shadowGlobal():
    value = -10   
    print(f"From inside the local scope of shadowGlobal(), value is: {value}")

def changeGlobal():
    global value
    value = -10
    print(f"From inside the local scope of changeGlobal(), value is: {value}")

# main
# value is a global variable because we're in the global scope here
value = 10
print(f"In the global scope, value has been set to: {value}\n")

readGlobal()
print(f"Back in the global scope, value is still: {value}\n")

shadowGlobal()
print(f"Back in the global scope, value is still: {value}\n")

changeGlobal()
print(f"Back in the global scope, value has now changed to: {value}")

input("\n\nPress the enter key to exit.")
