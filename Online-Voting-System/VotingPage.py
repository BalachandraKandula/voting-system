import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "Jana Sena\n\n K.Pawan Kalyan", variable = vote, value = "JSP", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"JSP",client_socket)).grid(row = 2,column = 1)
    JSPLogo = ImageTk.PhotoImage((Image.open("img/JSP.jpeg")).resize((45,45),Image.LANCZOS))
    JSPImg = Label(frame1, image=JSPLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "YCP\n\nY.S.Jagan", variable = vote, value = "YCP", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"YCP",client_socket)).grid(row = 3,column = 1)
    YCPLogo = ImageTk.PhotoImage((Image.open("img/YCP.jpeg")).resize((35,48),Image.LANCZOS))
    YCPImg = Label(frame1, image=YCPLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "TDP\n\nChandrababu Naidu", variable = vote, value = "TDP", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"TDP",client_socket) ).grid(row = 4,column = 1)
    TDPLogo = ImageTk.PhotoImage((Image.open("img/TDP.jpeg")).resize((55,40),Image.LANCZOS))
    TDPImg = Label(frame1, image=TDPLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "BJP\n\nPurandeshwari", variable = vote, value = "BJP", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"bjp",client_socket)).grid(row = 5,column = 1)
    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((50,45),Image.LANCZOS))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "Congress\n\nY.S.Sharmila", variable = vote, value = "CONG", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"cong",client_socket)).grid(row = 6,column = 1)
    congLogo = ImageTk.PhotoImage((Image.open("img/cong.jpg")).resize((50,45),Image.LANCZOS))
    congImg = Label(frame1, image=congLogo).grid(row = 6,column = 0)

    Radiobutton(frame1, text = "\nNOTA    \n  ", variable = vote, value = "NOTA", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"nota",client_socket)).grid(row = 7,column = 1)
    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((45,35),Image.LANCZOS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 7,column = 0)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         votingPg(root,frame1,client_socket)
