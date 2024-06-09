
#O multime de cuvinte
#O multime de stari Q
#Un sir de instructiuni

#Dictionarul cu sectiuni
sections = {}

#citeste un fisier si returneaza un dictionar cu sectiuni si instructiuni
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

        # join and split to remove \t and \n:

        if readSection == False:
            sectionName = ''.join(line.split())
            sectionName = sectionName[:len(sectionName) - 1] #remove the ':' from section name
            dictionary[sectionName] = [] #create the dictionary entry for this section
            readSection = True
            section = [] #create a list of words for this section
            continue

        if readSection:

            #invalid instructions
            #No valid section name entry
            if sectionName == " ":
                print("No valid section entry name at line " + str(lineCount))
                return None

            #Another section start before an end symbol
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
        break

    return dictionary

def get_section_list(content):

    if content is None:
        print("Invalid content")
        return None

    list = []
    for section in content:
        list.append(section)

    return list

def get_section_content(content, section_name):

    if content is None:
        print("Invalid content")
        return None

    if not content.__contains__(section_name):
        print("Invalid section name")
        return None

    sectionContent = []

    for i in range(0, len(content[section_name])):
        sectionContent.append(content[section_name][i])

    return sectionContent



#Initializare Seciune
#sections = ReadInstructions("InputNou.txt")


#print(get_section_list(sections))
#print(get_section_content(sections, "Transitions"))


