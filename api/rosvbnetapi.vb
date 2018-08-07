function compilefile(ByVal codepath As String)
    Dim retVal As Process = Process.Start("python run-file.py " & codepath)
    return retVal
