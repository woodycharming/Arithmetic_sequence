def loging(Name,data):
    print (Name,data)

def main():
    source = [0,0,0,1,1,2,3,3,3,2,3,3,0,0]
    a = 0
    all=[]
    res=[]
    for i in source:
        all.append(str(i))
    frist = ""
    group = []
    for i in all:
        if i == frist:
            group.append(i)
            if i == all[-1]:
                res.append(group)
        else:
            if group!=[]:
                res.append(group)
            group=[]
            group.append(i)
            frist=i
    loging("res",res)

if __name__ == '__main__':
    main()
