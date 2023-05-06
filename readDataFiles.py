import os
import glob

for file in glob.glob('data/*'):
    file_entries = open(file).readlines()

    for animal in file_entries:
        print(animal.strip())
