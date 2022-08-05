from github import Github
import os
from random import randint
from pprint import pprint

def create_file():
    with open("file.txt", 'w') as file:
        file.write("This is a test file" + randint(1, 11))

if __name__ == "__main__":
    file_path = "file.txt"

    