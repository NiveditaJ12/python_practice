# Remove punctuations from thr string

def remove_punctuations(str):
    punc = '''`!;:'",.?{}[]-_+=|\())*&%$#@'''
    empty_str = ""
    for i in range(len(str)):
        if str[i] not in punc:
            empty_str += str[i]
    return empty_str

str = "\'Hello, everyone.\ How are you?\'"

print(remove_punctuations(str))