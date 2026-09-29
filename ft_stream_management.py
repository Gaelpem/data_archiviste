import sys


def main():
    print("=== Cyber Archives Recovery & Preseration ===")
    if len(sys.argv) <= 1:# si il ya quelque chose dans la liste
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        for  value in sys.argv[1:]: # liste = [...]
            print(f"Accessing file {value}")
            try:
                file = open(value,'r')# verifie si fichier existe
            except FileNotFoundError as e:
                sys.stdout.write(f"[STDERR] Error opening file '{value}' : {e}")
            else:
                # si le fichier existe alors 
                save = file.read()# on recupee ce qu'il y a dedans 
                print(f"\n{save}")
                print("\n---")
                sys.stdout.write(f"File '{value}' closed")
                line_split = save.split("\n")
                print("\nTransformd data:")
                for line in line_split:
                    content  = line + "#\n"
                    sys.stdout.write(content)
                sys.stdout.write("Enter new file name (or empty): ")
                sys.stdout.flush()
                usr_input = sys.stdin.readline().strip()
                if usr_input:
                    try:  
                        file_transform = open(usr_input, "w")
                    except PermissionError as e:
                        sys.stderr.write(f"[STDERR] Error opening file '{usr_input}': {e}\n")
                        sys.stderr.write("Data not save\n")
                    else:
                        print(f"{usr_input}")                          
main()