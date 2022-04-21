#!/usr/bin/python3
def canUnlockAll(boxes):
    '''
    Write a method that determines if all the boxes can be opened..
    '''
    if (len(boxes) == 0):
        return False
    box = list(range(len(boxes)))
    key = [False]*len(boxes)
    keys = [0]
    key[0] = True

    for i in keys:
        for k in boxes[i]:
            if k in box:
                if k not in keys:
                    keys.append(k)
                    key[k] = True

    if False in key:
        return False
    return True

