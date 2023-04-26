import threading
from tkinter import *
from PIL import Image,ImageTk
from time import *
from threading import *

def toTransparent(image):

    # create a transparent version of the image
    img = image.convert("RGBA")
    img_data = img.getdata()

    # replace black pixels with transparent pixels
    new_data = []
    for item in img_data:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(item)

    # create a new image with the transparent pixels
    img.putdata(new_data)

    # create a PhotoImage object from the transparent image
    return ImageTk.PhotoImage(img)

class MyButton():
    def __init__(self,base,x,y,standardImg,cursor="arrow",hoverImg=None,clickImg=None,behavior=lambda:None,entry=None,padx=0,pady=0,fgSelected="black",fgNotSelected="white",*args,**kwargs):
        self.x=x
        self.y=y
        self.padx=padx
        self.pady=pady
        self.base=base
        self.entry=entry
        self.cursor=cursor
        self.behavior=behavior
        self.fgSelected=fgSelected
        self.fgNotSelected=fgNotSelected
        self.standardImg = None if standardImg == None else toTransparent(standardImg)
        self.hoverImg = None if hoverImg == None else toTransparent(hoverImg)
        self.clickImg = None if clickImg == None else toTransparent(clickImg)
        self.standardImgObject = self.base.create_image(self.x, self.y, image=self.standardImg, anchor=NW)
        self.base.tag_bind(self.standardImgObject, "<Enter>", self.buttonHover)
        self.base.tag_bind(self.standardImgObject, "<Leave>", self.buttonLeave)
        self.base.tag_bind(self.standardImgObject, "<Button-1>", self.buttonClick)
        self.base.tag_bind(self.standardImgObject, "<ButtonRelease-1>", self.buttonRelease)

        if self.entry!=None:
            self.entry=self.base.create_text(self.x+self.padx,self.y+self.pady,text=entry,fill=self.fgNotSelected,*args,**kwargs)
            self.base.tag_bind(self.entry, "<Enter>", self.buttonHover)
            self.base.tag_bind(self.entry, "<Leave>", self.buttonLeave)
            self.base.tag_bind(self.entry, "<Button-1>", self.buttonClick)
            self.base.tag_bind(self.entry, "<ButtonRelease-1>", self.buttonRelease)

    def setFgSelected(self):
        self.base.itemconfig(self.entry,fill=self.fgSelected)
    def buttonHover(self,event):
        self.base.config(cursor=self.cursor)
        if self.hoverImg != None:
            self.base.itemconfig(self.standardImgObject, image=self.hoverImg)

    def buttonLeave(self,event):
        self.base.itemconfig(self.standardImgObject, image=self.standardImg)
        self.base.config(cursor="arrow")

    def buttonClick(self,event):
        if self.entry!=None:
            self.base.itemconfig(self.entry, fill=self.fgSelected)

        if self.clickImg != None:
            self.base.itemconfig(self.standardImgObject, image=self.clickImg)
        self.behavior()
        self.base.config(cursor="arrow")


    def buttonRelease(self,event):
        # self.base.config(cursor="arrow")
        if self.clickImg != None:
            self.base.itemconfig(self.standardImgObject, image=self.standardImg)

    def place_forget(self):
        self.base.delete(self.standardImgObject)

    def place(self,x,y):
        self.standardImgObject = self.base.create_image(x, y, image=self.standardImg, anchor=NW)

    def setImage(self,frame,photo,original=None,value=True):
        self.base.itemconfig(self.standardImgObject, image=photo)
        frame.photoVar = ImageTk.getimage(photo) if value!=None else None
        frame.original =original  if value!=None else None
        self.standardImg=photo




class MyEntry:
    def __init__(self,base,x,y,standardImg,entry=None,hoverImg=None,clickImg=None,behavior=lambda:None,marginX=0,marginY=0,placeholder="",modified=False,value=None):
        self.x=x
        self.y=y
        self.marginX=marginX
        self.marginY=marginY
        self.base=base
        self.value=value
        self.entry=entry
        self.placeholder=placeholder
        self.modified=modified
        self.validation=None
        self.standardImg = None if standardImg == None else toTransparent(standardImg)
        self.hoverImg = None if hoverImg == None else toTransparent(hoverImg)
        self.clickImg = None if clickImg == None else toTransparent(clickImg)
        self.behavior=behavior
        self.standardImgObject = self.base.create_image(self.x, self.y, image=self.standardImg, anchor=NW)
        self.base.tag_bind(self.standardImgObject, "<Enter>", self.inputHover)
        self.base.tag_bind(self.standardImgObject, "<Leave>", self.inputLeave)
        self.base.tag_bind(self.standardImgObject, "<Button-1>", self.inputClick)
        self.base.tag_bind(self.standardImgObject, "<ButtonRelease-1>", self.inputRelease)

        self.entry.bind("<KeyRelease>",self.detectTyping)

        if self.entry!=None:
            if self.entry.get()==''and modified==False:
                self.entry.insert(0, self.placeholder)
                self.entry.config(state=DISABLED)

            elif self.entry.get()==placeholder and modified==False:
                self.entry.config(state=DISABLED)

            self.entry.bind("<Enter>", self.inputHover)
            self.entry.bind("<Leave>", self.inputLeave)
            self.entry.bind("<Button-1>", self.inputClick)
            self.entry.bind("<ButtonRelease-1>", self.inputRelease)

        self.entry.place(x=self.x+self.marginX,y=self.y+self.marginY)

    def getModified(self):
        return self.modified
    def detectTyping(self,event):
        if self.entry.get()=="":
            self.modified=False
        else:
            self.modified= True


    def inputHover(self,event):
        if self.hoverImg != None:
            self.base.itemconfig(self.standardImgObject, image=self.hoverImg)

    def inputLeave(self,event):
        self.base.itemconfig(self.standardImgObject, image=self.standardImg)
        if self.entry.get() == "":
            self.entry.insert(0,self.placeholder)
            self.entry.config(state=DISABLED)

    def inputClick(self,event):
        if self.clickImg != None:
            self.base.itemconfig(self.standardImgObject, image=self.clickImg)


        self.entry.config(state=NORMAL)

        if self.entry.get() == self.placeholder and self.modified==False:
            self.entry.delete(0,END)
        print(self.modified)
        print(self.get())
        self.behavior()

    def inputRelease(self,event):
        if self.clickImg != None:
            self.base.itemconfig(self.standardImgObject, image=self.standardImg)

    def place_forget(self):
        self.entry.destroy()
        self.base.delete(self.standardImgObject)

    def get(self):
        if not self.getModified():
            return ""
        return self.value.get()



class MyListBox(Listbox):

    def __init__(self, master,standardbg,standardfg,highlightbg,highlightfg,options=[],*args, **kwargs):
        Listbox.__init__(self, master, *args, **kwargs)

        self.bg = standardbg
        self.fg = standardfg
        self.h_bg = highlightbg
        self.h_fg = highlightfg

        self.options=options

        self.config(selectbackground=self.h_bg,activestyle="none")

        self.current = -1  # current highlighted item

        self.fill()

        self.bind("<Motion>", self.on_motion)
        self.bind("<Leave>", self.on_leave)

    def fill(self):
        print(self.options)
        """Fills the listbox with some numbers"""
        for index in range(len(self.options)):
            self.insert(END, self.options[index])
            self.itemconfig(index, {"bg": self.bg})
            self.itemconfig(index, {"fg": self.fg})

    def reset_colors(self):
        """Resets the colors of the items"""
        for index in range(len(self.get(0, END))):
            self.itemconfig(index, {"bg": self.bg})
            self.itemconfig(index, {"fg": self.fg})

    def set_highlighted_item(self, index):
        """Set the item at index with the highlighted colors"""
        self.itemconfig(index, {"bg": self.h_bg})
        self.itemconfig(index, {"fg": self.h_fg})

    def on_motion(self, event):
        """Calls everytime there's a motion of the mouse"""
        # print(self.current)
        index = self.index("@%s,%s" % (event.x, event.y))
        if self.current != -1 and self.current != index:
            self.reset_colors()
            self.set_highlighted_item(index)
        elif self.current == -1:
            self.set_highlighted_item(index)
        self.current = index

    def on_leave(self, event):
        self.reset_colors()
        self.current = -1




class MyMenu:
    def __init__(self,base,x,y,textLabel,defaultMenuButtonImg,hoverMenuButtonImg,clickedMenuButtonImg,defaultMenuListImg,hideWidgets=[],
                 padx=10,pady=7,menuListMarginX=0,menuListMarginY=40,listBoxMarginX=10,listBoxMarginY=50,anchor=NW,
                 standardbg="#1f1a24",standardfg="white",highlightbg="#bb86fc",highlightfg="#1f1a24",options=[],*args,**kwargs):

        # the x coordinate of the button
        self.x=x
        # the x coordinate of the button
        self.y=y
        # the base where the menu will be created
        self.base=base
        # the X margin of the menu list when appearing
        self.menuListMarginX=menuListMarginX
        # the Y margin of the menu list when appearing
        self.menuListMarginY=menuListMarginY
        # the X margin of the listBox when appearing
        self.listBoxMarginX=listBoxMarginX
        # the Y margin of the menu list when appearing
        self.listBoxMarginY=listBoxMarginY

        #colors used for the actual listmenu
        self.standardbg = standardbg
        self.standardfg = standardfg
        self.highlightbg = highlightbg
        self.highlightfg = highlightfg


        # widgets to hide while the menu is active
        self.hideWidgets=hideWidgets
        self.hiddenWidgetsPlaces=[]


        #to track if the drop down list is shown or not
        self.isActive=False

        #main label for the menu button
        self.defaultMenuButtonPhoto=toTransparent(defaultMenuButtonImg)

        #Menu button when hovered
        self.hoverMenuButtonPhoto = toTransparent(hoverMenuButtonImg)

        #Menu Button when clicked
        self.clickedMenuButtonPhoto = toTransparent(clickedMenuButtonImg)

        #the actual menu button
        self.menuButton=self.base.create_image(self.x,self.y,image=self.defaultMenuButtonPhoto,anchor=anchor)

        self.base.tag_bind(self.menuButton, "<Button-1>", self.menuButtonClick)
        self.base.tag_bind(self.menuButton, "<Enter>", self.menuButtonHover)
        self.base.tag_bind(self.menuButton, "<Leave>", self.menuButtonLeave)

        #the text label in the menu button
        self.textLabel=textLabel
        self.textLabel.place(x=self.x+padx,y=self.y+pady)

        self.textLabel.bind("<Button-1>", self.menuButtonClick)
        self.textLabel.bind("<Enter>", self.menuButtonHover)

        #main label for the menu list
        self.defaultMenuListPhoto = toTransparent(defaultMenuListImg)

        self.menuList = MyListBox(self.base, standardbg=self.standardbg, standardfg=self.standardfg,
                                  highlightbg=self.highlightbg, highlightfg=self.highlightfg,options=options, *args, **kwargs)
        self.menuList.bind("<<ListboxSelect>>", self.menuListClick)

    def menuButtonClick(self,event):
        if self.isActive==False:
            self.isActive = True

            # the actual listBox widget
            self.menuList.place(x=self.x+self.listBoxMarginX,y=self.y+self.listBoxMarginY)


            self.base.itemconfig(self.menuButton,image=self.clickedMenuButtonPhoto)

            #the actual menu button when clicked
            self.clickedMenuListObject = self.base.create_image(self.x+self.menuListMarginX, self.y +self.menuListMarginY, image=self.defaultMenuListPhoto, anchor=NW)

            #saving the coorinates of widgets to hide while menu is active
            for widget in self.hideWidgets:
                print(widget.place_info()["x"])
                self.hiddenWidgetsPlaces.append((widget,(int(widget.place_info()["x"]), int(widget.place_info()["y"]))))
            # for k,v in self.hiddenWidgetsPlaces.items():
            #     print(k,v)

            #hiding the widgets while menu is active
            for widget in self.hiddenWidgetsPlaces:
                widget[0].place_forget()

        else:
            self.isActive = False
            self.base.itemconfig(self.menuButton, image=self.hoverMenuButtonPhoto)
            self.menuListClick(event)


    def menuListClick(self,event):
        try:
            self.textLabel.config(text=self.menuList.get(self.menuList.curselection()))
        except:
            pass

        #recreating the hidden widgets when menu list is closed
        for widget in self.hiddenWidgetsPlaces:
            try:#to avoid an unexplained error
                widget[0].place(x=widget[1][0],y=widget[1][1])
            except:
                print("menu list error")

        self.menuList.place_forget()
        self.base.delete(self.clickedMenuListObject)
        self.base.itemconfig(self.menuButton, image=self.defaultMenuButtonPhoto)
        self.isActive=False
        print(self.get())

    def menuButtonHover(self,event):
        self.base.configure(cursor="hand2")
        th=threading.Thread(target=self.menuButtonHoverFunction)
        th.start()

    def menuButtonHoverFunction(self):
        if self.isActive==False:
            self.base.itemconfig(self.menuButton, image=self.hoverMenuButtonPhoto)


    def menuButtonLeave(self,event):
        self.base.configure(cursor="arrow")

        if self.isActive==False:
            self.base.itemconfig(self.menuButton, image=self.defaultMenuButtonPhoto)
        else:
            self.base.itemconfig(self.menuButton, image=self.clickedMenuButtonPhoto)

    def get(self):
        return self.textLabel["text"]

    def place_forget(self):
        self.base.delete(self.menuButton)
        self.base.delete(self.menuList)



class MyOption(MyButton):
    def __init__(self,base,x,y,entry=None,value=None,fgSelected="blue",fgNotSelected="blue",text="option",*args,**kwargs):
        super().__init__(base,x,y,entry=entry,fgSelected=fgSelected,fgNotSelected=fgNotSelected,*args,**kwargs)
        # self.label=entry
        self.fgSelected=fgSelected
        self.fgNotSelected=fgNotSelected
        self.base=base
        self.isSelected=False
        self.value=value
        self.optionList=None
        self.setOff()

    def setOptionlist(self,optionList):
        self.optionList=optionList

    def getValue(self):
        if self.value==None:
            return None
        return self.value

    def buttonClick(self,event):
        if self.isSelected==False:
            self.setOn()
        else:
            if self.clickImg != None:
                self.setOff()
                self.optionList.setActiveOption(None)

    def setOn(self):
        self.base.itemconfig(self.standardImgObject, image=self.clickImg)
        if self.entry!=None:
            self.base.itemconfig(self.entry,fill=self.fgSelected)

        self.isSelected = True
        self.optionList.setActiveOption(self)
        for option in self.optionList.optionsList:
            if option!=self:
                option.setOff()
    def setOff(self):
        self.base.itemconfig(self.standardImgObject, image=self.standardImg)
        if self.entry!=None:
            self.base.itemconfig(self.entry,fill=self.fgNotSelected)
        self.isSelected = False

    def buttonRelease(self,event):
        pass

    def buttonLeave(self,event):
        self.base.config(cursor="arrow")


    def place_forget(self):
        super().place_forget()
        self.base.delete(self.entry)

class MyOptionList:
    def __init__(self,options):
        self.optionsList=options
        self.activeOption=None

    def setActiveOption(self,option):
        self.activeOption=option
    def getActiveOption(self):
        return  self.activeOption

    def get(self):
        if self.activeOption==None:
            return None
        return self.activeOption.getValue()

class MyForm:
    def __init__(self,base,*args):
        self.components=[]
        for element in args:
            self.components.append(element)

    def get(self):
        values=[]
        for element in self.components:
            values.append(element.get())
        return values

class MyWidgetsGroup:
    def __init__(self,canvas,*args):
        self.canvas=canvas
        self.components=[]
        for element in args:
            self.components.append(element)

    def removeGroup(self):
        for element in self.components:
            try:
                element.place_forget()
            except:
                self.canvas.delete(element)

    def addElement(self,element):
        self.components.append(element)
    def get(self):
        values=[]
        for element in self.components:
            values.append(element.get())
        return values


class MyScrollableFrame:
    def __init__(self,baseCanvas,backgroundImg,backgroundColor,width,height,x=0,y=0,padx=0,pady=0):
        self.baseCanvas=baseCanvas
        self.BackgroundWidgetsFrame = baseCanvas.create_image(x, y, image=backgroundImg, anchor=NW)
        self.mainFrame=Frame(baseCanvas,border=0,highlightthickness=0,background=backgroundColor)
        self.mainFrame.place(x=x+padx,y=y+pady)

        self.canvas = Canvas(self.mainFrame, borderwidth=0, highlightthickness=0,width=width,height=height,background=backgroundColor)
        self.scrollbar = Scrollbar(self.mainFrame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas,bg=backgroundColor)
        self.scrollable_frame.bind("<Configure>", self.update_scrollregion)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left",fill="both",expand=False)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

    def update_scrollregion(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))  # # Ajouter des widgets à la frame gauche

    def place_forget(self):
        self.baseCanvas.delete(self.BackgroundWidgetsFrame)
        self.mainFrame.destroy()


class MyFrame:
    def __init__(self,baseCanvas,backgroundImg,backgroundColor,width,height,x=0,y=0,padx=0,pady=0):
        self.x=x
        self.y=y
        self.baseCanvas=baseCanvas
        self.background=backgroundImg
        self.BackgroundWidgetsFrame = self.baseCanvas.create_image(self.x, self.y, image=backgroundImg, anchor=NW)
        self.mainFrame=Canvas(baseCanvas,border=0,highlightthickness=0,background=backgroundColor,width=width,height=height)
        self.mainFrame.place(x=x+padx,y=y+pady)

    def place(self):
        self.BackgroundWidgetsFrame = self.baseCanvas.create_image(self.x, self.y, image=self.backgroundImg, anchor=NW)
        self.mainFrame.place(x=x+padx,y=y+pady)

    def place_forget(self):
        self.baseCanvas.delete(self.BackgroundWidgetsFrame)
        self.mainFrame.destroy()




