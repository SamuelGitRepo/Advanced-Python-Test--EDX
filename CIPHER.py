
CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))

#finding the index of each letter in a format of row and column indexes
def find_letter(m):
  m=m.upper()
  for i in range(len(CIPHER)):
    if m[0] in CIPHER[i]:
      aa = [i,CIPHER[i].index(m[0])]
    if m[1] in CIPHER[i]:
      bb = [i,CIPHER[i].index(m[1])] 
  return aa,bb
print(find_letter('nm'))
def encrypt(word):
    '''initializing the final output and the word'''
    result=''
    ww=""
    for char in word:
        if char.isalpha():
            if char.upper()=='J':
                ww+='I'
            else:
                ww+=char.upper()
    if (len(ww)%2)!=0:
        ww+='X'
    w = [ww[i:i+2]for i in range(0,len(ww),2)] #splitting the word
    #same case resolve
    for i in range(len(w)):
        if w[i][0]==w[i][1]:
            w[i]= w[i][0]+'X'

    for letter in w:
        #row case
        if find_letter(letter)[0][0]==find_letter(letter)[1][0]:
            if find_letter(letter)[0][1]==4:
                result += CIPHER[find_letter(letter)[0][0]][0]
            else:
                result += CIPHER[find_letter(letter)[0][0]][find_letter(letter)[0][1]+1]
            if find_letter(letter)[1][1]==4:
                result += CIPHER[find_letter(letter)[0][0]][0]
            else:
                result += CIPHER[find_letter(letter)[0][0]][find_letter(letter)[1][1]+1]
        #Column Case
        elif find_letter(letter)[0][1]==find_letter(letter)[1][1]:
            if find_letter(letter)[0][0]==4:
                result += CIPHER[0][find_letter(letter)[0][1]]
            else:
                result += CIPHER[find_letter(letter)[0][0]+1][find_letter(letter)[1][1]]
            if find_letter(letter)[1][0]==4:
                result += CIPHER[0][find_letter(letter)[0][1]]
            else:
                result += CIPHER[find_letter(letter)[1][0]+1][find_letter(letter)[1][1]]
        #Rectangle Case
        elif (find_letter(letter)[0][0]!=find_letter(letter)[1][0]) and (find_letter(letter)[0][1]!=find_letter(letter)[1][1]):
            result += CIPHER[find_letter(letter)[0][0]][find_letter(letter)[1][1]] 
            result += CIPHER[find_letter(letter)[1][0]][find_letter(letter)[0][1]]
        else:
            result+=""   
    return result
def decrypt(word):
    result=''
    w=''
    w = [word[i:i+2]for i in range(0,len(word),2)] #splitting the word
    for letter in w:
        #row case
        if find_letter(letter)[0][0]==find_letter(letter)[1][0]:
            if find_letter(letter)[0][1]==0:
                result += CIPHER[find_letter(letter)[0][0]][4]
            else:
                result += CIPHER[find_letter(letter)[0][0]][find_letter(letter)[0][1]-1]
            
            if find_letter(letter)[1][1]==0:
                result += CIPHER[find_letter(letter)[0][0]][4]
            
            else:
                result += CIPHER[find_letter(letter)[0][0]][find_letter(letter)[1][1]-1]
            
        #Column Case
        elif find_letter(letter)[0][1]==find_letter(letter)[1][1]:
            if find_letter(letter)[0][0]==0:
                result += CIPHER[4][find_letter(letter)[0][1]]
            else:
                result += CIPHER[find_letter(letter)[0][0]-1][find_letter(letter)[0][1]]
            if find_letter(letter)[1][0]==0:
                result += CIPHER[4][find_letter(letter)[1][1]]
            else:
                result += CIPHER[find_letter(letter)[1][0]-1][find_letter(letter)[1][1]]
        #Rectangle Case
        elif (find_letter(letter)[0][0]!=find_letter(letter)[1][0]) and (find_letter(letter)[0][1]!=find_letter(letter)[1][1]):
            result += CIPHER[find_letter(letter)[0][0]][find_letter(letter)[1][1]] 
            result += CIPHER[find_letter(letter)[1][0]][find_letter(letter)[0][1]]
        else:
            result+=""  


    return w,result

#print(encrypt("psdr"))
#print(encrypt("7d pSSa6575ammuejmni"))
#print(encrypt("SSa6575ammuejmn"))
print(encrypt("ps. Hello, worlds"))
print(decrypt('QLGRQTVZIBTYQZ'))
#print(encrypt("dvnrgklsfgrn"))
#print(encrypt("dgazbm"))
#"QLGRQTVZIBTYQZ"

