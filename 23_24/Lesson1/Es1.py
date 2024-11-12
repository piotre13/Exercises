

if __name__ == '__main__':

    # ES1 ***********************

    name = 'Mario'
    surname = 'Rossi'
    age = 28
    birth={}
    birth['place'] = 'Turin'
    birth['date'] = '1995-05-13'
    fav_foods = ['pasta', 'egg', 'fish']

    content = f"""
    	user name: {name},
    	surname: {surname},
    	age: {age},
    	birth_place: {birth['birth_place']}
    	birth_date: {birth['birth_date']}
    	favourite foods: {fav_foods} 
     """
    print (content)


    # ES1.1 *********************************************+

    name = input('What is your name?\n')
    surname = input('Surname?\n')
    age = input('Age?\n')
    birth={}
    birth['place'] = input('Where were you born?\n')
    birth['date'] = input('When were you borno?\n')
    fav_foods=[]
    print('please input your favorite foods and press "q" when its over\n')
    i=0
    while True:
        fav_f = input('Fav food #%s'%i)
        if fav_f == 'q':
            break
        fav_foods.append(fav_f)
        i+=1

    content = f"""
	user name: {name},
	surname: {surname},
	age: {age},
	birth_place: {birth['birth_place']}
	birth_date: {birth['birth_date']}
	favourite foods: {fav_foods} 
    """

    print(content)

    # Es1.2
    #test
    with open('User_info.txt', 'w') as f:
        txt = f.write(content)



    #NB once is written try to read ita and understand what is the output when reading simple text files