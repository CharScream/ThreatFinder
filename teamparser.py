import re
def parse(team):
    team_pat = re.compile(r"\b(.*)\s@\s(.*)\r\n.*:\s(.*)\r\n.*:\s(.*)\r\n(.*)\s[Nn].*\r\n")
    a = team_pat.findall(team)
    for i in a:
        print(i)

def main():

    pass


if __name__ == "main":
    main()

