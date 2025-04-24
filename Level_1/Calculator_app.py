# 24.04.20205


def is_number(n):
	n = n.strip()
	if n[0] in "+-":
		n = n[1:]
	return n.isdigit()

print("Simple Calculator - Enter expressions like 4+5 or -10*3")

operations = "+", "-", "*", "/"

while True:
	_input = input("-> ")
	if not _input:
		continue
	if _input.lower() == "exit":
		print("Exit")
		quit()
	tmp = "" + _input[0] * (_input[0] in "+-")
	if tmp:
		_input = _input[1:]
	for i in _input[1:]:
		if i in operations:
			lst = _input.split(i, 1)
			lst = [lst[0]] + [i] + [lst[1]]
			break
	else:
		print("Error: No valid operator found. Use one of + - * /.")
		continue
	lst[0] = tmp + lst[0]
	if is_number(lst[0]) and is_number(lst[2]):
		n1, n2 = int(lst[0]), int(lst[2])
	else:
		print("Error: is not a valid number.")
		continue
	if lst[1] == "+":
		print(n1 + n2)
	elif lst[1] == "-":
		print(n1 - n2)
	elif lst[1] == "*":
		print(n1 * n2)
	elif lst[1] == "/":
		if n2:
			print(n1 / n2)
		else:
			print("Error: Division by zero is not allowed.")
	else:
		print("Error: Unknown operator.")
