import re


def parse(team:str) -> list:
    """
    :param team: a Pokemon Showdown format team
    :return: The parsed team
    """
    team = team + "\r\n"  # the format of input might not contain a newline
    complete_mon_list = []
    team_pat = re.compile(
        r"(.*)\s@\s(.*)\s?\r\n.*:\s(.*)\s?\r\n(?:Shiny:.*\s?\r\n)?.*:\s(.*)\s?\r\n(.*)\s[Nn].*\s?\r\n(?:IVs:\s.*\s?\r\n)?-\s(.*)\s?\r\n-\s(.*)\s?\r\n-\s(.*)\s?\r\n-\s(.*)\r\n?")

    mon_list = team_pat.findall(team)

    for mon in mon_list:
        temp_li = list(mon)
        temp_li = [field.rstrip() for field in temp_li]
        # mon_name = temp_li[0].split()
        # temp_li[0] = mon_name[0]
        
        complete_mon_list.append(tuple(temp_li))
        team_li = []

        #since we only need to use the mons for now
        #v2 might require moves
        for mon in complete_mon_list:
            team_li.append(mon[0])
        team_li = [x.lower() for x in team_li]

    return team_li


def main():
    pass


if __name__ == "main":
    main()
