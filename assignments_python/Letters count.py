degerim = 'hippo runs to us!'

countdict= {}
for l in degerim :
    if l.isalpha():
        if l in countdict:
                countdict[l] +=1
        else:
                countdict[l]= 1

print(countdict)