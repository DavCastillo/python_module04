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
            print()
            print(type(file))
            content = file.read()
            print("---\n")
            print(content)
            print("---")
            file.close()
            print(f"File '{fl_name}' closed")
        except FileNotFoundError as error:
            print("Error opening file:", error)
        except PermissionError as error:
            print("Error opening file:", error)
