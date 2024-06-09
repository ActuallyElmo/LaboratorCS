import ProgramInstructiuni as pi

pi.sections = pi.ReadInstructions("InputNou.txt")
print(pi.get_section_list(pi.sections))
#print(pi.get_section_content(pi.sections, "Transitions"))

def CheckDFA():
    listOfStates = pi.get_section_content(pi.sections, "States")

    print listOfStates()
    initialState = listOfStates.Find


CheckDFA()