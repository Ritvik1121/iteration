import math
# Make a local change
# doing the same thing once for each member of a list

# iteration pattern

# [1, 5, 7 ,8 , 4, 3]

def iterate(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item
def add_one(list):
	#standard fot loop with range
	for i in range(0, len(list)):
		list[i] += 1
	return list

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern
# exclude a calculation from list members

def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"


# accumulation pattern - a type of iteration
# keep track of other data as we go

def sum(numbers):
	total = 0
	for n in numbers:
		total += n
	
	return total

def max(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = n

	return current_max

#Homework - >
	# a) Write a function that finds the average of the scores
def average(numbers):
	total = 0
	for n in numbers:
		total += n
	return total/ len(numbers)
	# b) write a second function that also finds the average but drops the lowest two scores


#def remove_n_smallest(lst, n):.


    
def fizz_buzz(numbers):
	result = []
	for n in numbers:
		if n % 3 == 0 and n % 5 == 0:
			result.append("Fizzbuzz")
		elif n % 3 == 0:
			result.append("Fizz")
		elif n % 5 == 0:
			result.append("Buzz")
		else:
			result.append('Bazz')
	return result
		
def alternating_sum(numbers):
	subtract = False
	total = 0
	for n in numbers:	
		if subtract == False:
			total += n
			subtract = True
		elif subtract == True:
			total -= n
			subtract = False
	return total

def sum_outside(numbers, min, max):
	total = 0
	for i in range(0, len(numbers)):
		if numbers[i] < min:
			total += numbers[i]
		elif numbers[i] >= max:
			total += numbers[i]		
	return total

def count_close_remainders(numbers, divisor):
	total = 0
	for i in range(0, len(numbers)):
		if numbers[i] % divisor == 0 or numbers[i] % divisor == 1 or numbers[i] % divisor == 4:
			total += 1
	return total

def double_down(numbers, target):
	result = [maybe_doubled(numbers[0], numbers[0], target)]
	for i in range(1, len(numbers)):
		result.append(maybe_doubled(numbers[1], numbers[i-1], target ))
	return result

def maybe_doubled(n, prev_n, target):
	distance = abs(n - target)
	if n < prev_n or distance <=3:
		return 2 * n
	return n

def standard_dev(numbers):
	total = 0
	result = []
	for i in range(0, len(numbers)):
		result.append(numbers[i] - average(numbers)) 
	for i in range(0, len(result)):
		total += result[i] * result[i]
	return math.sqrt(total/len(numbers))