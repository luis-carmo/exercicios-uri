p1 = input().split()
x1 = float(p1[0])
y1 = float(p1[1])
p2 = input().split()
x2 = float(p2[0])
y2 = float(p2[1])
distancia = (x2 - x1)**2 + (y2 - y1)**2
distf = distancia ** 0.5
print ('{:0.4f}'.format(distf))