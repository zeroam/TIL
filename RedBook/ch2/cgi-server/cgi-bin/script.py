import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
url = form.getvalue('url')

print('Content-Type: text/plain')
print()

print('Welcome... CGI Scripts')
print('name is', name)
print('email is', email)
print('url is', url)
