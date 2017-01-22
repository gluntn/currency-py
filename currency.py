def breakdown(input: int) -> int:
	nok = [1, 5, 10, 20, 50, 100, 500, 1000]
	fin = []

	while input > 0:
		for i in range(0, len(nok)):
			try:
				if input >= nok[i] and input < nok[i + 1]:
					input -= nok[i]
					fin.append(nok[i])
			except IndexError:
				input -= nok[len(nok)-1]
				fin.append(nok[len(nok)-1])
	return fin[::-1]

print(breakdown(14))
print(breakdown(517))
print(breakdown(1432))
print(breakdown(111))
print(breakdown(0))



