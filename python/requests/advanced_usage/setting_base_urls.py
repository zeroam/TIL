from requests_toolbelt import sessions

http = sessions.BaseUrlSession(base_url='https://api.org')
http.get('/list')
http.get('/list/item')