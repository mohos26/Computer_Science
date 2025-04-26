# 25.04.2025


import os
import json

def ft_get_id(lst):
	ids = []
	for arg in lst:
		ids.append(arg["id"])
	return max(ids) + 1

print("------------ MANUAL ------------")
print("--- show: Show List Of Tasks ---")
print("--- undo: UnDo Task ------------")
print("--- save: Save Your Tasks ------")
print("--- exit: Exit Programe --------")
print("--- add : add task -------------")
print("--- rm  : remove task ----------")
print("--- do  : Do task --------------")
print("--------------------------------")

if os.path.exists("todo_data.json"):
	with open("todo_data.json", 'r') as f:
		lst = json.load(f)
else:
	lst = []

while True:
	_input = input("-> ").strip().lower()
	if not _input:
		continue
	elif _input == "exit":
		print("exit")
		quit()
	elif _input == "show":
		flag = False
		for arg in sorted(lst, key=lambda d: d["do"]):
			if not flag and arg["do"]:
				print("----- Completed -----")
				flag = True
			print(f"* {arg['id']}: {arg['name']}")
			if arg["description"]:
				print(f"\t{arg['description']}")
	elif _input == "add":
		d = {
			"name": input("Type name: "),
			"description": input("Type description: "),
			'do': False,
			"id": ft_get_id(lst)
		}
		lst.append(d)
		print("Successful")
	elif _input == "rm":
		v_id = int(input("Type id: "))
		flag = False
		for arg in lst:
			if arg["id"] == v_id:
				flag = True
				lst.remove(arg)
		if flag:
			print("Successful")
		else:
			print(f"Error: id: {v_id} Not Found")
	elif _input == "do":
		v_id = int(input("Type id: "))
		flag = False
		for arg in lst:
			if arg["id"] == v_id:
				flag = True
				arg["do"] = True
		if flag:
			print("Successful")
		else:
			print(f"Error: id: {v_id} Not Found")
	elif _input == "undo":
		v_id = int(input("Type id: "))
		flag = False
		for arg in lst:
			if arg["id"] == v_id:
				flag = True
				arg["do"] = False
		if flag:
			print("Successful")
		else:
			print(f"Error: id: {v_id} Not Found")
	elif _input == "save":
		with open("todo_data.json", 'r') as f:
			f.write(json.dumps(lst, indent=4))
		print("Successful")
	else:
		print("Error")
