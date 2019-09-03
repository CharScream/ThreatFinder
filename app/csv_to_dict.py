import csv

def build_dict(file_name:str) -> dict:
	"""
	:param file_name: name of file to be read
    :return: dictionary of tuples, where the key is the pokemon and the value is a tuple of counters
	"""
	di = {}
	with open(file_name, newline="") as csvfile:
		reader = csv.reader(csvfile, delimiter= ",", quotechar="|")
		for row in reader:
			row_li = list(filter(None,row))
			di[row_li[0]] = tuple(row_li[1:])
	
	return di

def main():
	a = build_dict("monChecklist.csv")
	print(a)

if __name__ == "__main__":
	main()
