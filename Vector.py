import math
import random

class Vector(object):
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z


	def DoMath(self, vector):

		print('Длина векторов ', math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z))

		print('Скалярное произведение ', self.x * vector.x + self.y * vector.y + self.z * vector.z)

		print ('векторное произведение', self.y * vector.z - self.z * vector.y, self.z * vector.x - self.x * vector.z, self.x * vector.y - self.y * vector.x)

		print('Косинус угла', 
			(self.x * vector.x + self.y * vector.y + self.z * vector.z) / (math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z) * math.sqrt(vector.z * vector.z + vector.y * vector.y + vector.z * vector.z)))

		print('Сумма векторов', self.x + vector.x, self.y + vector.y, self.z + vector.z)

		print('Разность векторов', self.x - vector.x, self.y - vector.y, self.z - vector.z)

		return 'Конец программы'

x1 = int(input('Введите x1 '))
y1 = int(input('Введите y1 '))
z1 = int(input('Введите z1 '))
x2 = int(input('Введите x2 '))
y2 = int(input('Введите y2 '))
z2 = int(input('Введите z2 '))

vector = Vector(x1, y1, z1)
vec = Vector(x2, y2, z2)


print('-->', vector.DoMath(vec), ' <--')
input('')
