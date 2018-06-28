Imports System.IO
Imports System.Net
Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub RefreshBadges()
        Dim tClient As WebClient = New WebClient
        Dim tImage As Bitmap = Bitmap.FromStream(New MemoryStream(tClient.DownloadData("https://img.shields.io/travis/Richienb/ROS-Code.svg?longCache=true&style=for-the-badge")))
        PictureBox1.Image = tImage
        tImage = Bitmap.FromStream(New MemoryStream(tClient.DownloadData("https://www.codefactor.io/repository/github/richienb/ros-code/badge?longCache=true&style=for-the-badge")))
        PictureBox2.Image = tImage
    End Sub
End Class
