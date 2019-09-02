import csv

# string = "Apple,Red,Green,Round,Fruit,,"

# li = string.split(",")
# for i in li:
#   print(i)
# print(li)

# li = list(filter(None, li))

# print(li)

def build_dict(file_name:str) -> dict:
	di = {}
	with open(file_name, newline="") as csvfile:
		reader = csv.reader(csvfile, delimiter= ",", quotechar="|")
		for row in reader:
			row_li = list(filter(None,row))
			di[row_li[0]] = tuple(row_li[1:])
	
	return di

def main():
	print("hey")
	build_dict("monChecklist.csv")

if __name__ == "__main__":
	main()
