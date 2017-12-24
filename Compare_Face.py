# POST https://api-us.faceplusplus.com/facepp/v3/compare

import requests
import datetime
import FacePPAuth
import os
import json

URL = "https://api-us.faceplusplus.com/facepp/v3/compare?"
API_KEY = "api_key=" + FacePPAuth.api_key
API_SECRET = "api_secret=" + FacePPAuth.api_secret
#OUTER_ID = "outer_id=oid1"
FACE_TOKEN1 = "face_token1=81ebbaeb300d52a2e4c218766641afdb"
FACE_TOKEN2 = "face_token2=8013f6fe89107122fac613c12beae403"

print("================== COMPARE FACE SET =======================\n")
res = requests.post(URL + API_KEY + "&" + API_SECRET + "&" + FACE_TOKEN1 + "&" + FACE_TOKEN2 )


print("================== RES OF FACE COMPARE =======================\n")
strRes = res.content.decode('utf-8')
print(strRes)
cwd = os.getcwd()
with open(cwd + "/Res_CompareFaceSet.txt", "a") as myfile:
 curTime  = str(datetime.datetime.now())
 myfile.write("========================= "+ curTime +" ============================ \n")
 myfile.write(strRes)
 myfile.write("\n")
 myfile.write("\n")
