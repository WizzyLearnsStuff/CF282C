
def main():
    s = input()
    b = input()
    l = ("YES", "NO")
    if len(s) != len(b):
        print("NO")
        return
        
    print(l[all(i == '0' for i in s) ^ all(i == '0' for i in b)])

main()
