#!/usr/bin/env python3

import sys
import typing


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        sys.stdout.write(f"Usage: {sys.argv[0]} <file>\n")
    else:
        try:
            sys.stdout.write("=== Cyber Archives recovery ===\n")
            fl_name = sys.argv[1]
            sys.stdout.write(f"Accessing file '{fl_name}'\n")
            file: typing.IO[str] = open(fl_name)
            content = file.read()
            sys.stdout.write("---\n\n")
            sys.stdout.write(content)
            sys.stdout.write("\n---\n")
            file.close()
            sys.stdout.write(f"File '{fl_name}' closed\n")
            sys.stdout.write("\nTransform data:\n")
            content = content.replace("\n", "#\n")
            sys.stdout.write("---\n\n")
            sys.stdout.write(content)
            sys.stdout.write("\n---\n")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            new_name = sys.stdin.readline().strip()
            if (new_name != ""):
                sys.stdout.write(f"Saving data to '{new_name}'\n")
                new_file: typing.IO[str] = open(new_name, 'w')
                new_file.write(content)
                new_file.close()
                sys.stdout.write(f"Data saved in file '{new_name}'.\n")
            else:
                sys.stdout.write("Not saving data.\n")
        except FileNotFoundError:
            sys.stderr.write(f"[STDERR] Error opening file '{fl_name}': "
                             "[Errno 2] No such file or"
                             f" directory: '{fl_name}'\n")
        except PermissionError:
            sys.stderr.write(f"[STDERR] Error opening file '{new_name}': "
                             f"[Errno 13] Permission denied: '{new_name}'"
                             "\nData not saved.\n")
        except KeyboardInterrupt:
            sys.stderr.write("\nKeyboard interrupted\n")
