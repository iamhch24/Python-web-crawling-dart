# quty5도 있음
from tkinter import *

class GUI():
    def __init__(self):
        self.tkhandler = Tk()
        self.tkhandler.geometry("500x500")
        self.tkhandler.title("자동화 프로그램")
        self.label_title = Label(self.tkhandler, text='자동화 프로그램입니다.')
        #배치 - 한줄씩 쌓인다. : pack()
        self.label_title.pack()
        self.btn = Button(self.tkhandler, text="공시가 조회", width=30)
        self.btn.pack()

        #텔레그램 id입력창
        self.label_telegram = Label(self.tkhandler, text="텔레그램 ID")
        self.label_telegram.pack()
        #입력창
        self.text_telegram = Text(self.tkhandler, width=40, height=1, bd=1, relief=RIDGE)
        self.text_telegram.pack()


    #화면을 휠과 스크롤바로 움직인다.
    #스크롤바와 화면이 같이 움직인다. 

        self.scroll = Scrollbar(self.tkhandler,orient='vertical')
        self.lbox = Listbox(self.tkhandler, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.lbox.yview)
        self.scroll.pack(side='right',fill='y')
        self.lbox.pack(side='left',fill='both',expand=True) #윈도우 창이 변경되어도 listbox는 늘어난다.


    def run(self):
        self.tkhandler.mainloop()


g = GUI()
g.run()