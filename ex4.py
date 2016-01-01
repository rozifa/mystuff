#The "=" sign  is the assignment operator. It tells python the value of a 
#variable name. 

#Assign value of 100 to car variable
cars = 100.0

#There are 4 units of space within a car and this is assigned to space in car
space_in_a_car = 4.0

#Assigns number of drivers as 30 
drivers = 30

#Number of passengers is assigned to be 90
passengers = 90

#Number of cars not being driven is equal to the value of 
#the cars variable - the value fo the drivers variable
cars_not_driven = cars - drivers

#There is one driver per car so logicically, the number of cars driven will be
#equal to the number of drivers specified. These two variable values are equal.
cars_driven = drivers

#Carpool capacity is logically the total space available in all cars. 
#This is equal to the number of cars driven multiplied by the space in each car
carpool_capacity = cars_driven * space_in_a_car

#Average passengers is equal to total passengers distributed evenly between all
#cars.
average_passengers_per_car = passengers / cars_driven

#Print readable text that references predefined variables to answer questions.
print "There are", cars, "cars available."
print "There are only", drivers, "Drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#If python gave an error in line 8 that said car_pool_capacity was not defined
#this would mean no value was assigned to that variable name. In my code, 
#The value was assigned to a different variable name: carpool_capacity and #this specific name must be used when referencing the value of that variable. 
