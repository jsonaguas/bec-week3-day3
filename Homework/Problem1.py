names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

import re
def valid_names(list):
    for name in list:
        if re.match(r'^[A-Z][a-z]*\s[A-Z][a-z]*(\s[A-Z][a-z]*)?$', name):
            print(name)
        else:
            print("Invalid name")

valid_names(names)
