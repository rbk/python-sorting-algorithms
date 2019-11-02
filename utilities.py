from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Datasets
numbers_simple = [4,7,8,6,9,5,3,1,2,10]
numbers_complex = [0,3,5,6,83,3,3,5,7,78,82,2,2,4,4,5,67,46,34,5,534534,53,0,12,2,12]
words = ['python', 'cat', 'ace', 'elder', 'dog', 'story', 'program', 'coffee']

def log(text):
    text = str(text)
    dashes = len(text) + 6;
    line = reduce((lambda x, y: "-" + str(x)), ["-" for i in range(0, dashes)])
    print("|{}|".format(line))
    print(pad_text(text, dashes+2))
    print("|{}|".format(line))

def pad_text(text, length):
    pad = length - len(text)
    if pad > 0:
        half_pad = pad/2
        return "{}{}{}".format(get_spaces(half_pad), text, get_spaces(half_pad))
    return text

def get_spaces(count):
    return reduce((lambda x, y: " " + str(x)), [" " for i in range(0, int(count))])