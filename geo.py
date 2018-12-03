import requests
import getip
import ast
import sys

url = "https://iplocation.com"

print("=== Welcome to ip_info ===")
url = "https://iplocation.com"
if len(sys.argv) != 1:
    request = requests.post(url,data={'ip':sys.argv[1]})
    info = ast.literal_eval(request.text)
    print("[+]ip : "+str(info['ip']))
    print("[+]Your city : "+str(info['city']))
    print("[+]Your region : "+str(info['region_name']))
    print("[+]Your country : "+str(info['country_name']))
    print("[+]Time zone : "+str(info['time_zone']))
    print("[+]Your latitude and longitude  : "+str(info['lat'])+","+str(info['lng']))
else:
    request = requests.post(url,data={'ip':getip.get()})
    info = ast.literal_eval(request.text)
    print("[+]Your ip : "+str(info['ip']))
    print("[+]Your city : "+str(info['city']))
    print("[+]Your region : "+str(info['region_name']))
    print("[+]Your country : "+str(info['country_name']))
    print("[+]Time zone : "+str(info['time_zone']))
    print("[+]Your latitude and longitude  : "+str(info['lat'])+","+str(info['lng']))