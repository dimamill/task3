import sys
s=[]
def scob(l,r):
    return l+r in["()","[]","{}"]
for a in input():
    if a in'([{':
        s.append(a)
    else:
        if len(s)==0:
            print(False)
            sys.exit(0)
        if not scob(s.pop(),a):
            print(False)
            sys.exit(0)
    if len(s)==0:
        print(True)
    else:
        print(False)
