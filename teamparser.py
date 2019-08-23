import re

def parse(team):
    complete_mon_list = []
    team_pat = re.compile(
        r"(.*)\s@\s(.*)\s?\r\n.*:\s(.*)\s?\r\n(?:Shiny:.*\s?\r\n)?.*:\s(.*)\s?\r\n(.*)\s[Nn].*\s?\r\n(?:IVs:\s.*\s?\r\n)?-\s(.*)\s?\r\n-\s(.*)\s?\r\n-\s(.*)\s?\r\n-\s(.*)\r\n?")
    
    mon_list = team_pat.findall(team)

    print(type(mon_list))

    for mon in mon_list:
        temp_li = list(mon)
        temp_li = [field.rstrip() for field in temp_li]
        complete_mon_list.append(tuple(temp_li))

    for mon in complete_mon_list:
        print(mon)

    return complete_mon_list


def main():
    pass


if __name__ == "main":
    main()
