def palindrome(txt):
    # remove all spaces from the string. (in case if string have spaces)
    txt = txt.replace(" ", "")
    # checking if string is a palindrome through slicing
    return txt == txt[::-1]