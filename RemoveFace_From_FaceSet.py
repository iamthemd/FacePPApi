# POST https://api-us.faceplusplus.com/facepp/v3/faceset/removeface

import requests
import datetime
import FacePPAuth
import os
import json

URL = "https://api-us.faceplusplus.com/facepp/v3/faceset/removeface?"
API_KEY = "api_key=" + FacePPAuth.api_key
API_SECRET = "api_secret=" + FacePPAuth.api_secret
#DISPLAY_NAME = "display_name=faceset23dec"
OUTER_ID = "outer_id=oid1"
FACE_TOKEN = "face_token=" + ""	
print("================== REMOVE FACE FROM FACESET =======================\n")
res = requests.post(URL + API_KEY + "&" + API_SECRET + "&" + OUTER_ID + "&" + FACE_TOKEN)

print("================== REMOVED FACESET RES =======================\n")
strRes = res.content.decode('utf-8')
print(strRes)

cwd = os.getcwd()
with open(cwd + "/Res_RemoveFaceFromFaceSet.txt", "a") as myfile:
 curTime  = str(datetime.datetime.now())
 myfile.write("========================= "+ curTime +" ============================ \n")
 myfile.write(strRes)
 myfile.write("\n")
 myfile.write("\n")
