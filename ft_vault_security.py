def secure_archive(name_fichier: str, action="r", content=""):
   
    if action == 'r':
        try:
            with open(name_fichier, "r") as file:
                data = file.read()
        except FileNotFoundError as e:
            return (False, str(e))
        except PermissionError as e:
            return (False, str(e))
        else:
            return (True, data)
    else:
        with open(name_fichier, "w") as file:
            file.write(content)
            return (True,"Content successfully written to file")
            
print("=== Cyber Archives Security ===\n")
test = secure_archive("/not/existing/file", "r", None)
print(f"Using 'secure_archive' to read from a nonexistant file:")
print(f"{test}\n")

test1 = secure_archive("/etc/master.passwd", "r",None)
print(f"Using 'secure_archive' to read from an inaccessible file:")
print(f"{test1}\n")

test2 = secure_archive("ancient_fragment.txt", "r" , None)
print(f"Using 'secure_archive' to read a regular file:")
print(f"{test2}\n")

print("Using 'secure_archive' to write previous content to a new file")
test3 = secure_archive("new_file.txt", "w", "New file")
print(test3)

