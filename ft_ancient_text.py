import sys
# sys.argv est une liste

def main():
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        for value in sys.argv[1:]:
            print(f"Accessing file '{value}")
            try:
                file = open(value)
            except FileNotFoundError as e:
                print(f"Error opening file '{value}': {e}")
            except PermissionError as e:
                print(f"Error opening file '{value}': {e}")
            else:
                print(f"\n{file.read()}")
                print(f"File '{value}' closed")
                file.close()
    
main()
        
        