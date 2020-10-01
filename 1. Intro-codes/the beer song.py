word='bottle'
for beer_num in range(99,0,-1): #3rd parameter is increment/decrement step
    print(beer_num,word,'of beer on the wall')
    print(beer_num, word,'of beer')
    print('Take one down')
    print('Pass it down')
    if beer_num==1:
        word='bottle'
    else:
        new_num=beer_num-1
        if new_num==1:
            word='bottle'
        print(new_num, word, 'of beer on the wall')
    print()