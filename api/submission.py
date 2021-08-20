import requests
from flask_restful import Api, Resource, reqparse, request
import json

class submission(Resource):
  '''
  def get(self):
    return {
      'resultStatus': 'SUCCESS',
      'message': "submission"
      }
  '''

  def post(self):
    try:
      if request.data != "":
        data = json.loads((request.data).decode("UTF-8"))

        t = data["fileData"]["fileType"]

        if t == 0:
          upload_text(data)
        elif t == 1:
          upload_image(data)
        elif t == 2:
          upload_video(data)
        elif t == 3:
          upload_audio(data)
        else:
          return

        final_ret = {"status": "Success"}
        return final_ret
    except:
      pass


def upload_text(data):
  try:
    url = 'https://theamplificationproject.org/contribution'

    headers = {
      'Content-Type': 'multipart/form-data; boundary=---------------------------38375585703627189211349212993',
      'Cookie':  'ce1b76a4d055540c2ad919145fd6a3a5=bd983d63d6618f76f37172638fc96a5e'
    }

    b = '-----------------------------38375585703627189211349212993\r\n'

    type = 'Content-Disposition: form-data; name=\"contribution_type\"\r\n\r\n{}\r\n'.format(9)
    file = 'Content-Disposition: form-data; name=\"contributed_file\"; filename=\"{}\"\r\nContent-Type: text/plain\r\n\r\n'.format(data["fileData"]["title"])
    file_contents = '{}\r\n'.format(data["fileData"]["files"][0]["file_contents"])
    title = 'Content-Disposition: form-data; name=\"Elements[50][0][text]\"\r\n\r\n{}\r\n'.format(data["imageData"]["title"])

    sent_authors = ""
    try:
      sent_a_first = data["personalData"]["creator"]["firstNames"]
      sent_a_last = data["personalData"]["creator"]["lastNames"]
      n = 0
      while n < len(sent_a_first)-1:
        sent_authors += sent_a_first[n] + " " + sent_a_last[n] + ", "
        n += 1
      sent_authors += sent_a_first[n] + " " + sent_a_last[n]
    except:
      pass
    authors = 'Content-Disposition: form-data; name=\"Elements[39][0][text]\"\r\n\r\n{}\r\n'.format(sent_authors)

    sent_contributors = ""
    try:
      sent_c_first = data["personalData"]["contributor"]["firstNames"]
      sent_c_last = data["personalData"]["contributor"]["lastNames"]
      n = 0
      while n < len(sent_c_first)-1:
        sent_contributors += sent_c_first[n] + " " + sent_c_last[n] + ", "
        n += 1
      sent_contributors += sent_c_first[n] + " " + sent_c_last[n]
    except:
      pass
    contributor = 'Content-Disposition: form-data; name=\"Elements[37][0][text]\"\r\n\r\n{}\r\n'.format(sent_contributors)

    sent_statement = ""
    try:
      #data["personalData"]["creator"]["bio"]
      pass
    except:
      pass
    statement = 'Content-Disposition: form-data; name=\"Elements[48][0][text]\"\r\n\r\n{}\r\n'.format("")

    sent_description = ""
    try:
      sent_description = data["contributionData"]["description"]
    except:
      pass
    description = 'Content-Disposition: form-data; name=\"Elements[41][0][text]\"\r\n\r\n{}\r\n'.format(sent_description)

    sent_date = ""
    try:
      sent_date = data["contributionData"]["completionYear"]
    except:
      pass
    date = 'Content-Disposition: form-data; name=\"Elements[40][0][text]\"\r\n\r\n{}\r\n'.format(sent_date)

    sent_country = ""
    try:
      sent_country = data["imageData"]["country"]
      sent_city = sent_country = data["imageData"]["city"]
      if sent_country != None and sent_city != None:
        sent_country = sent_country + " " + sent_city
      elif sent_city != None:
        sent_country = sent_city
      elif sent_country == None and sent_city == None:
        sent_country = ""
    except:
      pass
    country = 'Content-Disposition: form-data; name=\"Elements[38][0][text]\"\r\n\r\n{}\r\n'.format(sent_country)

    type2 = 'Content-Disposition: form-data; name=\"Elements[51][0][text]\"\r\n\r\n{}\r\n'.format("")
    collection = 'Content-Disposition: form-data; name=\"Elements[46][0][text]\"\r\n\r\n{}\r\n'.format("")

    sent_language = ""
    try:
      sent_language = data["imageData"]["language"]
    except:
      pass
    language = 'Content-Disposition: form-data; name=\"Elements[44][0][text]\"\r\n\r\n{}\r\n'.format(sent_language)

    sent_rights = ""
    try:
      sent_rights = data["contributionData"]["rights"]
    except:
      pass
    rights = 'Content-Disposition: form-data; name=\"Elements[47][0][text]\"\r\n\r\n{}\r\n'.format(sent_rights)

    sent_keywords = ""
    try:
      sent_keywords = ",".join(data["contributionData"]["tags"])
    except:
      pass
    keywords = 'Content-Disposition: form-data; name=\"Elements[49][0][text]\"\r\n\r\n{}\r\n'.format(sent_keywords)

    email = 'Content-Disposition: form-data; name=\"contribution_email\"\r\n\r\n{}\r\n'.format(data["personalData"]["email"])

    lat = 'Content-Disposition: form-data; name=\"geolocation[latitude]\"\r\n\r\n{}\r\n'.format(31.929788123292955)
    long = 'Content-Disposition: form-data; name=\"geolocation[longitude]\"\r\n\r\n{}\r\n'.format(40.47258678631431)

    print(data["contributionData"])

    end = "-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"geolocation[zoom_level]\"\r\n\r\n7\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"geolocation[map_type]\"\r\n\r\nLeaflet\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"geolocation[address]\"\r\n\r\n\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"contribution-public\"\r\n\r\n0\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"contribution-public\"\r\n\r\n1\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"contribution-anonymous\"\r\n\r\n0\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"terms-agree\"\r\n\r\n0\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"terms-agree\"\r\n\r\n1\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"form-submit\"\r\n\r\nContribute\r\n-----------------------------38375585703627189211349212993\r\nContent-Disposition: form-data; name=\"csrf_token\"\r\n\r\nf32958ce252a7308fef41d11e4b1d29f\r\n-----------------------------38375585703627189211349212993--\r\n"

    payload = b+type+b+file+file_contents+b+title+b+authors+b+contributor+b+statement+b+description+b+date+b+country+b+type2+b+collection+b+language+b+rights+b+keywords+b+email+b+lat+b+long+end

    r = requests.post(url, headers=headers, data=payload)
  except:
    return False

def upload_image(data):
  print(1)

def upload_video(data):
  print(2)

def upload_audio(data):
  print(3)


'''
    print(self)
    parser = reqparse.RequestParser()
    parser.add_argument('type', type=str)
    parser.add_argument('message', type=str)
    args = parser.parse_args()
    print(args)
    # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

    request_type = args['type']
    request_json = args['message']
    # ret_status, ret_msg = ReturnData(request_type, request_json)
    # currently just returning the req straight
    ret_status = request_type
    ret_msg = request_json

    if ret_msg:
      #message = "Your Message Requested: {}".format(ret_msg)
      message = ret_msg
    else:
      message = "empty"
'''
