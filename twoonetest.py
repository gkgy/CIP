import pprint
info = '''SCENE I. Yorkshire. Gaultree Forest.
Enter the ARCHBISHOP OF YORK, MOWBRAY, LORD HASTINGS, and others
ARCHBISHOP OF YORK
What is this  forest call'd?
HASTINGS
'Tis Gaultree
Of forge
His foes are so enrooted with his friends'''
count = { }
for character in info.upper():
    count[character]=count.get(character,0)+1

value = pprint.pformat(count)
print(value)