from datetime import datetime  #importing specific functions from specific modules
odd=[1,3,5,7,9,11,13,15,17,19,
     21,23,25,27,29,31,33,35,37,39,
     41,43,45,47,49,51,53,55,57,59]

right_this_minute=datetime.today().minute

if right_this_minute in odd:  #'in' is super operator which is equivalent of '='
    print("\nThis minute seems odd")
else:
    print("\nNot an odd minute")