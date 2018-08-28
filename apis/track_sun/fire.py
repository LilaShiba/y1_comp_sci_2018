import bs4, requests, json, urllib.parse
# https://www.lmsal.com/hek/api.html

# get user values
start_time= input("what is the start date: yyyy-mm-dd ?")
end_time= input("what is the end date: yyyy-mm-dd ?")
#get json data
res = requests.get("http://www.lmsal.com/hek/her?cosec=2&cmd=search&type=column&event_type=fl,fe,er,fi,cw,lp,ss,cj,sp,pt,ar,cr,bu,ee&event_starttime="+start_time+"T00:00:00&event_endtime="+end_time+"T00:00:00&temporalmode=strict&event_coordsys=helioprojective&x1=-1200&x2=1200&y1=-1200&y2=1200")
res.raise_for_status()
print(res.text[:500])
#parse json data
parsed_json = res.json()