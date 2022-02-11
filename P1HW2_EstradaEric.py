    # This is a calculator for figuring out amount of pizzas needed for a group students
    # 2/10/2022
    # CTI-110 P1HW2 - Pizza Order
    # Eric Estrada
    #

    #number of students 
numstudents = int(input())

# Slices per pizza
pizzaslices = numstudents * 3

#number of pizzas for students required.
wholepizzas = numstudents//2

#Calculator results for pizzas needed
print('How many students do you want to order pizza for?',numstudents)
print('----Pizza--------')
print('Number of Students:',numstudents)
print('Pizza Slices Needed:',pizzaslices)
print('Pizzas Needed:',wholepizzas)
print('--------------------------')
