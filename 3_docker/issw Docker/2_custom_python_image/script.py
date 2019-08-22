#---------------------------------------------------------------
# 
# Export data as a JSON-file from a PFC which is connected to the WAGO Cloud
# 
#---------------------------------------------------------------
import json
import requests
#---------------------------------------------------------------
# --------------------------Start-------------------------------
# Change entries according to your WAGO Cloud subscription
# 
#---------------------------------------------------------------
myWagoCloudPassword='Wagowago1%'
myWagoCloudEmail = 'alexander.fugmann@wago.com'
myDeviceId= "c3006a0a-c218-4a65-b30c-ea1d5d2188ac"
myTagKey = "temperature"
myGroupKey = "1"
myStartDate = "2019-05-29T08:00:00.000Z"
MyStopDate =  "2019-06-05T19:00:00.000Z"
# 
#---------------------------------------------------------------
# --------------------------END---------------------------------
#---------------------------------------------------------------
# 
# Code to get login data to WAGO Cloud

sURL_login = 'https://cloud.wago.com/api/token' 							# send post to this url 
sHEAD_login = {"Content-type": "application/x-www-form-urlencoded"} 		# set content type of post   

payload = 'grant_type=password&username='+myWagoCloudEmail+'&password='+myWagoCloudPassword # create string which will be send to post url 
ret = requests.post(sURL_login,headers=sHEAD_login,data= payload) # send post
print("Login Code:",ret.status_code)	#print result code  if Login code = 200 , then the login was successful
json_login_data = ret.text				# parse response data to a JSON object
obj_json_login_data = json.loads(json_login_data)

# Code to create a http post to 'https://cloud.wago.com/API/v2/historicalData' with credentials 

sAccess_token = obj_json_login_data["access_token"] #extract the access token from "obj_json_login_data"
sTokenType = obj_json_login_data["token_type"] #extract the token type from "obj_json_login_data"
sHeaderEntry = {'Authorization': sTokenType+" "+sAccess_token,'Content-Type':'application/json'}
sURL_data_from_device_history = 'https://cloud.wago.com/API/v2/historicalData'

# build JSON object according to WAGO Cloud REST API Documentation
myTestDevice = {
  "from": myStartDate,
  "to": MyStopDate,
  "tags":[
            {
            "groupKey": myGroupKey,
            "deviceId": myDeviceId,
            "tagKey": myTagKey
            }
        ]
}

# post "myTestDevice" JSON to "sURL_data_from_device_history" with credentials from above
json_payload_get_data_from_device_history = json.dumps(myTestDevice)
ret_link_data_export_d_h = requests.post(sURL_data_from_device_history,
                           headers=sHeaderEntry,
                           data= json_payload_get_data_from_device_history)

print("Export  File Code: ",ret_link_data_export_d_h.status_code)
print("Export  File Response: ",ret_link_data_export_d_h.text)