n = int(input())
s = [input() for _ in range(n)]
ac = s.count('AC')
wa = s.count('WA')
tle = s.count('TLE')
re = s.count('RE')

print(f'AC x {ac}')
print(f'WA x {wa}')
print(f'TLE x {tle}')
print(f'RE x {re}')