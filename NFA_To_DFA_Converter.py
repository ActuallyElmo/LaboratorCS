import itertools

def ReadInstructions(file):
    f = open(str(file), "r")

    dictionary = {}
    section = []
    readSection = False
    lineCount = -1

    for line in f:
        lineCount = lineCount + 1

        if line.__contains__("#"):
            continue

        if line.__contains__("End"):
            readSection = False
            sectionName = " "
            continue

        if readSection == False:
            sectionName = ''.join(line.split())
            sectionName = sectionName[:len(sectionName) - 1]  # remove the ':' from section name
            dictionary[sectionName] = []  # create the dictionary entry for this section
            readSection = True
            section = []  # create a list of words for this section
            continue

        if readSection:
            if sectionName == " ":
                print("No valid section entry name at line " + str(lineCount))
                return None

            if line.__contains__(":"):
                print("Another section started before a valid end symbol at line " + str(lineCount))
                return None

            instructions = []
            for word in line.split(sep=","):
                formattedWord = ''.join(word.split())
                instructions.append(formattedWord)

            section.append(instructions)
            dictionary.update({sectionName: section})
            continue

    return dictionary

def get_section_list(content):
    if content is None:
        print("Invalid content")
        return None

    return list(content.keys())

def get_section_content(content, section_name):
    if content is None:
        print("Invalid content")
        return None

    if section_name not in content:
        print("Invalid section name")
        return None

    return content[section_name]


class NFA:
    def __init__(self, states, alphabet, start_state, accepting_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accepting_states = accepting_states
        self.transitions = transitions

    def get_epsilon_closure(self, state):
        closure = {state}
        stack = [state]
        while stack:
            current_state = stack.pop()
            if ('ε', current_state) in self.transitions:
                for next_state in self.transitions[('ε', current_state)]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def to_dfa(self):
        dfa_states = []
        dfa_start_state = frozenset(self.get_epsilon_closure(self.start_state))
        dfa_accepting_states = set()
        dfa_transitions = {}

        unprocessed_states = [dfa_start_state]
        dfa_states.append(dfa_start_state)

        while unprocessed_states:
            current = unprocessed_states.pop()
            if any(state in self.accepting_states for state in current):
                dfa_accepting_states.add(current)

            for symbol in self.alphabet:
                if symbol == 'ε':
                    continue

                next_state = set()
                for state in current:
                    if (symbol, state) in self.transitions:
                        for next_state_candidate in self.transitions[(symbol, state)]:
                            next_state.update(self.get_epsilon_closure(next_state_candidate))

                next_state = frozenset(next_state)
                if next_state not in dfa_states:
                    dfa_states.append(next_state)
                    unprocessed_states.append(next_state)

                dfa_transitions[(current, symbol)] = next_state

        return DFA(dfa_states, self.alphabet, dfa_start_state, dfa_accepting_states, dfa_transitions)

class DFA:
    def __init__(self, states, alphabet, start_state, accepting_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accepting_states = accepting_states
        self.transitions = transitions

def convert_to_dfa(nfa_file, dfa_file):
    sections = ReadInstructions(nfa_file)

    alphabet = [symbol[0] for symbol in get_section_content(sections, "Sigma")]
    states = [state[0] for state in get_section_content(sections, "States")]
    start_state = [state[0] for state in get_section_content(sections, "States") if len(state) > 1 and state[1] == 'S'][0]
    accepting_states = [state[0] for state in get_section_content(sections, "States") if len(state) > 1 and state[1] == 'F']
    
    transitions = {}

    for transition in get_section_content(sections, "Transitions"):
        from_state, symbol, to_state = transition
        if (symbol, from_state) not in transitions:
            transitions[(symbol, from_state)] = []
        transitions[(symbol, from_state)].append(to_state)

    nfa = NFA(states, alphabet, start_state, accepting_states, transitions)
    dfa = nfa.to_dfa()

    with open(dfa_file, 'w') as f:
        
        f.write("Sigma:\n")

        for symbol in dfa.alphabet:
            f.write(f"\t{symbol}\n")

        f.write("End\n")

        f.write("States:\n")

        for state in dfa.states:
            state_line = f"\t{state}"
            if state == dfa.start_state:
                state_line += ", S"
            if state in dfa.accepting_states:
                state_line += ", F"
            f.write(state_line + "\n")

        f.write("End\n")

        f.write("Transitions:\n")

        for (from_state, symbol), to_state in dfa.transitions.items():
            f.write(f"\t{from_state}, {symbol}, {to_state}\n")

        f.write("End\n")
