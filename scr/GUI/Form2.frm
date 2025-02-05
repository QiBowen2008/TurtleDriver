VERSION 5.00
Begin VB.Form Form2 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "关于"
   ClientHeight    =   2340
   ClientLeft      =   48
   ClientTop       =   396
   ClientWidth     =   4632
   LinkTopic       =   "Form2"
   MaxButton       =   0   'False
   ScaleHeight     =   2340
   ScaleWidth      =   4632
   StartUpPosition =   3  '窗口缺省
   Begin VB.CommandButton Command2 
      Caption         =   "检查更新"
      Height          =   372
      Left            =   2880
      TabIndex        =   4
      Top             =   1560
      Width           =   1092
   End
   Begin VB.CommandButton Command1 
      Caption         =   "Github仓库"
      Height          =   372
      Left            =   2880
      TabIndex        =   3
      Top             =   1080
      Width           =   1092
   End
   Begin VB.Label Label3 
      Caption         =   "开发者：Buger"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   12
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   372
      Left            =   360
      TabIndex        =   2
      Top             =   1680
      Width           =   1692
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
      Height          =   372
      Left            =   360
      TabIndex        =   1
      Top             =   1200
      Width           =   1332
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
      TabIndex        =   0
      Top             =   240
      Width           =   3495
   End
End
Attribute VB_Name = "Form2"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
