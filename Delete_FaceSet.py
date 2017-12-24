# POST https://api-us.faceplusplus.com/facepp/v3/faceset/delete

import requests
import datetime
import FacePPAuth
import os
import json

URL = "https://api-us.faceplusplus.com/facepp/v3/faceset/delete?"
API_KEY = "api_key=" + FacePPAuth.api_key
API_SECRET = "api_secret=" + FacePPAuth.api_secret
#OUTER_ID = "outer_id=oid1"
FACESET_TOKEN = "faceset_token=c1c496b37dae174d0bd6ab4dd00bc1d2"

print("================== DELETING FACE SET DETAIL =======================\n")
res = requests.post(URL + API_KEY + "&" + API_SECRET + "&" + FACESET_TOKEN )


print("================== RES OF FACESET DELETE =======================\n")
strRes = res.content.decode('utf-8')
print(strRes)
cwd = os.getcwd()
with open(cwd + "/Res_DeleteFaceSet.txt", "a") as myfile:
 curTime  = str(datetime.datetime.now())
 myfile.write("========================= "+ curTime +" ============================ \n")
 myfile.write(strRes)
 myfile.write("\n")
 myfile.write("\n")
