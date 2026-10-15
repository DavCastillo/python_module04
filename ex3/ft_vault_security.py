#!/usr/bin/env python3

def secure_archive(fl_name: str, action: int = 0,
                   content: str = "") -> tuple[bool, str]:
    if action:
        if content != "":
            with open(fl_name, 'w') as file:
                file.write(content)
                return (True, "Content succesfully written to file")
        else:
            return (False, "No content provided to write in the file")
    else:
        try:
            with open(fl_name) as file:
                return (True, file.read())
        except FileNotFoundError as error:
            return (False, str(error))
        except PermissionError as error:
            return (False, str(error))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure archive' to read from a nonexistent file:")
    print(secure_archive("/non/existing/file"))

    print("\nUsing 'secure archive' to read from a innaccesible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure archive' to read from a regular file:")
    file_content = secure_archive("fragment.txt")
    print(file_content)

    print("\nUsing 'secure archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", 1, file_content[1]))
