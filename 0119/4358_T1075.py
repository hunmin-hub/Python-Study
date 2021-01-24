from collections import defaultdict

dic = defaultdict(int)
while True:
    s = input().strip()
    if not s:
        break
    dic[s] += 1

cnt = sum(dic.values())
ret = [key + f" {100 * value / cnt:.4f}" for key, value in dic.items()]
print("\n".join(sorted(ret)))