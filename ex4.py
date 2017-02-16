#coding=utf-8
#定义了车数，每辆车的空位，司机数量，乘客总数，
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#不能开的车，就是车的总量减去司机的数量
cars_not_driven = cars - drivers
#能开走的车数与司机数相同
cars_driven = drivers
#车的总容量 = 能开的车数量 * 每辆车的容量
carpool_capacity = cars_driven * space_in_a_car
#平均每辆车的人数 = 总的乘客数量 / 
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be ", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
