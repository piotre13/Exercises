

#classes
#methods



if __name__ == '__main__':


    name = 'Pietro'
    surname = 'Rando'
    age = 28
    birth = {"birth_place": "Turin",
             "birth_date": "13/5/95"}

    fav_foods = ['pasta','pesce','mandolino']

    print(f"""
	user name: {name},
	surname: {surname},
	age: {age},
	birth_place: {birth['birth_place']}
	birth_date: {birth['birth_date']}
	favourite foods: {fav_foods} 
 """)

    name = input('what is your name?')
    print(name)

    birth['birth_place'] = input('where did you born?')

    fav_foods=[]
    flag = True
    while flag:
        food = input('fav foods?')
        if food == 'q':
            flag=False
        else:
            fav_foods.append(food)


