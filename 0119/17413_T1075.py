s = input()
rev = True
start = 0
end = 0
ret = []

for idx, c in enumerate(s):
    end=idx
    if c == '<':
        ret.append("".join(reversed(s[start:end])))
        start=idx
        rev=False
    if c == '>':
        ret.append(s[start:end+1])
        start=idx+1
        rev=True
    if c == ' ' and rev:
        ret.append("".join(reversed(s[start:end])))
        ret.append(' ')
        start=idx+1
ret.append("".join(reversed(s[start:end+1])))
print("".join(ret))