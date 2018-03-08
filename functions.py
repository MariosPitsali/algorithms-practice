def python_food(a):
    word = "Spam and eggs"
    left_margin = (a - len(word))//2
    print (" "* left_margin + word)
#calling the function 

def center_text(*args, sep=" "):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text))//2
    return (" "* left_margin + text)
    
# s1 = center_text("spam, spam and eggs")    
# print(s1)
# s2 =center_text(890)
# print(s2)
# s3 = center_text("spam and eggs")
# print(s3)
# s4  = center_text("spam,spam, spam and spam")
# print(s4)
# s5 = center_text("spam", "eggs", "ka" ,"po" , "ham", sep =":")
# print(s5)

with open("menu", "w") as menu :
    s1 = center_text("spam, spam and eggs")
    print (s1, file=menu)
    s2 =center_text(890)
    print (s2, file=menu)
    s3 = center_text("spam and eggs")
    print (s3, file=menu)
    s4  = center_text("spam,spam, spam and spam")
    print (s4, file=menu)