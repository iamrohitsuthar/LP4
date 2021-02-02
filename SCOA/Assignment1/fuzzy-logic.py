A = {"x1":0.5, "x2":0.7, "x3":0}
B = {"x1":0.8, "x2":0.2, "x3":1}

print("Fuzzy Set A:")
print(A)
print("Fuzzy Set B:")
print(B)

res = dict()
print("\nUnion Operation Result")
for key in A:
	res[key] = max(A[key], B[key])
print(res)
res.clear()

print("\nIntersection Operation Result")
for key in A:
	res[key] = min(A[key], B[key])
print(res)
res.clear()

print("\nComplement Operation on Fuzzy Set A")
for key in A:
	res[key] = round((1 - A[key]),1)
print(res)
res.clear()

print("\nDifference Operation Result")
for key in A:
	res[key] = round(min(A[key], 1 - B[key]),1)
print(res)
res.clear()

print()
X = {"x1":0.6, "x2":0.2, "x3":0.3}
Y = {"y1":0.7, "y2":0.3, "y3":0.4}
Z = {"z1":0.9, "z2":0.5, "z3":0.6}
print("Fuzzy Set X:")
print(X)
print("Fuzzy Set Y:")
print(Y)
print("Fuzzy Set Z:")
print(Z)

rows, cols = (3, 3) 
relation1 = [[0 for i in range(cols)] for j in range(rows)] 
relation2 = [[0 for i in range(cols)] for j in range(rows)] 

print("\nFuzzy Relation1 by Cartesian product of Fuzzy Set X and Y")
print("\t{}\t{}\t{}".format(*list(Y.keys())))
i = 0
for x_key in X:
	j = 0
	print(x_key, end = "\t")
	for y_key in Y:
		print(min(X[x_key], Y[y_key]), end = "\t")
		relation1[i][j] = min(X[x_key], Y[y_key])
		j += 1
	print()
	i += 1

print("\nFuzzy Relation2 by Cartesian product of Fuzzy Set Y and Z")
print("\t{}\t{}\t{}".format(*list(Z.keys())))
i = 0
for y_key in Y:
	j = 0
	print(y_key, end = "\t")
	for z_key in Z:
		print(min(Y[y_key], Z[z_key]), end = "\t")
		relation2[i][j] = min(Y[y_key], Z[z_key])
		j += 1
	print()
	i += 1

print("\nMax-Min Composition of Fuzzy Relation1 and Relation2")
print("\t{}\t{}\t{}".format(*list(Z.keys())))
for i in range(0,3):
	print("x{}".format(i+1), end="\t")
	for j in range(0,3):
		l1 = list()
		for k in range(0,3):
			l1.append(min(relation1[i][k],relation2[k][j]))
		print(max(l1), end = "\t")
	print()