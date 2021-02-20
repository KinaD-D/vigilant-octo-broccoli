import random

# 1Ый способ

class Example():

	def __init__(self):
		pass

	def DoMath(colvo, colvotime, chel):
		numbers = [j for j in range(1, colvo + 1)]
		rate = []
		counter = 0
		for i in range(colvo):
			add = random.randint(1, chel)
			rate += [add]
			counter += add
			
		for h in range(colvotime):
			ratecounter = coun = 0
			num = random.randint(1, counter)
			for m in range(colvo):
				if coun < num and num <= coun + rate[ratecounter]:
					print(numbers[ratecounter])
					break
				coun += rate[ratecounter]
				ratecounter += 1
		return 'Конец программы, Первый способ'


colvo = int(input('Введите кол-во случайных чисел '))
colvotime = int(input('Введите кол-во выборов случайностей '))
chel = int(input('Введите лимит редкости чисел '))

print('-->', Example.DoMath(colvo, colvotime, chel), '<--')

input()

class Math():
	def __init__(self):
		pass

	def DoMath(colvo, colvotime, chel):
		rate = []
		for i in range(colvo):
			math = random.randint(1, chel)
			for j in range(math):
				rate += [str(i)]
		for m in range(colvotime):
			print(random.choice(rate))

		return 'Конец программы, Второй способ'

print('-->', Math.DoMath(colvo, colvotime, chel), '<--')
input('')
