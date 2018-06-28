Imports System.IO
Imports System.Net
Imports MaterialSkin

Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Dim SkinManager As MaterialSkinManager = MaterialSkinManager.Instance
        SkinManager.Theme = MaterialSkinManager.Themes.LIGHT
        SkinManager.ColorScheme = New ColorScheme(Primary.Indigo800, Primary.Indigo900, Primary.Indigo500, Accent.Red200, TextShade.WHITE)
        RefreshBadges()
    End Sub

    Private Sub RefreshBadges()
        Dim tClient As WebClient = New WebClient
        Dim tImage As Bitmap = Bitmap.FromStream(New MemoryStream(tClient.DownloadData("https://api.travis-ci.org/Richienb/ROS-Code.png?branch=master")))
        PictureBox1.Image = tImage
    End Sub

    Private Sub MaterialRaisedButton1_Click(sender As Object, e As EventArgs) Handles MaterialRaisedButton1.Click
        MaterialSingleLineTextField1.Visible = Not MaterialSingleLineTextField1.Visible
        PictureBox2.Visible = Not PictureBox2.Visible
        PictureBox1.Visible = Not PictureBox1.Visible
    End Sub

    Private Sub MaterialLabel1_Click(sender As Object, e As EventArgs)

    End Sub

    Private Sub MaterialSingleLineTextField1_TextChanged(sender As Object, e As EventArgs) Handles MaterialSingleLineTextField1.TextChanged
        If My.Computer.Network.IsAvailable = False Then
            PictureBox2.Image = My.Resources.offline
        End If
        Dim req As System.Net.WebRequest
        Dim res As System.Net.WebResponse
        req = System.Net.WebRequest.Create("https://raw.githubusercontent.com/Richienb/ROS-Code/" & MaterialSingleLineTextField1.Text & "/src/syntax.py")
        Try
            res = req.GetResponse()
            PictureBox2.Image = My.Resources.valid
        Catch ex As WebException
            PictureBox2.Image = My.Resources.invalid
        End Try
    End Sub

    Private Sub MaterialRaisedButton4_Click(sender As Object, e As EventArgs) Handles MaterialRaisedButton4.Click
        MaterialSingleLineTextField1.Visible = Not MaterialSingleLineTextField1.Visible
        PictureBox2.Visible = Not PictureBox2.Visible
        PictureBox1.Visible = Not PictureBox1.Visible
    End Sub

    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        RefreshBadges()
    End Sub
End Class
