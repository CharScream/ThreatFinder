import re


def parse(team):
    team_pat = re.compile(
        r"\b(.*)\s@\s(.*)\s\r\n.*:\s(.*)\s\r\n.*:\s(.*)\s\r\n(.*)\s[Nn].*\r\n(?:[Ss].*\s.*\r\n)?(?:IVs:\s.*\s\r\n)?-\s(.*)\s\r\n-\s(.*)\s\r\n-\s(.*)\s\r\n-\s(.*)\r\n")
    mon_list = team_pat.findall(team)
    for mon in mon_list:
        print(mon)
    return mon_list


def main():
    pass


if __name__ == "main":
    main()
