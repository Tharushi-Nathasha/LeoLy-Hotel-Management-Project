def greeting ():
    print('Welcome to Hotel LeoLy !\nFollowing is the procedure of Hotel accessories.' )
    print('Please be kind to fill out the necessary requirements so the hotel management can support for your comfort.')
greeting ()

print('Follow the procedure as below when entering the count.\n___Count___ \ns  :single \nc :couple \nf :family \nm :more')
count = str(input('\nEnter the group type who take accommodation in the hotel :'))

if count == 's':
    print(' Single bed room.')
elif count == 'c':
    room = str(input('Choose dbrp-Double bed room package or hmrp-Honey moon room package:'))
    if room == 'dbrp':
        print('Normal double room package ')
    elif room == 'hmrp':
        print('Here you gain additional facilities such as: \n1.Decorated room  \n2.A private pool \n3.Best branded italian vine \n4.Free evening Honey moon food tray \n5.Gallery shoot \n6.10% discount and nuber of days is not considered')
    else :
        print('Room not found')

elif count == 'f'or 'm':
    print('rooms : s-Single rooms , d-Double rooms , e-Enlarge rooms , j-Jumble rooms ')

    rooms = str(input('We need :'))

    if rooms == 's':
        number = str(input('Number of single rooms we need is :'))
        print(f'We choose {number} single rooms')

    elif rooms == 'd':
        number = str(input('Number of double rooms we need is :'))
        print(f'We choose {number} double rooms')

    elif rooms == 'e':
        print('If you choose enlarge bedroom package there are rooms with :\n3dbr-3 double beds \n4dbr-4 double beds \n5dbr-5 double beds \n6dbr-6 double beds  ')
        print('Each enlarge room consists of : \nthree luxury bathrooms \nprivate pools for each room ')
        eroom = str(input('Enter the type of enlarge room/rooms you need :'))
        enumber=str(input(f'Enter the number of rooms you need with dbr type : '))
        print(f'At last we choose {enumber} ')

    elif rooms =='j':
        print('Choose :(sd) s-Single rooms + d-Double rooms or (se) s-Single rooms or e-Enlarge rooms 0r (de)d-double rooms + e-Enlarge rooms 0r (sde) s-Single rooms + d-double rooms + e-Enlarge rooms  ')
        rooms = str(input('We need :'))
        if rooms == 'sd':
            srnumber = str(input('Number of single rooms we need is :'))
            drnumber = str(input('Number of double rooms we need is :'))
            print(f'We choose {srnumber} single rooms and {drnumber} double rooms.')

        elif rooms == 'se':
            srnumber = str(input('Number of single rooms we need is :'))
            print( 'If you choose enlarge bedroom package there are rooms with :\n3dbr-3 double beds \n4dbr-4 double beds \n5dbr-5 double beds \n6dbr-6 double beds  ')
            print('Each enlarge room consists of : \nthree luxury bathrooms \nprivate pools for each room ')
            eroom = str(input('Enter the type of enlarge room/rooms you need :'))
            enumber = str(input(f'Enter the number of rooms you need with dbr type : '))
            ernumber = str(input('Number of enlarge rooms we need is :'))
            print(f'We choose {srnumber} single rooms and {ernumber} enlarge rooms.')

        elif rooms == 'de':
            drnumber = str(input('Number of double rooms we need is :'))
            print('If you choose enlarge bedroom package there are rooms with :\n3dbr-3 double beds \n4dbr-4 double beds \n5dbr-5 double beds \n6dbr-6 double beds  ')
            print('Each enlarge room consists of : \nthree luxury bathrooms \nprivate pools for each room ')
            eroom = str(input('Enter the type of enlarge room/rooms you need :'))
            enumber = str(input(f'Enter the number of rooms you need with dbr type : '))
            ernumber = str(input('Number of enlarge rooms we need is :'))

            print(f'We choose {drnumber} single rooms and {ernumber} enlarge rooms.')

#Number of days

print('\nplease enter the number of days that you are going to accommodate.')
days = str(input('Number of days that we going to accommodate is :'))

#Food board

print('\nSelect the way we should serve your food.')
food = str (input('fb-Full board / hb-Half board :'))
if food == 'fb' :
    print('Congratulations you gain 5% of discount from any menus you choose.')
elif food == 'hb' :
    print('Congratulations you gain 2% of discount from any menus you choose ')
else :
    print('Hope you would enjoy your meal outside the hotel.')
print(f'Food price is calculated according to the number of days and food board type :This willl be added to your bill {days}*{food} ')


# Welcome juice

print('\nBelow is the list of Welcome drink list of Hotel Leoly .\nWe would like to bring you a warm welcome with our customized refreshments. ')
print('\nPlease choose and customize your drink.')
choice2 = str(input('\nWhat would you like to do ? \ns-start,f-finish and order :'))

while choice2 != 'f':

    if choice2 == 's':

        drink_type = str(input('\nDo you want cool drinks or hot drinks ? :'))

        if drink_type == 'cool drinks':
            cd = str(input(f'You have varieties of {drink_type} such as :\nFruit juice \nMilkshakes \nBeer\nWhat do you want ? :'))
            if cd == 'Fruit juice':
                var1= str(input('Fruit juice varieties,select the one you prefer : Apple , Mango , Pine apple , Watermelon ,Orange , Mix fruit :'))
                no1 = int(input('Enter the number of of drinks you want from above item :'))
                print(f'You have selected {no1}  {var1} juice from {cd} items under {drink_type}.')
            elif cd == 'Milkshake':
                var2 = str(input('Here are some milkshake varieties , select the one you prefer : Chocolate , Vanilla, Faluda : '))
                no2 = str(input('Enter the number of of drinks you want from above item :'))
                print(f'You have selected {no2} {var2} milkshake from {cd} items under {drink_type}.')
            elif cd == 'Beer':
                var3 = str(input('Here are some beer varieties , select the one you prefer : Red ale , stouts , White beer : '))
                no3 = str(input('Enter the number of of drinks you want from above item :'))
                print(f'You have selected {no3}  {var3} beer/s from {cd} items under {drink_type}.')

        elif drink_type == 'hot drinks':
            hd = str(input(f'You have varieties of {drink_type} such as :\nTea \nCoffee \nBubble tea \nPlain tea \nHot chocolate\nWhat do you want :'))
            if hd == 'Tea':
                no4 = str(input('Enter the number of of drinks you want from above item :'))
                print(f'You have selected {no4} {hd} from {drink_type}.' )
            elif hd == 'Coffee':
                no5 = str(input('Enter the number of of drinks you want from above item :'))
                print(f'You have selected {no5} {hd} from {drink_type}.')
            elif hd == 'Bubble tea':
                var4=str(input('Here are some bubble tea varieties,select the one you prefer : Milk tea , Taro bubble tea, Thai tea , Strawberry :'))
                no6 = str(input('Enter the number of of drinks you want from above item :'))
                print(f'You have selected {no6} {var4} from {hd}items under {drink_type}.')
            elif hd == 'Plain tea':
                no7 = str(input('Enter the number of of drinks you want from above item :'))
                print(f'You have selected {no7} {hd} from {drink_type}.')
            elif hd == 'Hot chocolate':
                no8 = str(input('Enter the number of of drinks you want from above item :'))
                print(f'You have selected {no8}  {hd} from {drink_type}.')

        choice2 = str(input('What would you like to do ? \ns-start,f-finish and order :'))



print('Thank you for selecting the welcome drink !')



















