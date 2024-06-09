import sys
from NFA_To_DFA_Converter import convert_to_dfa

def main():
    if len(sys.argv) != 3:
        print("Usage: python your_dfa_engine.py nfa_file dfa_file")
        sys.exit(1)

    nfa_file = sys.argv[1]
    dfa_file = sys.argv[2]

    convert_to_dfa(nfa_file, dfa_file)

main()
