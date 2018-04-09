import re

def main():
    data=[]
    Number = int(input("input:"))
    data = input()
    a=0
    cha=[]
    all = re.findall("\d+",data)
    # all = ["3","1","2","6"]
    all2 =[]
    for i in all:
        all2.append(int(i))
    for a in range(len(all2)):
        for b in range(len(all2)):
            if all2[a]>all2[b]:
                all2[a],all2[b] =  all2[b],all2[a]
    for c in range(len(all2)):
        if c == len(all2)-1:
            print ("Yes")
            return
        if c == 0:
            sa = all2[c] -all2[c+1]
        else:
            if  all2[c] -all2[c+1] != sa:
                print ("NO")
                return


if __name__ == '__main__':
    main()
