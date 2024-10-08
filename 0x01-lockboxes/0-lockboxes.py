#!/usr/bin/python3


def canUnlockAll(boxes):
    arr = [subboxes[:] for subboxes in boxes]

    for box in boxes:
        for subBox in box:
            if (subBox != boxes.index(box)):
                arr[subBox].append('$')

    for box in arr[1:]:
        if '$' not in box:
            return False
    return True
