s1 = input()
s2 = input()
s3 = input()
t = list(input())

ans = []
for i in t:
    if i=='1':
        ans.append(s1)
    elif i=='2':
        ans.append(s2)
    else:
        ans.append(s3)

print(''.join(ans))