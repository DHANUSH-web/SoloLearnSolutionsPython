# simple password validator
password = input("Enter a password: ")
sp_chr = ['!', '@', '#', '$', '%', '&', '*']

cnt_num = 0
cnt_chr = 0

for c in password:
    if c.isdigit():
        cnt_num += 1
    elif c in sp_chr:
        cnt_chr += 1

if cnt_num >= 2 and cnt_chr >= 2 and len(password) >= 7:
    print("Strong")
else:
    print("Weak")
