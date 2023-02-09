class dog:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
	def sound(self):
		return "Woof"


fufu = dog("fifi",45)
print(fufu.name)
print(fufu.age)
print(fufu.sound())
