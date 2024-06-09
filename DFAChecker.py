
import DFAReader as pi
import collections

def CheckDFA(inputFile):

    pi.sections = pi.ReadInstructions(str(inputFile))

    listOfSymbols = pi.get_section_content(pi.sections, "Sigma")
    listOfStates = pi.get_section_content(pi.sections, "States")
    listOfTransitions = pi.get_section_content(pi.sections, "Transitions")

    initialState = None

    #todo remove lists from symbols so verifications would work properly
    for symbol in listOfSymbols:
        symbol = str(symbol)

    print(listOfSymbols)
    #Verify integrity of each section
    if len(listOfSymbols) == 0:
        print("Invalid symbols")
        return False

    if len(listOfStates) == 0:
        print("Invalid symbols")
        return False

    if len(listOfTransitions) == 0:
        print("Invalid symbols")
        return False


    initialStateCount = 0
    finalStateCount = 0

    #Verify integrity of each state
    for state in listOfStates:

        if len(state) > 1:
            if state[1] == "S":
                initialStateCount += 1

            if state[1] == "F":
                finalStateCount += 1

        transitionsFromThisState = []
        usedSymbols = []

        allSymbols = []
        for symbol in listOfSymbols:
            allSymbols.append(symbol[0])

        #looks for all transitions that start from this state
        for transition in listOfTransitions:
            if transition[0] == state[0]:
                #saves the symbol used
                usedSymbols.append(transition[1])
                #saves the transition
                transitionsFromThisState.append(transition)

        #checks if there are duplicate transitions on a state
        if not len(usedSymbols) == len(set(usedSymbols)):
            print("duplicate symbol used on state " + state[0])
            return False

        #checks if all states contain a definition for each symbol
        if not len(set(usedSymbols)) == len(set(allSymbols)):
            symbolsNotUsed = list(set(allSymbols).difference(set(usedSymbols)))
            for symbol in symbolsNotUsed:
                print("Missing transition from " + state[0] + " from symbol " + symbol)
                return False

    #checks if there is one initial state
    if initialStateCount > 1:
        print("Too many initial states")
        return False
    if initialState == 0:
        print("Missing initial state")
        return False
    #checks if theres at least 1 initial state
    if finalStateCount < 0:
        print("Missing final state")
        return False

    #checks if transitions use valid symbols
    for transition in listOfTransitions:
        if not listOfSymbols.__contains__(transition[1]):
            print("Invalid symbol used")
            return False
        if not listOfStates.__contains__(transition[0]):
            print("Invalid state used as from transition")
            return False
        if not listOfStates.__contains__(transition[2]):
            print("Invalid state used as to transition")
            return False

    for state in listOfStates:
        if state.__contains__("S"):
            initialState = state[0]


def process(self, input_string):
    self.reset()
    for symbol in input_string:
        if (self.current_state, symbol) in self.transitions:
            self.current_state = self.transitions[(self.current_state, symbol)]
        else:
            return False
    return self.current_state in self.accepting_states



CheckDFA("input.txt")