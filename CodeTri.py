print("#############")

liste=[4,8,7,5]

print('Liste non triée:',liste)

def selectMin(list):
    var=list[0]
    for i in list:
        if var>i:
            var=i
    return var

def triSelect(list):
    result=[]
    while len(list)>0:
        var=selectMin(list)
        list.remove(var)
        result.append(var)
    return result

print('Liste triée par sélection:',triSelect(liste),'\n')

liste=[4,8,7,5]

liste1=[1,4,5,7,8]

liste2=[0,2,3,9]

print('Liste 1 triée:',liste1,'\n','Liste 2 triée:',liste2)

def fusion(list1,list2):
    res=[]
    j=0
    for i in list1:
        while j<len(list2) and i>list2[j]:
            res.append(list2[j])
            j=j+1
        res.append(i)
    res.extend(list2[j:])
    return res

print('Test fusion de liste triée:',fusion(liste1,liste2),'\n')

def triFusion(list):
    if len(list)>1:
        milieu=len(list)//2

        list0=list[0:milieu]
        list1=list[milieu:]
        l1=triFusion(list0)
        l2=triFusion(list1)
        return fusion(l1,l2)
    else:
        return list

liste3=[9,0,7,2,1,8,3,4,6,5]

print('Liste non triée:',liste3)

print('Liste triée par fusion:',triFusion(liste3))