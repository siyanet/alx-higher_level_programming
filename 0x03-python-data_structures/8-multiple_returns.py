#!/usr/bin/python3
def multiple_returns(sentence):
    i = len(sentence)
    if i == 0:
        return i, None
    return i,sentence[0]

    sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
