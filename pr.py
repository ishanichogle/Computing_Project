from PIL import Image
z=1
star=Image.open("start.jpg")
star.show()
print("Lets start!!!Please type k in input to continue")
rr=input()
q1i=Image.open("dumbledore.jpg")
q1i.show()
print("enter your answer to question 1 here")
r1=input()
q2i=Image.open("phoenix.jpg")
q2i.show()
print("enter your answer to question 2 here")
r2=input()
q3i=Image.open("q3.jpg")
q3i.show()
print("enter your answer to question 2 here")
r3=input()
q4i=Image.open("q4.jpg")
q4i.show()
print("enter your answer to question 4 here")
r4=input()
q5i=Image.open("q5.jpg")
q5i.show()
print("enter your answer to question 5 here")
r5=input()
mydict=dict()
frequency=[]
finalletter=[]
rad=[r1,r2,r3,r4,r5]
for r in rad:
    if r not in mydict:
        mydict[r]=1
    else:
        mydict[r]=mydict[r]+1
for letter in mydict:
    frequency.append(mydict[letter])
maxf=max(frequency)
for letter in mydict:
    if mydict[letter]==maxf:
        finalletter.append(letter)
finalletter.sort()
house=finalletter[0]
if house=='a':
    im=Image.open("gryffindor.jpg")
    im.show()
elif house=='b':
    im=Image.open("ravenclaw.jpg")
    im.show()
elif house=='c':
    im=Image.open("huffle.jpg")
    im.show()
elif house=='d':
    im=Image.open("slytherin.jpg")
    im.show()
