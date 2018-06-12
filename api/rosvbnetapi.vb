function compilefile(ByVal codepath As String)
    Dim retVal As Process
    retVal = Process.Start("python compile.py " & codepath)
    return retVal
