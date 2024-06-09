import sys
from nfa_to_dfa_converter import convert_to_dfa

def main():
    if len(sys.argv) != 3:
        print("Usage: python your_dfa_engine.py nfa_file dfa_file")
        sys.exit(1)

    nfa_file = sys.argv[1]
    dfa_file = sys.argv[2]

    convert_to_dfa(nfa_file, dfa_file)

if __name__ == "__main__":
    main()
