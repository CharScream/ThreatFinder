import csv

"""
two ideas for implementation
1. use the team pokemons as the keys and check to see if you have checks for those checks on your team
2. loop through the whole dict and see if you can handle the whole meta game 
"""
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

def smash(team:list) -> list:
    """
    :param team: list of our pokemon team
    :return: list of pokemon that are threats to our team
    """
    mon_di = build_dict("app/static/monCheckList.csv")
    result = []
    threats = [] 
    to_remove = []
    debugging_counter = 0

    for mon in team:
        if mon in mon_di:
            threats += list(mon_di[mon])
        else:
            debugging_counter += 1
            print(debugging_counter)
            print(mon)

    threats = list(set(threats))

    for threat in threats:
        if len(set(team) & set(mon_di[threat])):
            to_remove.append(threat)
    for mon in to_remove:
        threats.remove(mon)
    print(threats)
    # result =list(set(threats))


    return threats


def main():
    temp_di = build_dict("static/monCheckList.csv")
    for keys,values in temp_di.items():
    	if("mega" not in keys):
        	print(keys)

if __name__ == "__main__":
    main()