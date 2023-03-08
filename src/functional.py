def calculation(s: str) -> float:
    ans = -1.0
    if s.find("+") != -1:
        ans = float(s[:s.find("+")])+float(s[s.find("+")+1:])
    elif s.find("-", 1) != -1:
        ans = float(s[:s.find("-", 1)])-float(s[s.find("-", 1)+1:])
    elif s.find("*") != -1:
        ans = float(s[:s.find("*")])*float(s[s.find("*")+1:])
    elif s.find("div") != -1:
        ans = float(s[:s.find("div")])/float(s[s.find("div")+3:])
    return ans
