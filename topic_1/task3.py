import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
D = b**2 - 4*а*с
if D > 0:
	x1 = (-b + math.sqrt(D)) / (2*a)
	x2 = (-b - math.sqrt(D)) / (2*a)
	print(f"рівняння має два кореня: x1 = {x1}, x2 = {x2}")
elif D == 0:
	x = -b / (2*а)
	print(f"рівняння має лише один корінь: х = {x}")
else:
	print("рівняння коренів немає")
