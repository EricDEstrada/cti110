current_price = int(input())
last_months_price = int(input())

''' Type your code here. '''
change = current_price - last_months_price #Should calculate the change in price

print('This house is $'+str(current_price)+'.'' The change is $'+str(change)+' since last month.')
print('The estimated monthly mortgage is ${:.2f}.'.format(current_price*0.051/12))

