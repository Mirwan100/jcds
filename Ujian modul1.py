def Hashtag(string) :
    hastag = "#"
    string = str(string)
    if string == "" :
        return False
    string = list((string.split(" ")))
    for kata in string :
        if kata == " " :
            string.remove(kata)
        kata = kata[0].upper() + kata[1:]
        hastag += kata
    if len(hastag) > 140 :
        return False
    else :
        return hastag
print(Hashtag("Saya makan nasi Goreng"))

def create_phone_number(number):
    phone_number = ""
    for a in number :
        if type(a) != int or a < 0 or a > 9  :
            return 'Input 10 digits of number!'

    if len(number) == 10 :
        phone_number += "(" + str(number[0]) + str(number[1]) + str(number[2]) + ")" + str(number[3]) + str(number[4]) + str(number[5])+ "-" + str(number[6])+ str(number[7])+ str(number[8])+ str(number[9])
    else : 
        phone_number = 'Input 10 digits of number!'
    return phone_number
    
print(create_phone_number([1,5,3,4,5,6,7,8,9,0]))'''

def sort_odd_even(list_num):
    ganjil = []
    genap = []
    count_genap = []
    count_ganjil = []
    for num in list_num :
        if num % 2 == 0 :
            genap.append(num)
            count_genap.append(list_num.index(num))
        else :
            ganjil.append(num)
            count_ganjil.append(list_num.index(num))
    genap.sort(reverse = True)
    ganjil.sort()
    for a in count_genap :
        list_num[a] = genap[count_genap.index(a)]
    for b in count_ganjil :
        list_num[b] = ganjil[count_ganjil.index(b)]
    return list_num

print(sort_odd_even([5,3,2,8,1,4]))

def hollowTriangle(n) :
    if n == 1:
        return "#"
    elif n == 2 :
        return "_#_"+ '\n' + "###"
    elif n> 2:
        k = ""
        n= n+1
        for i in range(1,n-1):
            k += ('_'*(2*n-i-1) + "#"+'_'*(2*i-3)+"#"*(i!=1) +'_'*(2*n-i-1)) +'\n'
        k = k +('#'*(2*n-1)*2)
        return k
print(hollowTriangle(4))
