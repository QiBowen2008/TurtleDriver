VERSION 5.00
Begin VB.Form Form1 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "�����ʻ̨"
   ClientHeight    =   5988
   ClientLeft      =   120
   ClientTop       =   468
   ClientWidth     =   15072
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   ScaleHeight     =   5988
   ScaleWidth      =   15072
   StartUpPosition =   3  '����ȱʡ
   Begin VB.Frame Frame6 
      Caption         =   "����"
      Height          =   2532
      Left            =   5160
      TabIndex        =   74
      Top             =   3240
      Width           =   3012
      Begin VB.CommandButton Command1 
         Caption         =   "Command1"
         Height          =   372
         Left            =   1680
         TabIndex        =   95
         Top             =   2040
         Width           =   852
      End
      Begin VB.CommandButton btnsetback 
         Caption         =   "����ԭ��"
         Height          =   350
         Left            =   240
         TabIndex        =   92
         Top             =   2040
         Width           =   1095
      End
      Begin VB.CommandButton btnchoosepic 
         Caption         =   "..."
         Height          =   300
         Left            =   2520
         TabIndex        =   88
         Top             =   960
         Width           =   375
      End
      Begin VB.TextBox Text25 
         Height          =   300
         Left            =   1200
         TabIndex        =   85
         Text            =   "500"
         Top             =   1560
         Width           =   495
      End
      Begin VB.TextBox Text24 
         Height          =   300
         Left            =   2400
         TabIndex        =   84
         Text            =   "500"
         Top             =   1560
         Width           =   495
      End
      Begin VB.TextBox txtpic 
         Height          =   300
         Left            =   1200
         TabIndex        =   82
         Top             =   960
         Width           =   1275
      End
      Begin VB.TextBox txtbackcolorr 
         Height          =   300
         Left            =   1200
         TabIndex        =   79
         Text            =   "0"
         Top             =   360
         Width           =   495
      End
      Begin VB.TextBox txtbackcolorrtxtbackcolorg 
         Height          =   300
         Left            =   1800
         TabIndex        =   78
         Text            =   "0"
         Top             =   360
         Width           =   495
      End
      Begin VB.TextBox txtbackcolorrb 
         Height          =   300
         Left            =   2400
         TabIndex        =   77
         Text            =   "0"
         Top             =   360
         Width           =   495
      End
      Begin VB.Label Label32 
         Caption         =   "x"
         BeginProperty Font 
            Name            =   "����"
            Size            =   10.8
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   252
         Left            =   1920
         TabIndex        =   86
         Top             =   1560
         Width           =   252
      End
      Begin VB.Label Label31 
         Caption         =   "������С"
         Height          =   375
         Left            =   240
         TabIndex        =   83
         Top             =   1560
         Width           =   855
      End
      Begin VB.Label Label30 
         Caption         =   "����ͼƬ"
         Height          =   255
         Left            =   240
         TabIndex        =   81
         Top             =   1080
         Width           =   855
      End
      Begin VB.Label Label29 
         Caption         =   "������ɫ"
         Height          =   255
         Left            =   240
         TabIndex        =   80
         Top             =   480
         Width           =   855
      End
   End
   Begin VB.TextBox txtcode 
      Height          =   2292
      Left            =   11760
      MultiLine       =   -1  'True
      TabIndex        =   72
      Text            =   "Form1.frx":0000
      Top             =   3480
      Width           =   3252
   End
   Begin VB.Frame Frame5 
      Caption         =   "�趨"
      Height          =   2895
      Left            =   11760
      TabIndex        =   64
      Top             =   120
      Width           =   3252
      Begin VB.ComboBox commode 
         Height          =   276
         ItemData        =   "Form1.frx":0007
         Left            =   1080
         List            =   "Form1.frx":0014
         TabIndex        =   71
         Text            =   "Combo2"
         Top             =   2040
         Width           =   1215
      End
      Begin VB.TextBox txtsetangle 
         Height          =   300
         Left            =   1080
         TabIndex        =   68
         Text            =   "360"
         Top             =   720
         Width           =   615
      End
      Begin VB.OptionButton optrad 
         Caption         =   "����"
         Height          =   300
         Left            =   120
         TabIndex        =   67
         Top             =   1200
         Width           =   855
      End
      Begin VB.OptionButton optangle 
         Caption         =   "�Ƕ�"
         Height          =   300
         Left            =   120
         TabIndex        =   66
         Top             =   720
         Value           =   -1  'True
         Width           =   735
      End
      Begin VB.Label Label26 
         Caption         =   "ms"
         Height          =   252
         Left            =   2160
         TabIndex        =   94
         Top             =   1680
         Width           =   252
      End
      Begin VB.Label Label27 
         Caption         =   "����ģʽ"
         Height          =   252
         Left            =   240
         TabIndex        =   70
         Top             =   2040
         Width           =   852
      End
      Begin VB.Label Label24 
         Caption         =   "ΪһԲ��"
         Height          =   255
         Left            =   1920
         TabIndex        =   69
         Top             =   720
         Width           =   855
      End
      Begin VB.Label Label23 
         Caption         =   "�Ƕȵ�λ"
         BeginProperty Font 
            Name            =   "����"
            Size            =   10.8
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   255
         Left            =   120
         TabIndex        =   65
         Top             =   240
         Width           =   1095
      End
   End
   Begin VB.Frame Frame4 
      Caption         =   "��������"
      Height          =   3015
      Left            =   8280
      TabIndex        =   45
      Top             =   2400
      Width           =   3375
      Begin VB.TextBox cominsertfontsize 
         Height          =   270
         Left            =   2640
         TabIndex        =   56
         Text            =   "10"
         Top             =   1680
         Width           =   615
      End
      Begin VB.ComboBox cominsertstyle 
         Height          =   300
         ItemData        =   "Form1.frx":002F
         Left            =   1440
         List            =   "Form1.frx":003C
         Style           =   2  'Dropdown List
         TabIndex        =   53
         Top             =   1680
         Width           =   1095
      End
      Begin VB.ComboBox cominserttext 
         Height          =   300
         ItemData        =   "Form1.frx":0056
         Left            =   240
         List            =   "Form1.frx":0063
         Style           =   2  'Dropdown List
         TabIndex        =   52
         Top             =   1680
         Width           =   1095
      End
      Begin VB.ComboBox comagline 
         Height          =   300
         ItemData        =   "Form1.frx":007D
         Left            =   1080
         List            =   "Form1.frx":008A
         Style           =   2  'Dropdown List
         TabIndex        =   51
         Top             =   960
         Width           =   1215
      End
      Begin VB.TextBox txtinsert 
         Height          =   540
         Left            =   120
         MultiLine       =   -1  'True
         TabIndex        =   48
         Top             =   240
         Width           =   3012
      End
      Begin VB.CheckBox Check2 
         Caption         =   "�����Ƶ��ı����½�"
         Height          =   255
         Left            =   240
         TabIndex        =   47
         Top             =   2160
         Width           =   2055
      End
      Begin VB.CommandButton btninserttext 
         Caption         =   "��д"
         Height          =   300
         Left            =   360
         TabIndex        =   46
         Top             =   2520
         Width           =   1095
      End
      Begin VB.Label Label22 
         Caption         =   "�ֺ�"
         Height          =   255
         Left            =   2640
         TabIndex        =   55
         Top             =   1320
         Width           =   400
      End
      Begin VB.Label Label21 
         Caption         =   "������ʽ"
         Height          =   255
         Left            =   1440
         TabIndex        =   54
         Top             =   1320
         Width           =   855
      End
      Begin VB.Label Label19 
         Caption         =   "���뷽ʽ"
         Height          =   255
         Left            =   240
         TabIndex        =   50
         Top             =   960
         Width           =   855
      End
      Begin VB.Label Label20 
         Caption         =   "����"
         Height          =   255
         Left            =   240
         TabIndex        =   49
         Top             =   1320
         Width           =   735
      End
   End
   Begin VB.Frame Frame3 
      Caption         =   "��������"
      Height          =   2172
      Left            =   8280
      TabIndex        =   40
      Top             =   120
      Width           =   3375
      Begin VB.CommandButton btnhide 
         Caption         =   "���غ���"
         Height          =   375
         Left            =   240
         TabIndex        =   57
         Top             =   1560
         Width           =   1095
      End
      Begin VB.CommandButton btnclear 
         Caption         =   "���"
         Height          =   350
         Left            =   1560
         TabIndex        =   44
         Top             =   960
         Width           =   1095
      End
      Begin VB.CommandButton btnreset 
         Caption         =   "����"
         Height          =   350
         Left            =   240
         TabIndex        =   43
         Top             =   960
         Width           =   1095
      End
      Begin VB.CommandButton btnendfill 
         Caption         =   "�������"
         Height          =   375
         Left            =   1560
         TabIndex        =   42
         Top             =   360
         Width           =   1095
      End
      Begin VB.CommandButton btnstartfill 
         Caption         =   "��ʼ���"
         Height          =   375
         Left            =   240
         TabIndex        =   41
         Top             =   360
         Width           =   1095
      End
   End
   Begin VB.Frame Frame2 
      Caption         =   "����"
      Height          =   2895
      Left            =   5160
      TabIndex        =   27
      Top             =   120
      Width           =   3012
      Begin VB.TextBox txtfillb 
         Height          =   300
         Left            =   2280
         TabIndex        =   63
         Text            =   "0"
         Top             =   2160
         Width           =   495
      End
      Begin VB.TextBox txtfillg 
         Height          =   300
         Left            =   1680
         TabIndex        =   62
         Text            =   "0"
         Top             =   2160
         Width           =   495
      End
      Begin VB.TextBox txtfillr 
         Height          =   300
         Left            =   1080
         TabIndex        =   61
         Text            =   "0"
         Top             =   2160
         Width           =   495
      End
      Begin VB.TextBox txtpenb 
         Height          =   300
         Left            =   2280
         TabIndex        =   60
         Text            =   "0"
         Top             =   1560
         Width           =   495
      End
      Begin VB.TextBox txtpeng 
         Height          =   300
         Left            =   1680
         TabIndex        =   59
         Text            =   "0"
         Top             =   1560
         Width           =   495
      End
      Begin VB.TextBox txtpenr 
         Height          =   300
         Left            =   1080
         TabIndex        =   58
         Text            =   "0"
         Top             =   1560
         Width           =   495
      End
      Begin VB.CommandButton btnwidth 
         Caption         =   "����"
         Height          =   350
         Left            =   2040
         TabIndex        =   32
         Top             =   960
         Width           =   732
      End
      Begin VB.TextBox txtwidth 
         Height          =   300
         Left            =   1080
         TabIndex        =   31
         Text            =   "1"
         Top             =   960
         Width           =   800
      End
      Begin VB.CommandButton btndown 
         Caption         =   "���"
         Height          =   375
         Left            =   1080
         TabIndex        =   29
         Top             =   360
         Width           =   732
      End
      Begin VB.CommandButton btnup 
         Caption         =   "̧��"
         Height          =   375
         Left            =   240
         TabIndex        =   28
         Top             =   360
         Width           =   732
      End
      Begin VB.Label Label15 
         Caption         =   "�����ɫ"
         Height          =   255
         Left            =   240
         TabIndex        =   34
         Top             =   2280
         Width           =   855
      End
      Begin VB.Label Label14 
         Caption         =   "������ɫ"
         Height          =   255
         Left            =   240
         TabIndex        =   33
         Top             =   1680
         Width           =   855
      End
      Begin VB.Label Label13 
         Caption         =   "���ʴ�ϸ"
         Height          =   252
         Left            =   240
         TabIndex        =   30
         Top             =   1080
         Width           =   732
      End
   End
   Begin VB.Frame Frame1 
      Caption         =   "��������"
      Height          =   5652
      Left            =   240
      TabIndex        =   0
      Top             =   120
      Width           =   4812
      Begin VB.CommandButton btnsetspeed 
         Caption         =   "����"
         Height          =   350
         Left            =   1680
         TabIndex        =   93
         Top             =   2280
         Width           =   800
      End
      Begin VB.CommandButton btnsetlocation 
         Caption         =   "��λ"
         Height          =   350
         Left            =   1440
         TabIndex        =   90
         Top             =   2880
         Width           =   1095
      End
      Begin VB.CommandButton btndot 
         Caption         =   "����"
         Height          =   372
         Left            =   3240
         TabIndex        =   89
         Top             =   1320
         Width           =   852
      End
      Begin VB.CommandButton btnundo 
         Caption         =   "����"
         Height          =   420
         Left            =   3120
         TabIndex        =   87
         Top             =   2280
         Width           =   975
      End
      Begin VB.ListBox lststampid 
         Height          =   948
         ItemData        =   "Form1.frx":00A4
         Left            =   2640
         List            =   "Form1.frx":00A6
         TabIndex        =   76
         Top             =   4440
         Width           =   1935
      End
      Begin VB.TextBox txtstampid 
         Height          =   300
         Left            =   3960
         TabIndex        =   38
         Top             =   3600
         Width           =   615
      End
      Begin VB.CommandButton btndeletestamp 
         Caption         =   "ɾ��"
         Height          =   350
         Left            =   2640
         TabIndex        =   37
         Top             =   3600
         Width           =   735
      End
      Begin VB.CommandButton btnstamp 
         Caption         =   "��ӡ��"
         Height          =   350
         Left            =   2640
         TabIndex        =   35
         Top             =   3120
         Width           =   975
      End
      Begin VB.TextBox Text4 
         Height          =   300
         Left            =   720
         TabIndex        =   25
         Text            =   "5"
         Top             =   2280
         Width           =   800
      End
      Begin VB.TextBox txtdotsize 
         Height          =   300
         Left            =   3240
         TabIndex        =   23
         Text            =   "50"
         Top             =   840
         Width           =   800
      End
      Begin VB.TextBox txtbiancount 
         Height          =   300
         Left            =   720
         TabIndex        =   21
         Text            =   "6"
         Top             =   4680
         Width           =   1755
      End
      Begin VB.TextBox txtrangle 
         Height          =   300
         Left            =   1080
         TabIndex        =   19
         Text            =   "360"
         Top             =   4200
         Width           =   1395
      End
      Begin VB.TextBox txtr 
         Height          =   300
         Left            =   600
         TabIndex        =   17
         Text            =   "100"
         Top             =   3720
         Width           =   1875
      End
      Begin VB.CommandButton btnhome 
         Caption         =   "����ԭ��"
         Height          =   350
         Left            =   720
         TabIndex        =   14
         Top             =   5040
         Width           =   1095
      End
      Begin VB.TextBox Text7 
         Height          =   300
         Left            =   600
         TabIndex        =   13
         Text            =   "0"
         Top             =   2880
         Width           =   675
      End
      Begin VB.CommandButton btnforward 
         Caption         =   "ǰ��"
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
         Top             =   840
         Width           =   795
      End
      Begin VB.CommandButton btnback 
         Caption         =   "����"
         Height          =   350
         Left            =   240
         TabIndex        =   5
         Top             =   840
         Width           =   800
      End
      Begin VB.CommandButton btnright 
         Caption         =   "��ת"
         Height          =   350
         Left            =   240
         TabIndex        =   4
         Top             =   1800
         Width           =   800
      End
      Begin VB.TextBox txtright 
         Height          =   300
         Left            =   1200
         TabIndex        =   3
         Text            =   "90"
         Top             =   1800
         Width           =   800
      End
      Begin VB.TextBox txtleft 
         Height          =   300
         Left            =   1200
         TabIndex        =   2
         Text            =   "90"
         Top             =   1320
         Width           =   800
      End
      Begin VB.CommandButton btnleft 
         Caption         =   "��ת"
         Height          =   350
         Left            =   240
         TabIndex        =   1
         Top             =   1320
         Width           =   800
      End
      Begin VB.Label Label37 
         Caption         =   "����"
         Height          =   252
         Left            =   120
         TabIndex        =   91
         Top             =   2880
         Width           =   492
      End
      Begin VB.Label Label18 
         Caption         =   "�ѼӸ�ӡ��ID"
         Height          =   252
         Left            =   2640
         TabIndex        =   75
         Top             =   4200
         Width           =   1452
      End
      Begin VB.Label Label17 
         Caption         =   "��ӡ��"
         Height          =   252
         Left            =   3840
         TabIndex        =   39
         Top             =   3960
         Width           =   612
      End
      Begin VB.Label Label16 
         Caption         =   "IDΪ"
         Height          =   216
         Left            =   3480
         TabIndex        =   36
         Top             =   3720
         Width           =   372
      End
      Begin VB.Label Label12 
         Caption         =   "�ٶ�"
         Height          =   252
         Left            =   240
         TabIndex        =   26
         Top             =   2400
         Width           =   492
      End
      Begin VB.Label Label10 
         Caption         =   "��С"
         Height          =   252
         Left            =   2520
         TabIndex        =   24
         Top             =   960
         Width           =   372
      End
      Begin VB.Label Label9 
         Caption         =   "����"
         Height          =   252
         Left            =   2520
         TabIndex        =   22
         Top             =   480
         Width           =   492
      End
      Begin VB.Label Label8 
         Caption         =   "����"
         Height          =   252
         Left            =   120
         TabIndex        =   20
         Top             =   4800
         Width           =   492
      End
      Begin VB.Label Label7 
         Caption         =   "���ƽǶ�"
         Height          =   276
         Left            =   120
         TabIndex        =   18
         Top             =   4320
         Width           =   852
      End
      Begin VB.Label Label6 
         Caption         =   "�뾶"
         Height          =   372
         Left            =   120
         TabIndex        =   16
         Top             =   3840
         Width           =   492
      End
      Begin VB.Label Label2 
         Caption         =   "���������"
         Height          =   252
         Left            =   120
         TabIndex        =   15
         Top             =   3360
         Width           =   1092
      End
      Begin VB.Label Label3 
         Caption         =   "��"
         Height          =   252
         Left            =   2160
         TabIndex        =   11
         Top             =   480
         Width           =   252
      End
      Begin VB.Label Label1 
         Caption         =   "��"
         Height          =   252
         Left            =   2160
         TabIndex        =   12
         Top             =   960
         Width           =   372
      End
      Begin VB.Label Label4 
         Caption         =   "��"
         Height          =   252
         Left            =   2160
         TabIndex        =   10
         Top             =   1440
         Width           =   252
      End
      Begin VB.Label Label5 
         Caption         =   "��"
         Height          =   252
         Index           =   0
         Left            =   2160
         TabIndex        =   9
         Top             =   1920
         Width           =   372
      End
   End
   Begin VB.Label Label28 
      Caption         =   "����"
      BeginProperty Font 
         Name            =   "����"
         Size            =   10.8
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   252
      Left            =   11760
      TabIndex        =   73
      Top             =   3240
      Width           =   1092
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()

End Sub

Private Sub Frame1_DragDrop(Source As Control, X As Single, Y As Single)

End Sub

Private Sub lbly_Click()

End Sub
