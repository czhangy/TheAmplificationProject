import requests

url = 'https://theamplificationproject.org/contribution'

headers = {
    'Content-Type': 'multipart/form-data; boundary=---------------------------38375585703627189211349212993',
    'Cookie':  'ce1b76a4d055540c2ad919145fd6a3a5=bd983d63d6618f76f37172638fc96a5e'
}

b = '-----------------------------38375585703627189211349212993\r\n'

type = 'Content-Disposition: form-data; name=\"contribution_type\"\r\n\r\n{}\r\n'.format(9)
file = 'Content-Disposition: form-data; name=\"contributed_file\"; filename=\"{}\"\r\nContent-Type: text/plain\r\n\r\n'.format("blue.txt")
file_contents = '{}\r\n'.format("Blue")
title = 'Content-Disposition: form-data; name=\"Elements[50][0][text]\"\r\n\r\n{}\r\n'.format("from python")
authors = 'Content-Disposition: form-data; name=\"Elements[39][0][text]\"\r\n\r\n{}\r\n'.format("bgrvfdcs")
contributor = 'Content-Disposition: form-data; name=\"Elements[37][0][text]\"\r\n\r\n{}\r\n'.format("qewdf")
statement = 'Content-Disposition: form-data; name=\"Elements[48][0][text]\"\r\n\r\n{}\r\n'.format("pkoikj")
description = 'Content-Disposition: form-data; name=\"Elements[41][0][text]\"\r\n\r\n{}\r\n'.format("yogfvc")
date = 'Content-Disposition: form-data; name=\"Elements[40][0][text]\"\r\n\r\n{}\r\n'.format("rvfecd")
country = 'Content-Disposition: form-data; name=\"Elements[38][0][text]\"\r\n\r\n{}\r\n'.format("vecdxlfred")
type2 = 'Content-Disposition: form-data; name=\"Elements[51][0][text]\"\r\n\r\n{}\r\n'.format("trfds")
collection = 'Content-Disposition: form-data; name=\"Elements[46][0][text]\"\r\n\r\n{}\r\n'.format("vecfdxs")
language = 'Content-Disposition: form-data; name=\"Elements[44][0][text]\"\r\n\r\n{}\r\n'.format("Eng")
rights = 'Content-Disposition: form-data; name=\"Elements[47][0][text]\"\r\n\r\n{}\r\n'.format("LOL")
keywords = 'Content-Disposition: form-data; name=\"Elements[49][0][text]\"\r\n\r\n{}\r\n'.format("yopagvcwds")
email = 'Content-Disposition: form-data; name=\"contribution_email\"\r\n\r\n{}\r\n'.format("me@example.com")
lat = 'Content-Disposition: form-data; name=\"geolocation[latitude]\"\r\n\r\n{}\r\n'.format(31.929788123292955)
long = 'Content-Disposition: form-data; name=\"geolocation[longitude]\"\r\n\r\n{}\r\n'.format(40.47258678631431)

end = "-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"geolocation[zoom_level]\"\r\n\r\n7\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"geolocation[map_type]\"\r\n\r\nLeaflet\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"geolocation[address]\"\r\n\r\n\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"contribution-public\"\r\n\r\n0\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"contribution-public\"\r\n\r\n1\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"contribution-anonymous\"\r\n\r\n0\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"terms-agree\"\r\n\r\n0\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"terms-agree\"\r\n\r\n1\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"form-submit\"\r\n\r\nContribute\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"csrf_token\"\r\n\r\nf32958ce252a7308fef41d11e4b1d29f\r\n-----------------------------38375585703627189211349212993--\r\n"

payload = b+type+b+file+file_contents+b+title+b+authors+b+contributor+b+statement+b+description+b+date+b+country+b+type2+b+collection+b+language+b+rights+b+keywords+b+email+b+lat+b+long+end

r = requests.post(url, headers=headers, data=payload)
