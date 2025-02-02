VERSION 5.00
Begin VB.Form Form1 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "海龟驾驶台"
   ClientHeight    =   6660
   ClientLeft      =   120
   ClientTop       =   768
   ClientWidth     =   16356
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   ScaleHeight     =   6660
   ScaleWidth      =   16356
   StartUpPosition =   3  '窗口缺省
   Begin VB.Frame Frame6 
      Caption         =   "背景"
      Height          =   2175
      Left            =   5160
      TabIndex        =   86
      Top             =   3240
      Width           =   3495
      Begin VB.CommandButton btnchoosepic 
         Caption         =   "..."
         Height          =   300
         Left            =   2640
         TabIndex        =   100
         Top             =   960
         Width           =   375
      End
      Begin VB.TextBox Text25 
         Height          =   300
         Left            =   1320
         TabIndex        =   97
         Text            =   "500"
         Top             =   1560
         Width           =   495
      End
      Begin VB.TextBox Text24 
         Height          =   300
         Left            =   2520
         TabIndex        =   96
         Text            =   "500"
         Top             =   1560
         Width           =   495
      End
      Begin VB.TextBox Text23 
         Height          =   300
         Left            =   1320
         TabIndex        =   94
         Top             =   960
         Width           =   1275
      End
      Begin VB.TextBox Text22 
         Height          =   300
         Left            =   1320
         TabIndex        =   91
         Text            =   "0"
         Top             =   360
         Width           =   495
      End
      Begin VB.TextBox Text21 
         Height          =   300
         Left            =   1920
         TabIndex        =   90
         Text            =   "0"
         Top             =   360
         Width           =   495
      End
      Begin VB.TextBox Text20 
         Height          =   300
         Left            =   2520
         TabIndex        =   89
         Text            =   "0"
         Top             =   360
         Width           =   495
      End
      Begin VB.Label Label32 
         Caption         =   "x"
         BeginProperty Font 
            Name            =   "宋体"
            Size            =   10.8
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   255
         Left            =   2040
         TabIndex        =   98
         Top             =   1560
         Width           =   255
      End
      Begin VB.Label Label31 
         Caption         =   "背景大小"
         Height          =   375
         Left            =   240
         TabIndex        =   95
         Top             =   1560
         Width           =   855
      End
      Begin VB.Label Label30 
         Caption         =   "背景图片"
         Height          =   255
         Left            =   240
         TabIndex        =   93
         Top             =   1080
         Width           =   855
      End
      Begin VB.Label Label29 
         Caption         =   "背景颜色"
         Height          =   255
         Left            =   240
         TabIndex        =   92
         Top             =   480
         Width           =   855
      End
   End
   Begin VB.TextBox Text19 
      Height          =   2655
      Left            =   12600
      MultiLine       =   -1  'True
      TabIndex        =   84
      Text            =   "Form1.frx":0000
      Top             =   3600
      Width           =   3375
   End
   Begin VB.Frame Frame5 
      Caption         =   "设定"
      Height          =   2895
      Left            =   12600
      TabIndex        =   72
      Top             =   120
      Width           =   3375
      Begin VB.ComboBox commode 
         Height          =   300
         ItemData        =   "Form1.frx":0007
         Left            =   1080
         List            =   "Form1.frx":0014
         TabIndex        =   83
         Text            =   "Combo2"
         Top             =   2400
         Width           =   1215
      End
      Begin VB.CommandButton Command13 
         Caption         =   "设置"
         Height          =   375
         Left            =   2640
         TabIndex        =   81
         Top             =   1680
         Width           =   495
      End
      Begin VB.TextBox txtdelay 
         Height          =   300
         Left            =   1080
         TabIndex        =   79
         Top             =   1800
         Width           =   855
      End
      Begin VB.TextBox txtsetangle 
         Height          =   300
         Left            =   1080
         TabIndex        =   76
         Text            =   "360"
         Top             =   720
         Width           =   615
      End
      Begin VB.OptionButton optrad 
         Caption         =   "弧度"
         Height          =   300
         Left            =   120
         TabIndex        =   75
         Top             =   1320
         Width           =   855
      End
      Begin VB.OptionButton optangle 
         Caption         =   "角度"
         Height          =   300
         Left            =   120
         TabIndex        =   74
         Top             =   720
         Value           =   -1  'True
         Width           =   735
      End
      Begin VB.Label Label27 
         Caption         =   "海龟模式"
         Height          =   255
         Left            =   240
         TabIndex        =   82
         Top             =   2400
         Width           =   855
      End
      Begin VB.Label Label26 
         Caption         =   "ms"
         Height          =   255
         Left            =   2160
         TabIndex        =   80
         Top             =   1800
         Width           =   375
      End
      Begin VB.Label Label25 
         Caption         =   "动画延迟"
         Height          =   255
         Left            =   240
         TabIndex        =   78
         Top             =   1800
         Width           =   855
      End
      Begin VB.Label Label24 
         Caption         =   "为一圆周"
         Height          =   255
         Left            =   1920
         TabIndex        =   77
         Top             =   720
         Width           =   855
      End
      Begin VB.Label Label23 
         Caption         =   "角度单位"
         BeginProperty Font 
            Name            =   "宋体"
            Size            =   10.8
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   255
         Left            =   120
         TabIndex        =   73
         Top             =   240
         Width           =   1095
      End
   End
   Begin VB.Frame Frame4 
      Caption         =   "插入文字"
      Height          =   3015
      Left            =   9000
      TabIndex        =   53
      Top             =   3240
      Width           =   3375
      Begin VB.TextBox Text9 
         Height          =   270
         Left            =   2640
         TabIndex        =   64
         Text            =   "10"
         Top             =   1680
         Width           =   615
      End
      Begin VB.ComboBox Combo6 
         Height          =   300
         ItemData        =   "Form1.frx":002F
         Left            =   1440
         List            =   "Form1.frx":003C
         Style           =   2  'Dropdown List
         TabIndex        =   61
         Top             =   1680
         Width           =   1095
      End
      Begin VB.ComboBox Combo5 
         Height          =   300
         ItemData        =   "Form1.frx":0056
         Left            =   240
         List            =   "Form1.frx":0063
         Style           =   2  'Dropdown List
         TabIndex        =   60
         Top             =   1680
         Width           =   1095
      End
      Begin VB.ComboBox Combo4 
         Height          =   300
         ItemData        =   "Form1.frx":007D
         Left            =   1080
         List            =   "Form1.frx":008A
         Style           =   2  'Dropdown List
         TabIndex        =   59
         Top             =   960
         Width           =   1215
      End
      Begin VB.TextBox Text8 
         Height          =   540
         Left            =   120
         MultiLine       =   -1  'True
         TabIndex        =   56
         Top             =   240
         Width           =   2535
      End
      Begin VB.CheckBox Check2 
         Caption         =   "画笔移到文本右下角"
         Height          =   255
         Left            =   240
         TabIndex        =   55
         Top             =   2160
         Width           =   2055
      End
      Begin VB.CommandButton Command11 
         Caption         =   "书写"
         Height          =   300
         Left            =   360
         TabIndex        =   54
         Top             =   2520
         Width           =   1095
      End
      Begin VB.Label Label22 
         Caption         =   "字号"
         Height          =   255
         Left            =   2640
         TabIndex        =   63
         Top             =   1320
         Width           =   400
      End
      Begin VB.Label Label21 
         Caption         =   "字体样式"
         Height          =   255
         Left            =   1440
         TabIndex        =   62
         Top             =   1320
         Width           =   855
      End
      Begin VB.Label Label19 
         Caption         =   "对齐方式"
         Height          =   255
         Left            =   240
         TabIndex        =   58
         Top             =   960
         Width           =   855
      End
      Begin VB.Label Label20 
         Caption         =   "字体"
         Height          =   255
         Left            =   240
         TabIndex        =   57
         Top             =   1320
         Width           =   735
      End
   End
   Begin VB.Frame Frame3 
      Caption         =   "其他控制"
      Height          =   2895
      Left            =   9000
      TabIndex        =   47
      Top             =   120
      Width           =   3375
      Begin VB.CommandButton btnhide 
         Caption         =   "隐藏海龟"
         Height          =   375
         Left            =   240
         TabIndex        =   65
         Top             =   2160
         Width           =   1095
      End
      Begin VB.CommandButton btnclear 
         Caption         =   "清空"
         Height          =   350
         Left            =   1560
         TabIndex        =   52
         Top             =   1560
         Width           =   1095
      End
      Begin VB.CommandButton btnreset 
         Caption         =   "重置"
         Height          =   350
         Left            =   240
         TabIndex        =   51
         Top             =   1560
         Width           =   1095
      End
      Begin VB.CommandButton btnendfill 
         Caption         =   "结束填充"
         Height          =   375
         Left            =   1560
         TabIndex        =   50
         Top             =   960
         Width           =   1095
      End
      Begin VB.CommandButton btnstartfill 
         Caption         =   "开始填充"
         Height          =   375
         Left            =   240
         TabIndex        =   49
         Top             =   960
         Width           =   1095
      End
      Begin VB.CheckBox Check1 
         Caption         =   "是否填充"
         Height          =   375
         Left            =   240
         TabIndex        =   48
         Top             =   360
         Width           =   1335
      End
   End
   Begin VB.Frame Frame2 
      Caption         =   "画笔"
      Height          =   2895
      Left            =   5160
      TabIndex        =   34
      Top             =   120
      Width           =   3495
      Begin VB.TextBox txtfillb 
         Height          =   300
         Left            =   2520
         TabIndex        =   71
         Text            =   "0"
         Top             =   2160
         Width           =   495
      End
      Begin VB.TextBox txtfillg 
         Height          =   300
         Left            =   1920
         TabIndex        =   70
         Text            =   "0"
         Top             =   2160
         Width           =   495
      End
      Begin VB.TextBox txtfillr 
         Height          =   300
         Left            =   1320
         TabIndex        =   69
         Text            =   "0"
         Top             =   2160
         Width           =   495
      End
      Begin VB.TextBox txtpenb 
         Height          =   300
         Left            =   2520
         TabIndex        =   68
         Text            =   "0"
         Top             =   1560
         Width           =   495
      End
      Begin VB.TextBox txtpeng 
         Height          =   300
         Left            =   1920
         TabIndex        =   67
         Text            =   "0"
         Top             =   1560
         Width           =   495
      End
      Begin VB.TextBox txtpenr 
         Height          =   300
         Left            =   1320
         TabIndex        =   66
         Text            =   "0"
         Top             =   1560
         Width           =   495
      End
      Begin VB.CommandButton Command3 
         Caption         =   "设置"
         Height          =   350
         Left            =   2160
         TabIndex        =   39
         Top             =   960
         Width           =   1095
      End
      Begin VB.TextBox txtwidth 
         Height          =   300
         Left            =   1200
         TabIndex        =   38
         Text            =   "1"
         Top             =   960
         Width           =   800
      End
      Begin VB.CommandButton btndown 
         Caption         =   "落笔"
         Height          =   375
         Left            =   1800
         TabIndex        =   36
         Top             =   360
         Width           =   1095
      End
      Begin VB.CommandButton btnup 
         Caption         =   "抬笔"
         Height          =   375
         Left            =   240
         TabIndex        =   35
         Top             =   360
         Width           =   1095
      End
      Begin VB.Label Label15 
         Caption         =   "填充颜色"
         Height          =   255
         Left            =   240
         TabIndex        =   41
         Top             =   2280
         Width           =   855
      End
      Begin VB.Label Label14 
         Caption         =   "画笔颜色"
         Height          =   255
         Left            =   240
         TabIndex        =   40
         Top             =   1680
         Width           =   855
      End
      Begin VB.Label Label13 
         Caption         =   "画笔粗细"
         Height          =   255
         Left            =   240
         TabIndex        =   37
         Top             =   1080
         Width           =   975
      End
   End
   Begin VB.CommandButton Command5 
      Caption         =   "定位"
      Height          =   350
      Left            =   1680
      TabIndex        =   16
      Top             =   3600
      Width           =   1095
   End
   Begin VB.TextBox txty 
      Height          =   300
      Left            =   1920
      TabIndex        =   15
      Text            =   "0"
      Top             =   3120
      Width           =   795
   End
   Begin VB.Frame Frame1 
      Caption         =   "基本控制"
      Height          =   6375
      Left            =   240
      TabIndex        =   0
      Top             =   120
      Width           =   4695
      Begin VB.TextBox Text6 
         Height          =   300
         Left            =   2880
         TabIndex        =   103
         Text            =   "0"
         Top             =   1680
         Width           =   495
      End
      Begin VB.TextBox Text2 
         Height          =   300
         Left            =   3480
         TabIndex        =   102
         Text            =   "0"
         Top             =   1680
         Width           =   495
      End
      Begin VB.TextBox Text1 
         Height          =   300
         Left            =   4080
         TabIndex        =   101
         Text            =   "0"
         Top             =   1680
         Width           =   495
      End
      Begin VB.CommandButton Command14 
         Caption         =   "撤回"
         Height          =   300
         Left            =   3120
         TabIndex        =   99
         Top             =   2760
         Width           =   975
      End
      Begin VB.ListBox List1 
         Height          =   1128
         Left            =   2640
         TabIndex        =   88
         Top             =   5040
         Width           =   1935
      End
      Begin VB.TextBox Text5 
         Height          =   300
         Left            =   3240
         TabIndex        =   45
         Top             =   4200
         Width           =   615
      End
      Begin VB.CommandButton Command6 
         Caption         =   "删除"
         Height          =   350
         Left            =   2640
         TabIndex        =   44
         Top             =   3720
         Width           =   735
      End
      Begin VB.CommandButton Command4 
         Caption         =   "盖印章"
         Height          =   350
         Left            =   3000
         TabIndex        =   42
         Top             =   3240
         Width           =   975
      End
      Begin VB.TextBox Text4 
         Height          =   300
         Left            =   3240
         TabIndex        =   32
         Text            =   "5"
         Top             =   2160
         Width           =   800
      End
      Begin VB.TextBox Text3 
         Height          =   300
         Left            =   3240
         TabIndex        =   29
         Text            =   "50"
         Top             =   960
         Width           =   800
      End
      Begin VB.TextBox txtbiancount 
         Height          =   300
         Left            =   720
         TabIndex        =   27
         Text            =   "6"
         Top             =   5040
         Width           =   1755
      End
      Begin VB.TextBox txtrangle 
         Height          =   300
         Left            =   1080
         TabIndex        =   25
         Text            =   "360"
         Top             =   4560
         Width           =   1395
      End
      Begin VB.TextBox txtr 
         Height          =   300
         Left            =   600
         TabIndex        =   23
         Text            =   "100"
         Top             =   4080
         Width           =   1875
      End
      Begin VB.CommandButton btnhome 
         Caption         =   "返回原处"
         Height          =   350
         Left            =   840
         TabIndex        =   20
         Top             =   5520
         Width           =   1095
      End
      Begin VB.TextBox Text7 
         Height          =   300
         Left            =   600
         TabIndex        =   18
         Text            =   "0"
         Top             =   3240
         Width           =   675
      End
      Begin VB.TextBox txtx 
         Height          =   300
         Left            =   600
         TabIndex        =   17
         Text            =   "0"
         Top             =   2760
         Width           =   675
      End
      Begin VB.CommandButton btnforward 
         Caption         =   "前进"
         Height          =   350
         Left            =   240
         TabIndex        =   8
         Top             =   360
         Width           =   800
      End
      Begin VB.TextBox txtforward 
         Height          =   300
         Left            =   1200
         TabIndex        =   7
         Text            =   "100"
         Top             =   360
         Width           =   800
      End
      Begin VB.TextBox txtback 
         Height          =   300
         Left            =   1200
         TabIndex        =   6
         Text            =   "100"
         Top             =   960
         Width           =   795
      End
      Begin VB.CommandButton btnback 
         Caption         =   "后退"
         Height          =   350
         Left            =   240
         TabIndex        =   5
         Top             =   960
         Width           =   800
      End
      Begin VB.CommandButton btnright 
         Caption         =   "右转"
         Height          =   350
         Left            =   240
         TabIndex        =   4
         Top             =   2160
         Width           =   800
      End
      Begin VB.TextBox txtright 
         Height          =   300
         Left            =   1200
         TabIndex        =   3
         Text            =   "90"
         Top             =   2160
         Width           =   800
      End
      Begin VB.TextBox txtleft 
         Height          =   300
         Left            =   1200
         TabIndex        =   2
         Text            =   "90"
         Top             =   1560
         Width           =   800
      End
      Begin VB.CommandButton btnleft 
         Caption         =   "左转"
         Height          =   350
         Left            =   240
         TabIndex        =   1
         Top             =   1560
         Width           =   800
      End
      Begin VB.Label Label18 
         Caption         =   "已加盖印章ID"
         Height          =   255
         Left            =   2640
         TabIndex        =   87
         Top             =   4680
         Width           =   1455
      End
      Begin VB.Label Label17 
         Caption         =   "的印章"
         Height          =   255
         Left            =   3960
         TabIndex        =   46
         Top             =   4200
         Width           =   615
      End
      Begin VB.Label Label16 
         Caption         =   "ID为"
         Height          =   330
         Left            =   2640
         TabIndex        =   43
         Top             =   4200
         Width           =   495
      End
      Begin VB.Label Label12 
         Caption         =   "速度"
         Height          =   255
         Left            =   2640
         TabIndex        =   33
         Top             =   2280
         Width           =   375
      End
      Begin VB.Label Label11 
         Caption         =   "颜色"
         Height          =   252
         Left            =   2520
         TabIndex        =   31
         Top             =   1680
         Width           =   372
      End
      Begin VB.Label Label10 
         Caption         =   "大小"
         Height          =   255
         Left            =   2640
         TabIndex        =   30
         Top             =   1080
         Width           =   375
      End
      Begin VB.Label Label9 
         Caption         =   "画点"
         Height          =   255
         Left            =   2640
         TabIndex        =   28
         Top             =   480
         Width           =   615
      End
      Begin VB.Label Label8 
         Caption         =   "边数"
         Height          =   375
         Left            =   120
         TabIndex        =   26
         Top             =   5160
         Width           =   495
      End
      Begin VB.Label Label7 
         Caption         =   "绘制角度"
         Height          =   270
         Left            =   120
         TabIndex        =   24
         Top             =   4680
         Width           =   855
      End
      Begin VB.Label Label6 
         Caption         =   "半径"
         Height          =   375
         Left            =   120
         TabIndex        =   22
         Top             =   4200
         Width           =   495
      End
      Begin VB.Label Label2 
         Caption         =   "画正多边形"
         Height          =   255
         Left            =   120
         TabIndex        =   21
         Top             =   3720
         Width           =   1095
      End
      Begin VB.Label Label5 
         Caption         =   "朝向"
         Height          =   255
         Index           =   3
         Left            =   120
         TabIndex        =   19
         Top             =   3360
         Width           =   375
      End
      Begin VB.Label Label5 
         Caption         =   "Y"
         Height          =   255
         Index           =   2
         Left            =   1440
         TabIndex        =   14
         Top             =   2880
         Width           =   375
      End
      Begin VB.Label Label5 
         Caption         =   "X"
         Height          =   255
         Index           =   1
         Left            =   240
         TabIndex        =   13
         Top             =   2880
         Width           =   255
      End
      Begin VB.Label Label3 
         Caption         =   "步"
         Height          =   255
         Left            =   2160
         TabIndex        =   11
         Top             =   480
         Width           =   500
      End
      Begin VB.Label Label1 
         Caption         =   "步"
         Height          =   255
         Left            =   2160
         TabIndex        =   12
         Top             =   1080
         Width           =   500
      End
      Begin VB.Label Label4 
         Caption         =   "度"
         Height          =   255
         Left            =   2160
         TabIndex        =   10
         Top             =   1680
         Width           =   500
      End
      Begin VB.Label Label5 
         Caption         =   "度"
         Height          =   255
         Index           =   0
         Left            =   2160
         TabIndex        =   9
         Top             =   2280
         Width           =   500
      End
   End
   Begin VB.Label Label28 
      Caption         =   "代码"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   10.8
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   255
      Left            =   12600
      TabIndex        =   85
      Top             =   3240
      Width           =   1095
   End
   Begin VB.Menu file 
      Caption         =   "文件"
      Begin VB.Menu save 
         Caption         =   "保存"
         Begin VB.Menu savepy 
            Caption         =   "保存代码为"
         End
         Begin VB.Menu savepic 
            Caption         =   "保存图片"
         End
      End
      Begin VB.Menu print 
         Caption         =   "打印"
         Begin VB.Menu printcode 
            Caption         =   "打印代码"
         End
         Begin VB.Menu printpic 
            Caption         =   "打印图片"
         End
      End
   End
   Begin VB.Menu help 
      Caption         =   "帮助"
      Begin VB.Menu example 
         Caption         =   "turtle范例"
      End
      Begin VB.Menu seehelp 
         Caption         =   "查看帮助"
      End
      Begin VB.Menu about 
         Caption         =   "关于"
      End
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
