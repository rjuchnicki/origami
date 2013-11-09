import dropbox 

app_key = '1owd69l36nqbew5'
app_secret = 'vuqt00va8g5t4hp'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()

authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

access_token, user_id = flow.finish(code)
#print "access token: ", access_token
#print "user_id: ", user_id

client = dropbox.client.DropboxClient(access_token)
#print "client: ", client
#print 'linked account: ', client.account_info()

f = open('test.pptx')
response = client.put_file('/test.pptx', f)
print "uploaded:", response

#DropboxClient.share('/test.pptx')