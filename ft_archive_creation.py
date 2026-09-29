import sys

def main():
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery & Presevrvation ===")
        for value in sys.argv[1:]:
            print(f"Accessing file {value}")
            try:
                file = open(value, "r")# ouvrir le fichier.....
            except FileNotFoundError as e:
                print(f"Error opening file '{value}': {e}")
            else:
                save = file.read() # on recupere le fichier sous forme de texte
                # on recupere ce qu'il y a dedans
                print(f"\n{save}")
                print("\n---")
                print(f"File '{value}' closed")# on affiche le nom du fichier
                line_split = save.split("\n")
                print("\nTransformd data:")
                print("---\n")
                for line in line_split:
                        content = line + "#"
                        print(f"{content}")
                print("\n---")
                usr_input = input("Enter new  file name (or empty): ")
                if usr_input:
                    print(f"Saving data to : '{usr_input}'")# le nom du fichier
                    new_file = open(usr_input,"w") #  ouvre le fichier et creer
                    texte_decouper = save # on decoupe le txt
                    line2_split = texte_decouper.split("\n")
                    for line2 in line2_split:
                        content2 = line2 + "#\n"
                        new_file.write(content2)
                    print(f"Data saved  in file '{usr_input}'.")
                else:
                    print("Not saving data")
                    
main()