#1
user_height = float(input('Enter height in cm'))
user_weight = float(input('Enter weight in kg'))
recommended_weight = user_weight/(user_height**2)
if recommended_weight < 18.5:
    print('underweight')
elif recommended_weight >=18.5 and recommended_weight <=25:
    print('normal weight')
elif recommended_weight >=25 and recommended_weight <=30:
    print('overweight')
else:
    print('odesity')   
    
#2
online_store = []
price_product = 0
vat = 18
nds = price_product*vat/100
for x in range(0,5):
    name = input('Name product')
    price = float(input('Price product'))
    product = {'name': name,
        'price': price}
online_store.append([product])
if product == 50:
    print('10 azn kupon qazandiniz')
elif product >=100:
    print('15 azn kupon qazandiniz')
else:
    print('bextinizi bir daha sinayin')
    
#3
customer = int(input('1(car),2(plane),3(train)'))
way = float(input('How many km'))
if customer == 1:
    print('Payment', way * 0.5)
elif customer == 2:
    print('Payment', way * 1)
else:
    print('Payment', way*2)    
         