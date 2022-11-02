import os
import re
from pathlib import Path
from time import time

from pympler import asizeof


class WorkWithFile:
    def __init__(self, pattern: str, file_to_read: str):
        self.pattern = pattern
        self.file_to_read = file_to_read
        self.dir = Path(__file__).parent
        self.writer_in_file(self.filter_lines())

    def __str__(self):
        answ = ""
        for j, k, z in zip(
            self.size_file(), self.len_file(), self.files_in_directory()
        ):
            answ += f"\nFile: {z}\nSize: {j} bytes\nNumber of lines: {k}\n"
        return answ

    def filter_lines(self):
        file_to_read = self.dir / self.file_to_read
        with open(file_to_read, encoding="utf-8") as file:
            while True:
                line = file.readline().rstrip()
                if not line:
                    break
                if self.pattern in line.lower():
                    yield line

    def writer_in_file(self, line: filter_lines):
        file_to_save = self.dir / f"{int(time())}.txt"
        with open(file_to_save, "a", encoding="utf-8") as f:
            for item in list(line):
                f.write(f"{item}\n")

    def files_in_directory(self):
        for files in os.walk(self.dir):
            for file in files[2]:
                if re.search("[0-9]{10}.txt", file):
                    yield file

    def len_file(self):
        for i in self.files_in_directory():
            with open(i, encoding="utf-8") as file:
                yield len(file.readlines())

    def size_file(self):
        for i in self.files_in_directory():
            with open(i, encoding="utf-8") as file:
                yield asizeof.asizeof(file.readlines()) / 1000000


print(WorkWithFile("1", "rockyou.txt"))
