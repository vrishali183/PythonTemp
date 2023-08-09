from tkinter import *
import requests      
import json


root = Tk()
root.geometry('670x550')

root.overrideredirect(True)



newsupdate=Label(root, text="BBC News Update",font=("Helvetica", 18,'bold'))
newsupdate.place(relx=0.5,rely=0.1,anchor=CENTER)
#--------------------------------------------------------------------------------------------
news1 = Label(root,font=("arial", 12,'bold'), fg="red",wraplength=500,justify=LEFT)
news1.place(relx=0.2,rely=0.17, anchor=W)

news_desc1 = Label(root,font = 'arial 13', fg="black", wraplength=500, justify=LEFT)
news_desc1.place(relx=0.2,rely=0.24, anchor=W)
#--------------------------------------------------------------------------------------------
news2 = Label(root, font=("arial", 12,'bold'), fg ='red', wraplength=500,justify=LEFT)
news2.place(relx=0.2,rely=0.32, anchor=W)

news_desc2 = Label(root , font = 'arial 13',fg="black",wraplength=500, justify=LEFT)
news_desc2.place(relx=0.2,rely=0.41, anchor=W)
#-----------------------------------------------------------------------------------------------
news3 = Label(root,font=("arial", 12,'bold'), fg="red",wraplength=500,justify=LEFT)
news3.place(relx=0.2,rely=0.5, anchor=W)

news_desc3 = Label(root, font = 'arial 13', fg="black",wraplength=500, justify=LEFT)
news_desc3.place(relx=0.2,rely=0.59, anchor=W)

#-----------------------------------------------------------------------------------------------
news4 = Label(root,font=("arial", 12,'bold'), fg="red",wraplength=500,justify=LEFT)
news4.place(relx=0.2,rely=0.68, anchor=W)

news_desc4 = Label(root, font = 'arial 13', fg="black",wraplength=500, justify=LEFT)
news_desc4.place(relx=0.2,rely=0.77, anchor=W)

#----------------------------------------------------------------------------------------------
news5 = Label(root,font=("arial", 12,'bold'), fg="red",wraplength=500,justify=LEFT)
news5.place(relx=0.2,rely=0.85, anchor=W)

news_desc5 = Label(root, font = 'arial 13', fg="black",wraplength=500, justify=LEFT)
news_desc5.place(relx=0.2,rely=0.94, anchor=W)

#------add this link https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=d19e527b11df48c0bcc07c26dfe0a65e
api_request= requests.get("")

open_bbc_page = json.loads() #-----api_request.content

title1 =open_bbc_page["articles"][0]["title"]
print(title1)

desc1 =open_bbc_page["articles"][0]["description"]
print(desc1)

title2=open_bbc_page["articles"][1]["title"]
print(title2)


desc2 =open_bbc_page["articles"][1]["description"]
print(desc2)

title3 =open_bbc_page["articles"][2]["title"]
print(title3) 

desc3 =open_bbc_page["articles"][2]["description"]
print(desc3)


title4 =open_bbc_page["articles"][3]["title"]
print(title3)


desc4 =open_bbc_page["articles"][3]["description"]
print(desc3)

title5 =open_bbc_page["articles"][4]["title"]
print(title3)

desc5 =open_bbc_page["articles"][4]["description"]
print(desc3)

news1["text"]="Title 1: "  + #---title1

news_desc1["text"]= "Description: "+ #---desc1

news2["text"]="Title 2: "+ title2

news_desc2["text"]= "Description: "+ #---desc2

news3["text"]="Title 3: "+ title3

news_desc3["text"]= "Description: "+ #---desc3 

news4["text"]="Title 4: "+ title4

news_desc4["text"]= "Description: "+  #--desc4

news5["text"]="Title 5: "+ title5

news_desc5["text"]= "Description: "+  #--desc5

#-------------    root.mainloop()