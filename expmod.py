import sys

def expmod(a, b, n):
	rexpo = 1
	pot = a % n
	while b > 0:
		if b % 2 == 1:
			rexpo = (rexpo * pot) % n
		b = b / 2
		pot = (pot * pot) % n
	return rexpo
	
if len(sys.argv) != 4:
	print 'El numero de argumentos es invalido'
else:
	isnumber = True
	ispositive = True
	for i in xrange(1, len(sys.argv)): # Desde sys.argv[1] hasta sys.argv[len(sys.argv) - 1]
		if not sys.argv[i].isdigit(): # Si alguno de los argumentos no son numeros
			isnumber = False
			break
		elif not int(sys.argv[i]) > 0: # Si alguno de los argumento (numeros) no son mayores que 0
			ispositive = False # Si alguno de los argumentos que si son numeros no son mayores que cero
			break
	if isnumber and ispositive:
		a = int(sys.argv[1])
		b = int(sys.argv[2])
		n = int(sys.argv[3])
		rexpo = expmod(a, b, n)
		print rexpo
	else:
		print 'Todos los argumentos deben ser numeros enteros mayores que 0'
