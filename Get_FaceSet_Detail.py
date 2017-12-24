# POST https://api-us.faceplusplus.com/facepp/v3/faceset/getdetail

import requests
import datetime
import FacePPAuth
import os
import json

URL = "https://api-us.faceplusplus.com/facepp/v3/faceset/getdetail?"
API_KEY = "api_key=" + FacePPAuth.api_key
API_SECRET = "api_secret=" + FacePPAuth.api_secret
OUTER_ID = "outer_id=oid1"

print("================== GETTING FACE SET DETAIL =======================\n")
res = requests.post(URL + API_KEY + "&" + API_SECRET + "&" + OUTER_ID )


print("================== RES OF FACESET DETAIL =======================\n")
strRes = res.content.decode('utf-8')
print(strRes)
cwd = os.getcwd()
with open(cwd + "/Res_GetFaceSetDetail.txt", "a") as myfile:
 curTime  = str(datetime.datetime.now())
 myfile.write("========================= "+ curTime +" ============================ \n")
 myfile.write(strRes)
 myfile.write("\n")
 myfile.write("\n")
