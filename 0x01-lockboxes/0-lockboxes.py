#!/usr/bin/python3
""" lockboxes """


def canUnlockAll(boxes):
    """
    function canUnlockAll:
        determines if all the boxes can be opened.
    """
    arr = [subboxes[:] for subboxes in boxes]

    for box in boxes:
        for subBox in box:
            if subBox < len(arr) and (subBox != boxes.index(box)):
                arr[subBox].append('$')

    for box in arr[1:]:
        if '$' not in box:
            return False
    return True
