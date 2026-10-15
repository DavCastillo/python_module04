#!/usr/bin/env python3

import sys
import typing


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print(f"Usage: {sys.argv[0]} <file>\n")
    else:
        try:
            print("=== Cyber Archives recovery ===")
            fl_name = sys.argv[1]
            print(f"Accessing file '{fl_name}'")
            file: typing.IO[str] = open(fl_name)
            content = file.read()
            print("---\n")
            print(content)
            print("---")
            file.close()
            print(f"File '{fl_name}' closed")
            print("\nTransform data:")
            content = content.replace("\n", "#\n")
            print("---\n")
            print(content)
            print("---")
            new_name = input("Enter new file name (or empty): ")
            if (new_name != ""):
                print(f"Saving data to '{new_name}'")
                new_file: typing.IO[str] = open(new_name, 'w')
                new_file.write(content)
                new_file.close()
                print(f"Data saved in file '{new_name}'.")
            else:
                print("Not saving data.")
        except FileNotFoundError as error:
            print("Error opening file:", error)
        except PermissionError as error:
            print("Error opening file:", error)
        except KeyboardInterrupt:
            print("\nKeyboard interrupted")
