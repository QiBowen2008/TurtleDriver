VERSION 5.00
Begin VB.Form Form2 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "关于"
   ClientHeight    =   3090
   ClientLeft      =   45
   ClientTop       =   390
   ClientWidth     =   5280
   LinkTopic       =   "Form2"
   MaxButton       =   0   'False
   ScaleHeight     =   3090
   ScaleWidth      =   5280
   StartUpPosition =   3  '窗口缺省
   Begin VB.CommandButton Command1 
      Caption         =   "确定"
      Height          =   615
      Left            =   1800
      TabIndex        =   0
      Top             =   2160
      Width           =   1575
   End
   Begin VB.Label Label2 
      Caption         =   "版本1.0"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   12
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   360
      TabIndex        =   2
      Top             =   1200
      Width           =   1335
   End
   Begin VB.Label Label1 
      Caption         =   "海龟驾驶台"
      BeginProperty Font 
         Name            =   "微软雅黑"
         Size            =   24
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   615
      Left            =   240
      TabIndex        =   1
      Top             =   240
      Width           =   3495
   End
End
Attribute VB_Name = "Form2"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
