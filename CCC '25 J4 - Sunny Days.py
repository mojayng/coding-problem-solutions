n = int(input())
d = []
left = 0
count = 0
maxsun = 0

for i in range (n):
    d.append(input().strip())
    if d[i] == 'P':
        count += 1
    
    while count > 1:
        if d[left] == 'P':
            count -= 1
        left += 1

    maxsun = max(maxsun, i - left + 1)
#have to switch the order of these two if statements because if there is no P, then maxsun will be 0 and we want to print 0 instead of -1
if 'P' not in d:
    maxsun -= 1
print(maxsun)