import os
import pathlib


def find_directories(directory):
    for filename in os.listdir(directory):
        if os.path.isdir(f"{directory}/{filename}"):
            print(f"{directory}/{filename}")
            find_directories(f"{directory}/{filename}")


find_directories(".")
