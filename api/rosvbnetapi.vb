function compilefile(ByVal codepath As String)
    Dim retVal As Process
    retVal = Process.Start("python run-file.py " & codepath)
    return retVal
