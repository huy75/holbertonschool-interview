#!/usr/bin/python3
def canUnlockAll(boxes):
    if not boxes:
        return False
    size = len(boxes)
    checker = {}
    index = 0

    for box in boxes:
        for key in box:
                if key < size and key != index:
                    checker[key] = key
        if len(checker) == size - 1:
            return True
        index += 1
    return False
