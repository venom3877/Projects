#a viewer used a spam comment find the spam comment and highlight it
user=input("enter your comment here : ")
if("make lot of monmey" in user):
    spam=True
elif("buy this" in user):
    spam=True
elif("click this link" in user):
    spam=True
elif("watch this video now" in user):
    spam=True
else:
    spam=False
if(spam):
    print("this comment is a spam,your ID has been restricted") 
else:print("enjoy the show")
