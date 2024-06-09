import json
import sys
import DFAChecker

#inputCommand = input()
#splitCommands = inputCommand.split()
#engine = splitCommands[0]
#config = splitCommands[1]
#inputStr = splitCommands[2]

if len(sys.argv) != 3:
    print("Usage: python your_dfa_engine.py dfa_config_file input_string")
    sys.exit(1)

python_File = sys.argv[0]
config_file = sys.argv[1]
input_string = sys.argv[2]

try:
    with open(config_file, "r") as file:
        config = json.load(file)
except Exception as e:
    print(f"Error reading config file: {e}")
    sys.exit(1)

if(DFAChecker.CheckDFA(input_string) == False):
    print("reject")

if python_File.process(input_string):
    print("accept")
else:
    print("reject")



