#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import turtle
import os, sys, gettext
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
#Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
from tkinter.messagebox import *
#from tkinter import filedialog  #.askopenfilename()
#from tkinter import simpledialog  #.askstring()

class Application_ui(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title('海龟驾驶台')
        self.master.geometry('1256x555')
        self.master.resizable(0,0)
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TFrame6.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame6.TLabelframe.Label', font=('宋体',9))
        self.Frame6 = LabelFrame(self.top, text='背景', style='TFrame6.TLabelframe')
        self.Frame6.place(relx=0.342, rely=0.486, relwidth=0.2, relheight=0.327)

        self.txtcodeFont = Font(font=('宋体',9))
        self.txtcode = Text(self.top, font=self.txtcodeFont)
        self.txtcode.place(relx=0.78, rely=0.523, relwidth=0.216, relheight=0.416)
        self.txtcode.bind('<<Modified>>', self.txtcode_Modified)
        self.txtcode.insert('1.0','Text19')

        self.style.configure('TFrame5.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame5.TLabelframe.Label', font=('宋体',9))
        self.Frame5 = LabelFrame(self.top, text='设定', style='TFrame5.TLabelframe')
        self.Frame5.place(relx=0.78, rely=0.018, relwidth=0.216, relheight=0.435)

        self.style.configure('TFrame4.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame4.TLabelframe.Label', font=('宋体',9))
        self.Frame4 = LabelFrame(self.top, text='插入文字', style='TFrame4.TLabelframe')
        self.Frame4.place(relx=0.549, rely=0.486, relwidth=0.224, relheight=0.453)

        self.style.configure('TFrame3.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame3.TLabelframe.Label', font=('宋体',9))
        self.Frame3 = LabelFrame(self.top, text='其他控制', style='TFrame3.TLabelframe')
        self.Frame3.place(relx=0.549, rely=0.018, relwidth=0.224, relheight=0.435)

        self.style.configure('TFrame2.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame2.TLabelframe.Label', font=('宋体',9))
        self.Frame2 = LabelFrame(self.top, text='画笔', style='TFrame2.TLabelframe')
        self.Frame2.place(relx=0.342, rely=0.018, relwidth=0.2, relheight=0.435)

        self.btnsetlocationVar = StringVar(value='定位')
        self.style.configure('Tbtnsetlocation.TButton', font=('宋体',9))
        self.btnsetlocation = Button(self.top, text='定位', textvariable=self.btnsetlocationVar, command=self.btnsetlocation_Cmd, style='Tbtnsetlocation.TButton')
        self.btnsetlocation.setText = lambda x: self.btnsetlocationVar.set(x)
        self.btnsetlocation.text = lambda : self.btnsetlocationVar.get()
        self.btnsetlocation.place(relx=0.111, rely=0.505, relwidth=0.073, relheight=0.053)

        self.txtyVar = StringVar(value='0')
        self.txty = Entry(self.top, textvariable=self.txtyVar, font=('宋体',9))
        self.txty.setText = lambda x: self.txtyVar.set(x)
        self.txty.text = lambda : self.txtyVar.get()
        self.txty.place(relx=0.127, rely=0.432, relwidth=0.053, relheight=0.045)

        self.style.configure('TFrame1.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame1.TLabelframe.Label', font=('宋体',9))
        self.Frame1 = LabelFrame(self.top, text='基本控制', style='TFrame1.TLabelframe')
        self.Frame1.place(relx=0.016, rely=0.018, relwidth=0.319, relheight=0.921)

        self.Label28Var = StringVar(value='代码')
        self.style.configure('TLabel28.TLabel', anchor='w', font=('宋体',11))
        self.Label28 = Label(self.top, text='代码', textvariable=self.Label28Var, style='TLabel28.TLabel')
        self.Label28.setText = lambda x: self.Label28Var.set(x)
        self.Label28.text = lambda : self.Label28Var.get()
        self.Label28.place(relx=0.78, rely=0.486, relwidth=0.072, relheight=0.038)

        self.MainMenu = Menu(self.top, tearoff=0)

        self.file = Menu(self.MainMenu, tearoff=0)

        self.save = Menu(self.file, tearoff=0)
        self.save.add_command(label='保存代码为', command=self.savepy_Cmd)
        self.save.add_command(label='保存图片', command=self.savepic_Cmd)
        self.file.add_cascade(menu=self.save, label='保存')

        self.print = Menu(self.file, tearoff=0)
        self.print.add_command(label='打印代码', command=self.printcode_Cmd)
        self.print.add_command(label='打印图片', command=self.printpic_Cmd)
        self.file.add_cascade(menu=self.print, label='打印')
        self.MainMenu.add_cascade(menu=self.file, label='文件')

        self.help = Menu(self.MainMenu, tearoff=0)
        self.help.add_command(label='turtle范例', command=self.example_Cmd)
        self.help.add_command(label='查看帮助', command=self.seehelp_Cmd)
        self.help.add_command(label='关于', command=self.about_Cmd)
        self.MainMenu.add_cascade(menu=self.help, label='帮助')
        self.top.configure(menu=self.MainMenu)

        self.btndotVar = StringVar(value='画点')
        self.style.configure('Tbtndot.TButton', font=('宋体',9))
        self.btndot = Button(self.top, text='画点', textvariable=self.btndotVar, command=self.btndot_Cmd, style='Tbtndot.TButton')
        self.btndot.setText = lambda x: self.btndotVar.set(x)
        self.btndot.text = lambda : self.btndotVar.get()
        self.btndot.place(relx=0.199, rely=0.306, relwidth=0.065, relheight=0.053)

        self.btnchoosepicVar = StringVar(value='...')
        self.style.configure('Tbtnchoosepic.TButton', font=('宋体',9))
        self.btnchoosepic = Button(self.Frame6, text='...', textvariable=self.btnchoosepicVar, command=self.btnchoosepic_Cmd, style='Tbtnchoosepic.TButton')
        self.btnchoosepic.setText = lambda x: self.btnchoosepicVar.set(x)
        self.btnchoosepic.text = lambda : self.btnchoosepicVar.get()
        self.btnchoosepic.place(relx=0.837, rely=0.441, relwidth=0.125, relheight=0.138)

        self.Text25Var = StringVar(value='500')
        self.Text25 = Entry(self.Frame6, textvariable=self.Text25Var, font=('宋体',9))
        self.Text25.setText = lambda x: self.Text25Var.set(x)
        self.Text25.text = lambda : self.Text25Var.get()
        self.Text25.place(relx=0.398, rely=0.717, relwidth=0.164, relheight=0.138)

        self.commodeList = ['logo', 'standard', 'world', ]
        self.commodeVar = StringVar(value='logo')
        self.commode = Combobox(self.Frame5, exportselection=0, text='logo', textvariable=self.commodeVar, values=self.commodeList, font=('宋体',9))
        self.commode.setText = lambda x: self.commodeVar.set(x)
        self.commode.text = lambda : self.commodeVar.get()
        self.commode.place(relx=0.332, rely=0.705, relwidth=0.374)

        self.btnsetdelayVar = StringVar(value='设置')
        self.style.configure('Tbtnsetdelay.TButton', font=('宋体',9))
        self.btnsetdelay = Button(self.Frame5, text='设置', textvariable=self.btnsetdelayVar, command=self.btnsetdelay_Cmd, style='Tbtnsetdelay.TButton')
        self.btnsetdelay.setText = lambda x: self.btnsetdelayVar.set(x)
        self.btnsetdelay.text = lambda : self.btnsetdelayVar.get()
        self.btnsetdelay.place(relx=0.775, rely=0.539, relwidth=0.152, relheight=0.13)

        self.txtdelayVar = StringVar(value='')
        self.txtdelay = Entry(self.Frame5, textvariable=self.txtdelayVar, font=('宋体',9))
        self.txtdelay.setText = lambda x: self.txtdelayVar.set(x)
        self.txtdelay.text = lambda : self.txtdelayVar.get()
        self.txtdelay.place(relx=0.332, rely=0.539, relwidth=0.263, relheight=0.104)

        self.txtsetangleVar = StringVar(value='360')
        self.txtsetangle = Entry(self.Frame5, textvariable=self.txtsetangleVar, font=('宋体',9))
        self.txtsetangle.setText = lambda x: self.txtsetangleVar.set(x)
        self.txtsetangle.text = lambda : self.txtsetangleVar.get()
        self.txtsetangle.place(relx=0.332, rely=0.249, relwidth=0.189, relheight=0.104)

        self.optradTextVar = StringVar(value='弧度')
        self.Frame5RadioVar = StringVar()
        self.style.configure('Toptrad.TRadiobutton', font=('宋体',9))
        self.optrad = Radiobutton(self.Frame5, text='弧度', value='optrad', textvariable=self.optradTextVar, variable=self.Frame5RadioVar, style='Toptrad.TRadiobutton')
        self.optrad.setText = lambda x: self.optradTextVar.set(x)
        self.optrad.text = lambda : self.optradTextVar.get()
        self.optrad.setValue = lambda x: self.Frame5RadioVar.set('optrad' if x else '')
        self.optrad.value = lambda : 1 if self.Frame5RadioVar.get() == 'optrad' else 0
        self.optrad.place(relx=0.037, rely=0.415, relwidth=0.263, relheight=0.104)

        self.optangleTextVar = StringVar(value='角度')
        self.style.configure('Toptangle.TRadiobutton', font=('宋体',9))
        self.optangle = Radiobutton(self.Frame5, text='角度', value='optangle', textvariable=self.optangleTextVar, variable=self.Frame5RadioVar, style='Toptangle.TRadiobutton')
        self.optangle.setText = lambda x: self.optangleTextVar.set(x)
        self.optangle.text = lambda : self.optangleTextVar.get()
        self.optangle.setValue = lambda x: self.Frame5RadioVar.set('optangle' if x else '')
        self.optangle.value = lambda : 1 if self.Frame5RadioVar.get() == 'optangle' else 0
        self.optangle.setValue(1)
        self.optangle.place(relx=0.037, rely=0.249, relwidth=0.226, relheight=0.104)

        self.Label27Var = StringVar(value='海龟模式')
        self.style.configure('TLabel27.TLabel', anchor='w', font=('宋体',9))
        self.Label27 = Label(self.Frame5, text='海龟模式', textvariable=self.Label27Var, style='TLabel27.TLabel')
        self.Label27.setText = lambda x: self.Label27Var.set(x)
        self.Label27.text = lambda : self.Label27Var.get()
        self.Label27.place(relx=0.074, rely=0.705, relwidth=0.262, relheight=0.087)

        self.Label26Var = StringVar(value='ms')
        self.style.configure('TLabel26.TLabel', anchor='w', font=('宋体',9))
        self.Label26 = Label(self.Frame5, text='ms', textvariable=self.Label26Var, style='TLabel26.TLabel')
        self.Label26.setText = lambda x: self.Label26Var.set(x)
        self.Label26.text = lambda : self.Label26Var.get()
        self.Label26.place(relx=0.664, rely=0.58, relwidth=0.077, relheight=0.087)

        self.Label25Var = StringVar(value='动画延迟')
        self.style.configure('TLabel25.TLabel', anchor='w', font=('宋体',9))
        self.Label25 = Label(self.Frame5, text='动画延迟', textvariable=self.Label25Var, style='TLabel25.TLabel')
        self.Label25.setText = lambda x: self.Label25Var.set(x)
        self.Label25.text = lambda : self.Label25Var.get()
        self.Label25.place(relx=0.074, rely=0.58, relwidth=0.262, relheight=0.087)

        self.Label24Var = StringVar(value='为一圆周')
        self.style.configure('TLabel24.TLabel', anchor='w', font=('宋体',9))
        self.Label24 = Label(self.Frame5, text='为一圆周', textvariable=self.Label24Var, style='TLabel24.TLabel')
        self.Label24.setText = lambda x: self.Label24Var.set(x)
        self.Label24.text = lambda : self.Label24Var.get()
        self.Label24.place(relx=0.59, rely=0.249, relwidth=0.263, relheight=0.088)

        self.Label23Var = StringVar(value='角度单位')
        self.style.configure('TLabel23.TLabel', anchor='w', font=('宋体',11))
        self.Label23 = Label(self.Frame5, text='角度单位', textvariable=self.Label23Var, style='TLabel23.TLabel')
        self.Label23.setText = lambda x: self.Label23Var.set(x)
        self.Label23.text = lambda : self.Label23Var.get()
        self.Label23.place(relx=0.037, rely=0.083, relwidth=0.337, relheight=0.088)

        self.Text24Var = StringVar(value='500')
        self.Text24 = Entry(self.Frame6, textvariable=self.Text24Var, font=('宋体',9))
        self.Text24.setText = lambda x: self.Text24Var.set(x)
        self.Text24.text = lambda : self.Text24Var.get()
        self.Text24.place(relx=0.797, rely=0.717, relwidth=0.164, relheight=0.138)

        self.cominsertfontsizeVar = StringVar(value='10')
        self.cominsertfontsize = Entry(self.Frame4, textvariable=self.cominsertfontsizeVar, font=('宋体',9))
        self.cominsertfontsize.setText = lambda x: self.cominsertfontsizeVar.set(x)
        self.cominsertfontsize.text = lambda : self.cominsertfontsizeVar.get()
        self.cominsertfontsize.place(relx=0.782, rely=0.557, relwidth=0.182, relheight=0.09)

        self.cominsertstyleList = ['左对齐', '右对齐', '居中', ]
        self.cominsertstyleVar = StringVar(value='左对齐')
        self.cominsertstyle = Combobox(self.Frame4, exportselection=0, state='readonly', text='左对齐', textvariable=self.cominsertstyleVar, values=self.cominsertstyleList, font=('宋体',9))
        self.cominsertstyle.setText = lambda x: self.cominsertstyleVar.set(x)
        self.cominsertstyle.text = lambda : self.cominsertstyleVar.get()
        self.cominsertstyle.place(relx=0.427, rely=0.557, relwidth=0.324)

        self.cominserttextList = ['左对齐', '右对齐', '居中', ]
        self.cominserttextVar = StringVar(value='左对齐')
        self.cominserttext = Combobox(self.Frame4, exportselection=0, state='readonly', text='左对齐', textvariable=self.cominserttextVar, values=self.cominserttextList, font=('宋体',9))
        self.cominserttext.setText = lambda x: self.cominserttextVar.set(x)
        self.cominserttext.text = lambda : self.cominserttextVar.get()
        self.cominserttext.place(relx=0.071, rely=0.557, relwidth=0.324)

        self.comaglineList = ['左对齐', '右对齐', '居中', ]
        self.comaglineVar = StringVar(value='左对齐')
        self.comagline = Combobox(self.Frame4, exportselection=0, state='readonly', text='左对齐', textvariable=self.comaglineVar, values=self.comaglineList, font=('宋体',9))
        self.comagline.setText = lambda x: self.comaglineVar.set(x)
        self.comagline.text = lambda : self.comaglineVar.get()
        self.comagline.place(relx=0.32, rely=0.318, relwidth=0.36)

        self.txtinsertFont = Font(font=('宋体',9))
        self.txtinsert = Text(self.Frame4, font=self.txtinsertFont)
        self.txtinsert.place(relx=0.036, rely=0.08, relwidth=0.751, relheight=0.179)
        self.txtinsert.insert('1.0','')

        self.Check2TextVar = StringVar(value='画笔移到文本右下角')
        self.Check2Var = IntVar(value=0)
        self.style.configure('TCheck2.TCheckbutton', font=('宋体',9))
        self.Check2 = Checkbutton(self.Frame4, text='画笔移到文本右下角', textvariable=self.Check2TextVar, variable=self.Check2Var, style='TCheck2.TCheckbutton')
        self.Check2.setText = lambda x: self.Check2TextVar.set(x)
        self.Check2.text = lambda : self.Check2TextVar.get()
        self.Check2.setValue = lambda x: self.Check2Var.set(x)
        self.Check2.value = lambda : self.Check2Var.get()
        self.Check2.place(relx=0.071, rely=0.716, relwidth=0.609, relheight=0.085)

        self.btninserttextVar = StringVar(value='书写')
        self.style.configure('Tbtninserttext.TButton', font=('宋体',9))
        self.btninserttext = Button(self.Frame4, text='书写', textvariable=self.btninserttextVar, command=self.btninserttext_Cmd, style='Tbtninserttext.TButton')
        self.btninserttext.setText = lambda x: self.btninserttextVar.set(x)
        self.btninserttext.text = lambda : self.btninserttextVar.get()
        self.btninserttext.place(relx=0.107, rely=0.836, relwidth=0.324, relheight=0.1)

        self.Label22Var = StringVar(value='字号')
        self.style.configure('TLabel22.TLabel', anchor='w', font=('宋体',9))
        self.Label22 = Label(self.Frame4, text='字号', textvariable=self.Label22Var, style='TLabel22.TLabel')
        self.Label22.setText = lambda x: self.Label22Var.set(x)
        self.Label22.text = lambda : self.Label22Var.get()
        self.Label22.place(relx=0.782, rely=0.438, relwidth=0.119, relheight=0.085)

        self.Label21Var = StringVar(value='字体样式')
        self.style.configure('TLabel21.TLabel', anchor='w', font=('宋体',9))
        self.Label21 = Label(self.Frame4, text='字体样式', textvariable=self.Label21Var, style='TLabel21.TLabel')
        self.Label21.setText = lambda x: self.Label21Var.set(x)
        self.Label21.text = lambda : self.Label21Var.get()
        self.Label21.place(relx=0.427, rely=0.438, relwidth=0.253, relheight=0.085)

        self.Label19Var = StringVar(value='对齐方式')
        self.style.configure('TLabel19.TLabel', anchor='w', font=('宋体',9))
        self.Label19 = Label(self.Frame4, text='对齐方式', textvariable=self.Label19Var, style='TLabel19.TLabel')
        self.Label19.setText = lambda x: self.Label19Var.set(x)
        self.Label19.text = lambda : self.Label19Var.get()
        self.Label19.place(relx=0.071, rely=0.318, relwidth=0.253, relheight=0.085)

        self.Label20Var = StringVar(value='字体')
        self.style.configure('TLabel20.TLabel', anchor='w', font=('宋体',9))
        self.Label20 = Label(self.Frame4, text='字体', textvariable=self.Label20Var, style='TLabel20.TLabel')
        self.Label20.setText = lambda x: self.Label20Var.set(x)
        self.Label20.text = lambda : self.Label20Var.get()
        self.Label20.place(relx=0.071, rely=0.438, relwidth=0.218, relheight=0.085)

        self.txtpicVar = StringVar(value='')
        self.txtpic = Entry(self.Frame6, textvariable=self.txtpicVar, font=('宋体',9))
        self.txtpic.setText = lambda x: self.txtpicVar.set(x)
        self.txtpic.text = lambda : self.txtpicVar.get()
        self.txtpic.place(relx=0.398, rely=0.441, relwidth=0.423, relheight=0.138)

        self.btnhideVar = StringVar(value='隐藏海龟')
        self.style.configure('Tbtnhide.TButton', font=('宋体',9))
        self.btnhide = Button(self.Frame3, text='隐藏海龟', textvariable=self.btnhideVar, command=self.btnhide_Cmd, style='Tbtnhide.TButton')
        self.btnhide.setText = lambda x: self.btnhideVar.set(x)
        self.btnhide.text = lambda : self.btnhideVar.get()
        self.btnhide.place(relx=0.071, rely=0.746, relwidth=0.324, relheight=0.13)

        self.btnclearVar = StringVar(value='清空')
        self.style.configure('Tbtnclear.TButton', font=('宋体',9))
        self.btnclear = Button(self.Frame3, text='清空', textvariable=self.btnclearVar, command=self.btnclear_Cmd, style='Tbtnclear.TButton')
        self.btnclear.setText = lambda x: self.btnclearVar.set(x)
        self.btnclear.text = lambda : self.btnclearVar.get()
        self.btnclear.place(relx=0.462, rely=0.539, relwidth=0.324, relheight=0.121)

        self.btnresetVar = StringVar(value='重置')
        self.style.configure('Tbtnreset.TButton', font=('宋体',9))
        self.btnreset = Button(self.Frame3, text='重置', textvariable=self.btnresetVar, command=self.btnreset_Cmd, style='Tbtnreset.TButton')
        self.btnreset.setText = lambda x: self.btnresetVar.set(x)
        self.btnreset.text = lambda : self.btnresetVar.get()
        self.btnreset.place(relx=0.071, rely=0.539, relwidth=0.324, relheight=0.121)

        self.btnendfillVar = StringVar(value='结束填充')
        self.style.configure('Tbtnendfill.TButton', font=('宋体',9))
        self.btnendfill = Button(self.Frame3, text='结束填充', textvariable=self.btnendfillVar, command=self.btnendfill_Cmd, style='Tbtnendfill.TButton')
        self.btnendfill.setText = lambda x: self.btnendfillVar.set(x)
        self.btnendfill.text = lambda : self.btnendfillVar.get()
        self.btnendfill.place(relx=0.462, rely=0.332, relwidth=0.324, relheight=0.13)

        self.btnstartfillVar = StringVar(value='开始填充')
        self.style.configure('Tbtnstartfill.TButton', font=('宋体',9))
        self.btnstartfill = Button(self.Frame3, text='开始填充', textvariable=self.btnstartfillVar, command=self.btnstartfill_Cmd, style='Tbtnstartfill.TButton')
        self.btnstartfill.setText = lambda x: self.btnstartfillVar.set(x)
        self.btnstartfill.text = lambda : self.btnstartfillVar.get()
        self.btnstartfill.place(relx=0.071, rely=0.332, relwidth=0.324, relheight=0.13)

        self.chkfillTextVar = StringVar(value='是否填充')
        self.chkfillVar = IntVar(value=0)
        self.style.configure('Tchkfill.TCheckbutton', font=('宋体',9))
        self.chkfill = Checkbutton(self.Frame3, text='是否填充', textvariable=self.chkfillTextVar, variable=self.chkfillVar, style='Tchkfill.TCheckbutton')
        self.chkfill.setText = lambda x: self.chkfillTextVar.set(x)
        self.chkfill.text = lambda : self.chkfillTextVar.get()
        self.chkfill.setValue = lambda x: self.chkfillVar.set(x)
        self.chkfill.value = lambda : self.chkfillVar.get()
        self.chkfill.place(relx=0.071, rely=0.124, relwidth=0.396, relheight=0.13)

        self.txtbackcolorrVar = StringVar(value='0')
        self.txtbackcolorr = Entry(self.Frame6, textvariable=self.txtbackcolorrVar, font=('宋体',9))
        self.txtbackcolorr.setText = lambda x: self.txtbackcolorrVar.set(x)
        self.txtbackcolorr.text = lambda : self.txtbackcolorrVar.get()
        self.txtbackcolorr.place(relx=0.398, rely=0.166, relwidth=0.164, relheight=0.138)

        self.txtfillbVar = StringVar(value='0')
        self.txtfillb = Entry(self.Frame2, textvariable=self.txtfillbVar, font=('宋体',9))
        self.txtfillb.setText = lambda x: self.txtfillbVar.set(x)
        self.txtfillb.text = lambda : self.txtfillbVar.get()
        self.txtfillb.place(relx=0.757, rely=0.746, relwidth=0.164, relheight=0.104)

        self.txtfillgVar = StringVar(value='0')
        self.txtfillg = Entry(self.Frame2, textvariable=self.txtfillgVar, font=('宋体',9))
        self.txtfillg.setText = lambda x: self.txtfillgVar.set(x)
        self.txtfillg.text = lambda : self.txtfillgVar.get()
        self.txtfillg.place(relx=0.558, rely=0.746, relwidth=0.164, relheight=0.104)

        self.txtfillrVar = StringVar(value='0')
        self.txtfillr = Entry(self.Frame2, textvariable=self.txtfillrVar, font=('宋体',9))
        self.txtfillr.setText = lambda x: self.txtfillrVar.set(x)
        self.txtfillr.text = lambda : self.txtfillrVar.get()
        self.txtfillr.place(relx=0.359, rely=0.746, relwidth=0.164, relheight=0.104)

        self.txtpenbVar = StringVar(value='0')
        self.txtpenb = Entry(self.Frame2, textvariable=self.txtpenbVar, font=('宋体',9))
        self.txtpenb.setText = lambda x: self.txtpenbVar.set(x)
        self.txtpenb.text = lambda : self.txtpenbVar.get()
        self.txtpenb.place(relx=0.757, rely=0.539, relwidth=0.164, relheight=0.104)

        self.txtpengVar = StringVar(value='0')
        self.txtpeng = Entry(self.Frame2, textvariable=self.txtpengVar, font=('宋体',9))
        self.txtpeng.setText = lambda x: self.txtpengVar.set(x)
        self.txtpeng.text = lambda : self.txtpengVar.get()
        self.txtpeng.place(relx=0.558, rely=0.539, relwidth=0.164, relheight=0.104)

        self.txtpenrVar = StringVar(value='0')
        self.txtpenr = Entry(self.Frame2, textvariable=self.txtpenrVar, font=('宋体',9))
        self.txtpenr.setText = lambda x: self.txtpenrVar.set(x)
        self.txtpenr.text = lambda : self.txtpenrVar.get()
        self.txtpenr.place(relx=0.359, rely=0.539, relwidth=0.164, relheight=0.104)

        self.btnwidthVar = StringVar(value='设置')
        self.style.configure('Tbtnwidth.TButton', font=('宋体',9))
        self.btnwidth = Button(self.Frame2, text='设置', textvariable=self.btnwidthVar, command=self.btnwidth_Cmd, style='Tbtnwidth.TButton')
        self.btnwidth.setText = lambda x: self.btnwidthVar.set(x)
        self.btnwidth.text = lambda : self.btnwidthVar.get()
        self.btnwidth.place(relx=0.677, rely=0.332, relwidth=0.243, relheight=0.121)

        self.txtwidthVar = StringVar(value='1')
        self.txtwidth = Entry(self.Frame2, textvariable=self.txtwidthVar, font=('宋体',9))
        self.txtwidth.setText = lambda x: self.txtwidthVar.set(x)
        self.txtwidth.text = lambda : self.txtwidthVar.get()
        self.txtwidth.place(relx=0.359, rely=0.332, relwidth=0.266, relheight=0.104)

        self.btndownVar = StringVar(value='落笔')
        self.style.configure('Tbtndown.TButton', font=('宋体',9))
        self.btndown = Button(self.Frame2, text='落笔', textvariable=self.btndownVar, command=self.btndown_Cmd, style='Tbtndown.TButton')
        self.btndown.setText = lambda x: self.btndownVar.set(x)
        self.btndown.text = lambda : self.btndownVar.get()
        self.btndown.place(relx=0.359, rely=0.124, relwidth=0.243, relheight=0.13)

        self.btnupVar = StringVar(value='抬笔')
        self.style.configure('Tbtnup.TButton', font=('宋体',9))
        self.btnup = Button(self.Frame2, text='抬笔', textvariable=self.btnupVar, command=self.btnup_Cmd, style='Tbtnup.TButton')
        self.btnup.setText = lambda x: self.btnupVar.set(x)
        self.btnup.text = lambda : self.btnupVar.get()
        self.btnup.place(relx=0.08, rely=0.124, relwidth=0.243, relheight=0.13)

        self.Label15Var = StringVar(value='填充颜色')
        self.style.configure('TLabel15.TLabel', anchor='w', font=('宋体',9))
        self.Label15 = Label(self.Frame2, text='填充颜色', textvariable=self.Label15Var, style='TLabel15.TLabel')
        self.Label15.setText = lambda x: self.Label15Var.set(x)
        self.Label15.text = lambda : self.Label15Var.get()
        self.Label15.place(relx=0.08, rely=0.788, relwidth=0.284, relheight=0.088)

        self.Label14Var = StringVar(value='画笔颜色')
        self.style.configure('TLabel14.TLabel', anchor='w', font=('宋体',9))
        self.Label14 = Label(self.Frame2, text='画笔颜色', textvariable=self.Label14Var, style='TLabel14.TLabel')
        self.Label14.setText = lambda x: self.Label14Var.set(x)
        self.Label14.text = lambda : self.Label14Var.get()
        self.Label14.place(relx=0.08, rely=0.58, relwidth=0.284, relheight=0.088)

        self.Label13Var = StringVar(value='画笔粗细')
        self.style.configure('TLabel13.TLabel', anchor='w', font=('宋体',9))
        self.Label13 = Label(self.Frame2, text='画笔粗细', textvariable=self.Label13Var, style='TLabel13.TLabel')
        self.Label13.setText = lambda x: self.Label13Var.set(x)
        self.Label13.text = lambda : self.Label13Var.get()
        self.Label13.place(relx=0.08, rely=0.373, relwidth=0.243, relheight=0.087)

        self.txtbackcolorrtxtbackcolorgVar = StringVar(value='0')
        self.txtbackcolorrtxtbackcolorg = Entry(self.Frame6, textvariable=self.txtbackcolorrtxtbackcolorgVar, font=('宋体',9))
        self.txtbackcolorrtxtbackcolorg.setText = lambda x: self.txtbackcolorrtxtbackcolorgVar.set(x)
        self.txtbackcolorrtxtbackcolorg.text = lambda : self.txtbackcolorrtxtbackcolorgVar.get()
        self.txtbackcolorrtxtbackcolorg.place(relx=0.598, rely=0.166, relwidth=0.164, relheight=0.138)

        self.txtbackcolorrbVar = StringVar(value='0')
        self.txtbackcolorrb = Entry(self.Frame6, textvariable=self.txtbackcolorrbVar, font=('宋体',9))
        self.txtbackcolorrb.setText = lambda x: self.txtbackcolorrbVar.set(x)
        self.txtbackcolorrb.text = lambda : self.txtbackcolorrbVar.get()
        self.txtbackcolorrb.place(relx=0.797, rely=0.166, relwidth=0.164, relheight=0.138)

        self.Label32Var = StringVar(value='x')
        self.style.configure('TLabel32.TLabel', anchor='w', font=('宋体',11))
        self.Label32 = Label(self.Frame6, text='x', textvariable=self.Label32Var, style='TLabel32.TLabel')
        self.Label32.setText = lambda x: self.Label32Var.set(x)
        self.Label32.text = lambda : self.Label32Var.get()
        self.Label32.place(relx=0.637, rely=0.717, relwidth=0.084, relheight=0.116)

        self.Text6Var = StringVar(value='0')
        self.Text6 = Entry(self.Frame1, textvariable=self.Text6Var, font=('宋体',9))
        self.Text6.setText = lambda x: self.Text6Var.set(x)
        self.Text6.text = lambda : self.Text6Var.get()
        self.Text6.place(relx=0.623, rely=0.215, relwidth=0.103, relheight=0.049)

        self.Text2Var = StringVar(value='0')
        self.Text2 = Entry(self.Frame1, textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.setText = lambda x: self.Text2Var.set(x)
        self.Text2.text = lambda : self.Text2Var.get()
        self.Text2.place(relx=0.748, rely=0.215, relwidth=0.103, relheight=0.049)

        self.Text1Var = StringVar(value='0')
        self.Text1 = Entry(self.Frame1, textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda : self.Text1Var.get()
        self.Text1.place(relx=0.873, rely=0.215, relwidth=0.103, relheight=0.049)

        self.btnundoVar = StringVar(value='撤回')
        self.style.configure('Tbtnundo.TButton', font=('宋体',9))
        self.btnundo = Button(self.Frame1, text='撤回', textvariable=self.btnundoVar, command=self.btnundo_Cmd, style='Tbtnundo.TButton')
        self.btnundo.setText = lambda x: self.btnundoVar.set(x)
        self.btnundo.text = lambda : self.btnundoVar.get()
        self.btnundo.place(relx=0.599, rely=0.45, relwidth=0.203, relheight=0.049)

        self.lststampidVar = StringVar(value='lststampid')
        self.lststampidFont = Font(font=('宋体',9))
        self.lststampid = Listbox(self.Frame1, listvariable=self.lststampidVar, font=self.lststampidFont)
        self.lststampid.place(relx=0.549, rely=0.822, relwidth=0.402, relheight=0.155)

        self.txtstampidVar = StringVar(value='')
        self.txtstampid = Entry(self.Frame1, textvariable=self.txtstampidVar, font=('宋体',9))
        self.txtstampid.setText = lambda x: self.txtstampidVar.set(x)
        self.txtstampid.text = lambda : self.txtstampidVar.get()
        self.txtstampid.place(relx=0.673, rely=0.685, relwidth=0.128, relheight=0.049)

        self.btndeletestampVar = StringVar(value='删除')
        self.style.configure('Tbtndeletestamp.TButton', font=('宋体',9))
        self.btndeletestamp = Button(self.Frame1, text='删除', textvariable=self.btndeletestampVar, command=self.btndeletestamp_Cmd, style='Tbtndeletestamp.TButton')
        self.btndeletestamp.setText = lambda x: self.btndeletestampVar.set(x)
        self.btndeletestamp.text = lambda : self.btndeletestampVar.get()
        self.btndeletestamp.place(relx=0.574, rely=0.607, relwidth=0.153, relheight=0.057)

        self.btnstampVar = StringVar(value='盖印章')
        self.style.configure('Tbtnstamp.TButton', font=('宋体',9))
        self.btnstamp = Button(self.Frame1, text='盖印章', textvariable=self.btnstampVar, command=self.btnstamp_Cmd, style='Tbtnstamp.TButton')
        self.btnstamp.setText = lambda x: self.btnstampVar.set(x)
        self.btnstamp.text = lambda : self.btnstampVar.get()
        self.btnstamp.place(relx=0.623, rely=0.528, relwidth=0.203, relheight=0.057)

        self.Text4Var = StringVar(value='5')
        self.Text4 = Entry(self.Frame1, textvariable=self.Text4Var, font=('宋体',9))
        self.Text4.setText = lambda x: self.Text4Var.set(x)
        self.Text4.text = lambda : self.Text4Var.get()
        self.Text4.place(relx=0.249, rely=0.372, relwidth=0.166, relheight=0.049)

        self.txtdotsizeVar = StringVar(value='50')
        self.txtdotsize = Entry(self.Frame1, textvariable=self.txtdotsizeVar, font=('宋体',9))
        self.txtdotsize.setText = lambda x: self.txtdotsizeVar.set(x)
        self.txtdotsize.text = lambda : self.txtdotsizeVar.get()
        self.txtdotsize.place(relx=0.673, rely=0.137, relwidth=0.166, relheight=0.049)

        self.txtbiancountVar = StringVar(value='6')
        self.txtbiancount = Entry(self.Frame1, textvariable=self.txtbiancountVar, font=('宋体',9))
        self.txtbiancount.setText = lambda x: self.txtbiancountVar.set(x)
        self.txtbiancount.text = lambda : self.txtbiancountVar.get()
        self.txtbiancount.place(relx=0.15, rely=0.822, relwidth=0.365, relheight=0.049)

        self.txtrangleVar = StringVar(value='360')
        self.txtrangle = Entry(self.Frame1, textvariable=self.txtrangleVar, font=('宋体',9))
        self.txtrangle.setText = lambda x: self.txtrangleVar.set(x)
        self.txtrangle.text = lambda : self.txtrangleVar.get()
        self.txtrangle.place(relx=0.224, rely=0.744, relwidth=0.29, relheight=0.049)

        self.txtrVar = StringVar(value='100')
        self.txtr = Entry(self.Frame1, textvariable=self.txtrVar, font=('宋体',9))
        self.txtr.setText = lambda x: self.txtrVar.set(x)
        self.txtr.text = lambda : self.txtrVar.get()
        self.txtr.place(relx=0.125, rely=0.665, relwidth=0.39, relheight=0.049)

        self.btnhomeVar = StringVar(value='返回原处')
        self.style.configure('Tbtnhome.TButton', font=('宋体',9))
        self.btnhome = Button(self.Frame1, text='返回原处', textvariable=self.btnhomeVar, command=self.btnhome_Cmd, style='Tbtnhome.TButton')
        self.btnhome.setText = lambda x: self.btnhomeVar.set(x)
        self.btnhome.text = lambda : self.btnhomeVar.get()
        self.btnhome.place(relx=0.175, rely=0.9, relwidth=0.228, relheight=0.057)

        self.Text7Var = StringVar(value='0')
        self.Text7 = Entry(self.Frame1, textvariable=self.Text7Var, font=('宋体',9))
        self.Text7.setText = lambda x: self.Text7Var.set(x)
        self.Text7.text = lambda : self.Text7Var.get()
        self.Text7.place(relx=0.125, rely=0.528, relwidth=0.14, relheight=0.049)

        self.txtxVar = StringVar(value='0')
        self.txtx = Entry(self.Frame1, textvariable=self.txtxVar, font=('宋体',9))
        self.txtx.setText = lambda x: self.txtxVar.set(x)
        self.txtx.text = lambda : self.txtxVar.get()
        self.txtx.place(relx=0.125, rely=0.45, relwidth=0.14, relheight=0.049)

        self.btnforwardVar = StringVar(value='前进')
        self.style.configure('Tbtnforward.TButton', font=('宋体',9))
        self.btnforward = Button(self.Frame1, text='前进', textvariable=self.btnforwardVar, command=self.btnforward_Cmd, style='Tbtnforward.TButton')
        self.btnforward.setText = lambda x: self.btnforwardVar.set(x)
        self.btnforward.text = lambda : self.btnforwardVar.get()
        self.btnforward.place(relx=0.05, rely=0.059, relwidth=0.166, relheight=0.057)

        self.txtforwardVar = StringVar(value='100')
        self.txtforward = Entry(self.Frame1, textvariable=self.txtforwardVar, font=('宋体',9))
        self.txtforward.setText = lambda x: self.txtforwardVar.set(x)
        self.txtforward.text = lambda : self.txtforwardVar.get()
        self.txtforward.place(relx=0.249, rely=0.059, relwidth=0.166, relheight=0.049)

        self.txtbackVar = StringVar(value='100')
        self.txtback = Entry(self.Frame1, textvariable=self.txtbackVar, font=('宋体',9))
        self.txtback.setText = lambda x: self.txtbackVar.set(x)
        self.txtback.text = lambda : self.txtbackVar.get()
        self.txtback.place(relx=0.249, rely=0.137, relwidth=0.165, relheight=0.049)

        self.btnbackVar = StringVar(value='后退')
        self.style.configure('Tbtnback.TButton', font=('宋体',9))
        self.btnback = Button(self.Frame1, text='后退', textvariable=self.btnbackVar, command=self.btnback_Cmd, style='Tbtnback.TButton')
        self.btnback.setText = lambda x: self.btnbackVar.set(x)
        self.btnback.text = lambda : self.btnbackVar.get()
        self.btnback.place(relx=0.05, rely=0.137, relwidth=0.166, relheight=0.057)

        self.btnrightVar = StringVar(value='右转')
        self.style.configure('Tbtnright.TButton', font=('宋体',9))
        self.btnright = Button(self.Frame1, text='右转', textvariable=self.btnrightVar, command=self.btnright_Cmd, style='Tbtnright.TButton')
        self.btnright.setText = lambda x: self.btnrightVar.set(x)
        self.btnright.text = lambda : self.btnrightVar.get()
        self.btnright.place(relx=0.05, rely=0.294, relwidth=0.166, relheight=0.057)

        self.txtrightVar = StringVar(value='90')
        self.txtright = Entry(self.Frame1, textvariable=self.txtrightVar, font=('宋体',9))
        self.txtright.setText = lambda x: self.txtrightVar.set(x)
        self.txtright.text = lambda : self.txtrightVar.get()
        self.txtright.place(relx=0.249, rely=0.294, relwidth=0.166, relheight=0.049)

        self.txtleftVar = StringVar(value='90')
        self.txtleft = Entry(self.Frame1, textvariable=self.txtleftVar, font=('宋体',9))
        self.txtleft.setText = lambda x: self.txtleftVar.set(x)
        self.txtleft.text = lambda : self.txtleftVar.get()
        self.txtleft.place(relx=0.249, rely=0.215, relwidth=0.166, relheight=0.049)

        self.btnleftVar = StringVar(value='左转')
        self.style.configure('Tbtnleft.TButton', font=('宋体',9))
        self.btnleft = Button(self.Frame1, text='左转', textvariable=self.btnleftVar, command=self.btnleft_Cmd, style='Tbtnleft.TButton')
        self.btnleft.setText = lambda x: self.btnleftVar.set(x)
        self.btnleft.text = lambda : self.btnleftVar.get()
        self.btnleft.place(relx=0.05, rely=0.215, relwidth=0.166, relheight=0.057)

        self.Label18Var = StringVar(value='已加盖印章ID')
        self.style.configure('TLabel18.TLabel', anchor='w', font=('宋体',9))
        self.Label18 = Label(self.Frame1, text='已加盖印章ID', textvariable=self.Label18Var, style='TLabel18.TLabel')
        self.Label18.setText = lambda x: self.Label18Var.set(x)
        self.Label18.text = lambda : self.Label18Var.get()
        self.Label18.place(relx=0.549, rely=0.763, relwidth=0.302, relheight=0.042)

        self.Label17Var = StringVar(value='的印章')
        self.style.configure('TLabel17.TLabel', anchor='w', font=('宋体',9))
        self.Label17 = Label(self.Frame1, text='的印章', textvariable=self.Label17Var, style='TLabel17.TLabel')
        self.Label17.setText = lambda x: self.Label17Var.set(x)
        self.Label17.text = lambda : self.Label17Var.get()
        self.Label17.place(relx=0.823, rely=0.685, relwidth=0.128, relheight=0.042)

        self.Label16Var = StringVar(value='ID为')
        self.style.configure('TLabel16.TLabel', anchor='w', font=('宋体',9))
        self.Label16 = Label(self.Frame1, text='ID为', textvariable=self.Label16Var, style='TLabel16.TLabel')
        self.Label16.setText = lambda x: self.Label16Var.set(x)
        self.Label16.text = lambda : self.Label16Var.get()
        self.Label16.place(relx=0.549, rely=0.685, relwidth=0.103, relheight=0.054)

        self.Label12Var = StringVar(value='速度')
        self.style.configure('TLabel12.TLabel', anchor='w', font=('宋体',9))
        self.Label12 = Label(self.Frame1, text='速度', textvariable=self.Label12Var, style='TLabel12.TLabel')
        self.Label12.setText = lambda x: self.Label12Var.set(x)
        self.Label12.text = lambda : self.Label12Var.get()
        self.Label12.place(relx=0.1, rely=0.391, relwidth=0.102, relheight=0.041)

        self.Label11Var = StringVar(value='颜色')
        self.style.configure('TLabel11.TLabel', anchor='w', font=('宋体',9))
        self.Label11 = Label(self.Frame1, text='颜色', textvariable=self.Label11Var, style='TLabel11.TLabel')
        self.Label11.setText = lambda x: self.Label11Var.set(x)
        self.Label11.text = lambda : self.Label11Var.get()
        self.Label11.place(relx=0.524, rely=0.235, relwidth=0.102, relheight=0.041)

        self.Label10Var = StringVar(value='大小')
        self.style.configure('TLabel10.TLabel', anchor='w', font=('宋体',9))
        self.Label10 = Label(self.Frame1, text='大小', textvariable=self.Label10Var, style='TLabel10.TLabel')
        self.Label10.setText = lambda x: self.Label10Var.set(x)
        self.Label10.text = lambda : self.Label10Var.get()
        self.Label10.place(relx=0.524, rely=0.157, relwidth=0.077, relheight=0.041)

        self.Label9Var = StringVar(value='画点')
        self.style.configure('TLabel9.TLabel', anchor='w', font=('宋体',9))
        self.Label9 = Label(self.Frame1, text='画点', textvariable=self.Label9Var, style='TLabel9.TLabel')
        self.Label9.setText = lambda x: self.Label9Var.set(x)
        self.Label9.text = lambda : self.Label9Var.get()
        self.Label9.place(relx=0.524, rely=0.078, relwidth=0.102, relheight=0.041)

        self.Label8Var = StringVar(value='边数')
        self.style.configure('TLabel8.TLabel', anchor='w', font=('宋体',9))
        self.Label8 = Label(self.Frame1, text='边数', textvariable=self.Label8Var, style='TLabel8.TLabel')
        self.Label8.setText = lambda x: self.Label8Var.set(x)
        self.Label8.text = lambda : self.Label8Var.get()
        self.Label8.place(relx=0.025, rely=0.841, relwidth=0.102, relheight=0.041)

        self.Label7Var = StringVar(value='绘制角度')
        self.style.configure('TLabel7.TLabel', anchor='w', font=('宋体',9))
        self.Label7 = Label(self.Frame1, text='绘制角度', textvariable=self.Label7Var, style='TLabel7.TLabel')
        self.Label7.setText = lambda x: self.Label7Var.set(x)
        self.Label7.text = lambda : self.Label7Var.get()
        self.Label7.place(relx=0.025, rely=0.763, relwidth=0.178, relheight=0.044)

        self.Label6Var = StringVar(value='半径')
        self.style.configure('TLabel6.TLabel', anchor='w', font=('宋体',9))
        self.Label6 = Label(self.Frame1, text='半径', textvariable=self.Label6Var, style='TLabel6.TLabel')
        self.Label6.setText = lambda x: self.Label6Var.set(x)
        self.Label6.text = lambda : self.Label6Var.get()
        self.Label6.place(relx=0.025, rely=0.685, relwidth=0.103, relheight=0.061)

        self.Label2Var = StringVar(value='画正多边形')
        self.style.configure('TLabel2.TLabel', anchor='w', font=('宋体',9))
        self.Label2 = Label(self.Frame1, text='画正多边形', textvariable=self.Label2Var, style='TLabel2.TLabel')
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda : self.Label2Var.get()
        self.Label2.place(relx=0.025, rely=0.607, relwidth=0.228, relheight=0.042)

        self.Label5Var = StringVar(value='朝向')
        self.style.configure('TLabel5.TLabel', anchor='w', font=('宋体',9))
        self.Label5 = Label(self.Frame1, text='朝向', textvariable=self.Label5Var, style='TLabel5.TLabel')
        self.Label5.setText = lambda x: self.Label5Var.set(x)
        self.Label5.text = lambda : self.Label5Var.get()
        self.Label5.place(relx=0.025, rely=0.548, relwidth=0.078, relheight=0.042)

        self.Label5Var = StringVar(value='Y')
        self.style.configure('TLabel5.TLabel', anchor='w', font=('宋体',9))
        self.Label5 = Label(self.Frame1, text='Y', textvariable=self.Label5Var, style='TLabel5.TLabel')
        self.Label5.setText = lambda x: self.Label5Var.set(x)
        self.Label5.text = lambda : self.Label5Var.get()
        self.Label5.place(relx=0.299, rely=0.47, relwidth=0.078, relheight=0.042)

        self.Label5Var = StringVar(value='X')
        self.style.configure('TLabel5.TLabel', anchor='w', font=('宋体',9))
        self.Label5 = Label(self.Frame1, text='X', textvariable=self.Label5Var, style='TLabel5.TLabel')
        self.Label5.setText = lambda x: self.Label5Var.set(x)
        self.Label5.text = lambda : self.Label5Var.get()
        self.Label5.place(relx=0.05, rely=0.47, relwidth=0.053, relheight=0.042)

        self.Label3Var = StringVar(value='步')
        self.style.configure('TLabel3.TLabel', anchor='w', font=('宋体',9))
        self.Label3 = Label(self.Frame1, text='步', textvariable=self.Label3Var, style='TLabel3.TLabel')
        self.Label3.setText = lambda x: self.Label3Var.set(x)
        self.Label3.text = lambda : self.Label3Var.get()
        self.Label3.place(relx=0.449, rely=0.078, relwidth=0.052, relheight=0.041)

        self.Label1Var = StringVar(value='步')
        self.style.configure('TLabel1.TLabel', anchor='w', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='步', textvariable=self.Label1Var, style='TLabel1.TLabel')
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.449, rely=0.157, relwidth=0.077, relheight=0.041)

        self.Label4Var = StringVar(value='度')
        self.style.configure('TLabel4.TLabel', anchor='w', font=('宋体',9))
        self.Label4 = Label(self.Frame1, text='度', textvariable=self.Label4Var, style='TLabel4.TLabel')
        self.Label4.setText = lambda x: self.Label4Var.set(x)
        self.Label4.text = lambda : self.Label4Var.get()
        self.Label4.place(relx=0.449, rely=0.235, relwidth=0.052, relheight=0.041)

        self.Label5Var = StringVar(value='度')
        self.style.configure('TLabel5.TLabel', anchor='w', font=('宋体',9))
        self.Label5 = Label(self.Frame1, text='度', textvariable=self.Label5Var, style='TLabel5.TLabel')
        self.Label5.setText = lambda x: self.Label5Var.set(x)
        self.Label5.text = lambda : self.Label5Var.get()
        self.Label5.place(relx=0.449, rely=0.313, relwidth=0.077, relheight=0.041)

        self.Label31Var = StringVar(value='背景大小')
        self.style.configure('TLabel31.TLabel', anchor='w', font=('宋体',9))
        self.Label31 = Label(self.Frame6, text='背景大小', textvariable=self.Label31Var, style='TLabel31.TLabel')
        self.Label31.setText = lambda x: self.Label31Var.set(x)
        self.Label31.text = lambda : self.Label31Var.get()
        self.Label31.place(relx=0.08, rely=0.717, relwidth=0.284, relheight=0.172)

        self.Label30Var = StringVar(value='背景图片')
        self.style.configure('TLabel30.TLabel', anchor='w', font=('宋体',9))
        self.Label30 = Label(self.Frame6, text='背景图片', textvariable=self.Label30Var, style='TLabel30.TLabel')
        self.Label30.setText = lambda x: self.Label30Var.set(x)
        self.Label30.text = lambda : self.Label30Var.get()
        self.Label30.place(relx=0.08, rely=0.497, relwidth=0.284, relheight=0.117)

        self.Label29Var = StringVar(value='背景颜色')
        self.style.configure('TLabel29.TLabel', anchor='w', font=('宋体',9))
        self.Label29 = Label(self.Frame6, text='背景颜色', textvariable=self.Label29Var, style='TLabel29.TLabel')
        self.Label29.setText = lambda x: self.Label29Var.set(x)
        self.Label29.text = lambda : self.Label29Var.get()
        self.Label29.place(relx=0.08, rely=0.221, relwidth=0.284, relheight=0.117)

    def retranslateUi(self):
        self.master.title(_('海龟驾驶台'))
        self.Frame6.configure(text=_('背景'))
        self.Frame5.configure(text=_('设定'))
        self.Frame4.configure(text=_('插入文字'))
        self.Frame3.configure(text=_('其他控制'))
        self.Frame2.configure(text=_('画笔'))
        self.btnsetlocation.setText(_('定位'))
        self.Frame1.configure(text=_('基本控制'))
        self.Label28.setText(_('代码'))
        self.save.entryconfigure(0, label=_('保存代码为'))
        self.save.entryconfigure(1, label=_('保存图片'))
        self.file.entryconfigure(0, label=_('保存'))
        self.print.entryconfigure(0, label=_('打印代码'))
        self.print.entryconfigure(1, label=_('打印图片'))
        self.file.entryconfigure(1, label=_('打印'))
        self.MainMenu.entryconfigure(0, label=_('文件'))
        self.help.entryconfigure(0, label=_('turtle范例'))
        self.help.entryconfigure(1, label=_('查看帮助'))
        self.help.entryconfigure(2, label=_('关于'))
        self.MainMenu.entryconfigure(1, label=_('帮助'))
        self.btndot.setText(_('画点'))
        self.btnchoosepic.setText(_('...'))
        self.btnsetdelay.setText(_('设置'))
        self.optrad.setText(_('弧度'))
        self.optangle.setText(_('角度'))
        self.Label27.setText(_('海龟模式'))
        self.Label26.setText(_('ms'))
        self.Label25.setText(_('动画延迟'))
        self.Label24.setText(_('为一圆周'))
        self.Label23.setText(_('角度单位'))
        self.Check2.setText(_('画笔移到文本右下角'))
        self.btninserttext.setText(_('书写'))
        self.Label22.setText(_('字号'))
        self.Label21.setText(_('字体样式'))
        self.Label19.setText(_('对齐方式'))
        self.Label20.setText(_('字体'))
        self.btnhide.setText(_('隐藏海龟'))
        self.btnclear.setText(_('清空'))
        self.btnreset.setText(_('重置'))
        self.btnendfill.setText(_('结束填充'))
        self.btnstartfill.setText(_('开始填充'))
        self.chkfill.setText(_('是否填充'))
        self.btnwidth.setText(_('设置'))
        self.btndown.setText(_('落笔'))
        self.btnup.setText(_('抬笔'))
        self.Label15.setText(_('填充颜色'))
        self.Label14.setText(_('画笔颜色'))
        self.Label13.setText(_('画笔粗细'))
        self.Label32.setText(_('x'))
        self.btnundo.setText(_('撤回'))
        self.btndeletestamp.setText(_('删除'))
        self.btnstamp.setText(_('盖印章'))
        self.btnhome.setText(_('返回原处'))
        self.btnforward.setText(_('前进'))
        self.btnback.setText(_('后退'))
        self.btnright.setText(_('右转'))
        self.btnleft.setText(_('左转'))
        self.Label18.setText(_('已加盖印章ID'))
        self.Label17.setText(_('的印章'))
        self.Label16.setText(_('ID为'))
        self.Label12.setText(_('速度'))
        self.Label11.setText(_('颜色'))
        self.Label10.setText(_('大小'))
        self.Label9.setText(_('画点'))
        self.Label8.setText(_('边数'))
        self.Label7.setText(_('绘制角度'))
        self.Label6.setText(_('半径'))
        self.Label2.setText(_('画正多边形'))
        self.Label5.setText(_('朝向'))
        self.Label5.setText(_('Y'))
        self.Label5.setText(_('X'))
        self.Label3.setText(_('步'))
        self.Label1.setText(_('步'))
        self.Label4.setText(_('度'))
        self.Label5.setText(_('度'))
        self.Label31.setText(_('背景大小'))
        self.Label30.setText(_('背景图片'))
        self.Label29.setText(_('背景颜色'))

class Application(Application_ui):
    def __init__(self, master):
        super().__init__(master)
        tr = gettext.translation('lang', localedir='i18n', languages=['en'], fallback=True)
        tr.install()
        self.retranslateUi()

    def txtcode_Modified(self, event):
        #TODO, Please finish the function here!
        self.txtcode.edit_modified(False)

    def btnsetlocation_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def savepy_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def savepic_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def printcode_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def printpic_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def example_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def seehelp_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def about_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def btndot_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def btnchoosepic_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def btnsetdelay_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def btninserttext_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def btnhide_Cmd(self, event=None):
        turtle.hideturtle()
        pass

    def btnclear_Cmd(self, event=None):
        turtle.clear()
        pass

    def btnreset_Cmd(self, event=None):
        turtle.reset()
        pass

    def btnendfill_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def btnstartfill_Cmd(self, event=None):
        turtle.begin_fill()
        pass

    def btnwidth_Cmd(self, event=None):
        turtle.width=int(self.txtwidth.get())
        pass

    def btndown_Cmd(self, event=None):
        turtle.pendown()
        pass

    def btnup_Cmd(self, event=None):
        turtle.penup()
        pass

    def btnundo_Cmd(self, event=None):
        turtle.undo()
        pass

    def btndeletestamp_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def btnstamp_Cmd(self, event=None):
        turtle.stamp()
        pass

    def btnhome_Cmd(self, event=None):
        turtle.home()
        pass

    def btnforward_Cmd(self, event=None):
        turtle.forward(float(self.txtforward.get()))
        pass

    def btnback_Cmd(self, event=None):
        turtle.back(float(self.txtback.get()))
        pass

    def btnright_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def btnleft_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

