# POST https://api-us.faceplusplus.com/facepp/v3/detect

import requests
import datetime
import FacePPAuth
import os
import json
import base64 

URL = "https://api-us.faceplusplus.com/facepp/v3/detect?"
API_KEY = "api_key=" + FacePPAuth.api_key
API_SECRET = "api_secret=" + FacePPAuth.api_secret


print("================== DTECT FACE =======================\n")

files = {'image_file': open('/home/osboxes/Face++/FacePPApi/Img/Img_3.jpg', 'rb')}

res = requests.post(URL + API_KEY + "&" + API_SECRET, files=files)

print("================== DETECT FACESET RES =======================\n")
strRes = res.content.decode('utf-8')
print(strRes)

cwd = os.getcwd()
with open(cwd + "/Res_DetectFace.txt", "a") as myfile:
 curTime  = str(datetime.datetime.now())
 myfile.write("========================= "+ curTime +" ============================ \n")
 myfile.write(strRes)
 myfile.write("\n")
 myfile.write("\n")
