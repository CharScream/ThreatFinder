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
    team_set = set(team)
    threats = {}
    result = []
    for mon in team:
        temp_li = team[:]
        temp_li.remove(mon)
        new_set = set(temp_li)
        new_li = list(set(temp_li))

        # for pkmn in mon_di[mon]:
        #     for poke in mon_di[pkmn]:
        #         if poke in new_set:
        #             if pkmn not in threats:
        #                 threats[pkmn] = 1
        #             else:
        #                 threats[pkmn] += 1

        # for pkmn in mon_di[mon]:
        #     if new_set not in set(mon_di[pkmn]):
        #         if pkmn not in threats:
        #             threats[pkmn] = 1
        #         else:
        #             threats[pkmn] += 1

        for pkmn in mon_di[mon]:
            if not any(m in pkmn for m in new_li):
                if pkmn not in threats:
                    threats[pkmn] = 1
                else:
                    threats[pkmn] += 1



        
    for k,v in threats.items():
        print(k,v)


    return result





def main():
    pass

if __name__ == "__main__":
    main()