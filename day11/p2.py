'''
--- Part Two ---
You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage an item no longer causes your worry level to be divided by three.

Unfortunately, that relief was all that was keeping your worry levels from reaching ridiculous levels. You'll need to find another way to keep your worry levels manageable.

At this rate, you might be putting up with these monkeys for a very long time - possibly 10000 rounds!

With these new rules, you can still figure out the monkey business after 10000 rounds. Using the same example above:

== After round 1 ==
Monkey 0 inspected items 2 times.
Monkey 1 inspected items 4 times.
Monkey 2 inspected items 3 times.
Monkey 3 inspected items 6 times.

== After round 20 ==
Monkey 0 inspected items 99 times.
Monkey 1 inspected items 97 times.
Monkey 2 inspected items 8 times.
Monkey 3 inspected items 103 times.

== After round 1000 ==
Monkey 0 inspected items 5204 times.
Monkey 1 inspected items 4792 times.
Monkey 2 inspected items 199 times.
Monkey 3 inspected items 5192 times.

== After round 2000 ==
Monkey 0 inspected items 10419 times.
Monkey 1 inspected items 9577 times.
Monkey 2 inspected items 392 times.
Monkey 3 inspected items 10391 times.

== After round 3000 ==
Monkey 0 inspected items 15638 times.
Monkey 1 inspected items 14358 times.
Monkey 2 inspected items 587 times.
Monkey 3 inspected items 15593 times.

== After round 4000 ==
Monkey 0 inspected items 20858 times.
Monkey 1 inspected items 19138 times.
Monkey 2 inspected items 780 times.
Monkey 3 inspected items 20797 times.

== After round 5000 ==
Monkey 0 inspected items 26075 times.
Monkey 1 inspected items 23921 times.
Monkey 2 inspected items 974 times.
Monkey 3 inspected items 26000 times.

== After round 6000 ==
Monkey 0 inspected items 31294 times.
Monkey 1 inspected items 28702 times.
Monkey 2 inspected items 1165 times.
Monkey 3 inspected items 31204 times.

== After round 7000 ==
Monkey 0 inspected items 36508 times.
Monkey 1 inspected items 33488 times.
Monkey 2 inspected items 1360 times.
Monkey 3 inspected items 36400 times.

== After round 8000 ==
Monkey 0 inspected items 41728 times.
Monkey 1 inspected items 38268 times.
Monkey 2 inspected items 1553 times.
Monkey 3 inspected items 41606 times.

== After round 9000 ==
Monkey 0 inspected items 46945 times.
Monkey 1 inspected items 43051 times.
Monkey 2 inspected items 1746 times.
Monkey 3 inspected items 46807 times.

== After round 10000 ==
Monkey 0 inspected items 52166 times.
Monkey 1 inspected items 47830 times.
Monkey 2 inspected items 1938 times.
Monkey 3 inspected items 52013 times.
After 10000 rounds, the two most active monkeys inspected items 52166 and 52013 times. Multiplying these together, the level of monkey business in this situation is now 2713310158.

Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable. Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?
'''

import re
try:
    from tqdm import tqdm
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'tqdm'])
    from tqdm import tqdm


class badMonkey():

	def __init__(self,number:int, bag:list,operation:tuple, test:int, target:tuple):
		print(f"Creating monkey {number}...")
		self.number = number
		self.bag = bag
		self.itemsInspected = 0
		self.operation = operation
		self.test = test
		self.target = target
        

	def getInfo(self):
		print(f"Monkey {self.number} info:")
		print(f"Bag: {self.bag}")
		print(f"Items Inspected: {self.itemsInspected}")
		return ''

	def inspectBag(self, verbose:bool = False):
		'''
		Returns a json of Target and item
		'''
		if verbose:
			print(f"Monkey {self.number} is Inspecting Items in Bag...")
		returnBag = []
		while self.bag:
			self.itemsInspected += 1
			item = self.bag.pop(0)

			item = self.newOperation(item)//3
			# print(self.operation)
			returnBag.append({"Target": self.findTarget(item),
			"Concern": item})
		return returnBag

	def findTarget(self,concern:int):
		# if not 0, return the true value for target
		if not concern % self.test:
			return self.target[0]
		return self.target[1]

	def newOperation(self, concern:int):
		if self.operation[0] == '+':
			concern += self.operation[1]
		if self.operation[0] == '-':
			concern -= self.operation[1]
		if self.operation[0] == '*':
			concern *= self.operation[1]
		if self.operation[0] == '/':
			concern /= self.operation[1]
		if self.operation[0] == '**':
			concern *= concern
		return concern
	
	def catchItem(self, concern:int):
		self.bag.append(concern)

	def itemsInspected(self):
		return self.itemsInspected


def getNumbers(text:str):

	return re.findall('[0-9]+', text)

def processMonkey(monkey:list):
	monkeyNumber = int(getNumbers(monkey[0])[0])
	
	#create monkey bag
	bag = []
	concern = getNumbers(monkey[1])
	for num in concern:
		bag.append(int(num))


	if getNumbers(monkey[2]):
		operation = re.search('[-+\\*]+', monkey[2])[0]
		operationMod = int(getNumbers(monkey[2])[0])
	else:
		operation = '**'
		operationMod = '0'

	test = int(getNumbers(monkey[3])[0])
	target = (int(getNumbers(monkey[4])[0]),int(getNumbers(monkey[5])[0]))

	# print(monkeyNumber, bag, operation, operationMod, test, TF)
	return badMonkey(monkeyNumber, bag, (operation, operationMod), test, target)



with open("./input.txt", "r") as f:
    inputFile = [monkey.split('\n') for monkey in f.read().split('\n\n')]

monkeys = []

for item in inputFile:
	monkeys.append(processMonkey(item))


for monkey in monkeys:
	print(monkey.getInfo())

# print(monkeys[0].inspectBag())

for count in tqdm(range(10000)):
	for monkey in monkeys:
		items = monkey.inspectBag()
		for item in items:
			monkeys[item['Target']].catchItem(item['Concern'])

count = []
for monkey in monkeys:
	count.append(monkey.itemsInspected)
count = sorted(count)
print(count[-1]*count[-2])