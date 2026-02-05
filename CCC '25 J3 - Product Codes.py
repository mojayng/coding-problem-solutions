n = int(input())

for _ in range (n):
    s = input().strip()
    code = []
    total = 0
    i=0
    while i < len(s):
        if s[i].isupper():
            code.append(s[i])
        elif s[i] == '-':
            i+=1
            num = ""
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i+=1    
            total -= int(num)
            continue
        elif s[i].isdigit():
            num = ""
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i+=1    
            total += int(num)
            continue
        i+=1
    
    print("".join(code) + str(total))