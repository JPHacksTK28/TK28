import csv
import random
import shutil
import os

import numpy as np


occasions = [
    "Exercise", "MeetingFriends", "Shopping", "Museum", "School", "Work"
]


def write(lines, filename):
    writer = csv.writer(open(filename, 'w'))
    writer.writerows(lines)


def readlines(filename):
    lines = open(filename).read().strip()
    lines = lines.split("\n")
    reader = csv.reader(lines)
    lines = list(reader)
    return lines


def copy(label_filename, src, dst):
    reader = csv.reader(open(label_filename))
    for row in reader:
        basename = row[0]

        s = os.path.join(src, "original", basename)
        d = os.path.join(dst, "original", basename)
        shutil.copy(s, d)

        s = os.path.join(src, "patches", basename)
        d = os.path.join(dst, "patches", basename)
        shutil.copy(s, d)

    d = os.path.join(dst, label_filename)
    shutil.copy(label_filename, d)


labels = readlines("./system/male/labels.txt")
random.shuffle(labels)

n = int(len(labels) * 0.4)
training, test = labels[:n], labels[n:]

training_labels = "training-labels.txt"
test_labels = "test-labels.txt"

write(training, training_labels)
write(test, test_labels)

copy(training_labels, "./system/male", "./system/training_male2")
copy(test_labels, "./system/male", "./user/test_male2")
