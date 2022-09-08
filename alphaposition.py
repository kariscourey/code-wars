def alphabet_position(text):

    lst = []

    for i in text:
        if i.isalpha():
            lst.append(str(ord(i.lower()) - 96))
    return " ".join(lst)

print(alphabet_position("The sunset sets at twelve o' clock."))

# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha()
