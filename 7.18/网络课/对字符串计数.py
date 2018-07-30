


str=input('')
str1=str.strip()
index=0
count=0
while index<len(str1):
    while  str1[index]!=' ':
        index+=1
        if index==len(str1):
            break
    count +=1
    if index==len(str):
        break
while str1[index]==' ':
        index+=1

