a,b,c= input().split()
a,b,c = float(a), float(b),float(c)
delta = b**2 - 4*a*c
if delta < 0 or a == 0:
  print("Impossivel calcular")
else:
  raizdelta = delta**0.5
  r1 = (-b + raizdelta)/(2*a)
  r2 = (-b - raizdelta)/(2*a)
  print("R1 = {:0.5f}".format(r1))
  print("R2 = {:0.5f}".format(r2))