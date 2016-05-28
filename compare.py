import json
from bs4 import BeautifulSoup
senderreceiver=[]
per=[]
files = ['app1.json','app2.json','app3.json','app4.json','app5.json','app6.json','app7.json','app8.json','app9.json','app10.json',
	'app11.json','app12.json','app13.json','app14.json','app15.json','app16.json','app17.json','app18.json','app19.json','app20.json']
xmlfiles = ['AirDroid.xml','app-debug.xml','app-debug2.xml','Battery HD.xml','Battery Doctor (Battery Saver).xml','com_lightbox_android_camera_2.xml','Compass for Android.xml','CycleDroid.xml','de_k3b_android_androFotoFinder_12.xml','Do Not Crash.xml','Drawing Desk.xml','Easy Screenshot -no ad capture.xml','English Offline Dictionary.xml','Equalizer & Bass Booster.xml','Evernote.xml','fr_mobdev_goblim_2.xml','Google Calendar.xml','Islamic Prayer Times & Qibla.xml','Percentage Calculator v1.xml','Quick Memo.xml']

for f in range(len(files)):
	for k in range(f+1,4,1):
		app1 = json.loads(open(files[f]).read())
		app2 = json.loads(open(files[k]).read())
		act=[]
		intents=[]
		flag1 = False
	

		for i in range(len(app1["Intents"])):
			intents.append(app1["Intents"][i])
			x=intents[i]
			if(x):
				intents[i]=x.replace("\"","")
				for j in range(len(app2["Actions"])):
					act.append(app2["Actions"][j])
					if(intents[i] == act[j]):
						flag1=True
						senderreceiver.append([app1["sender"][i],app2["Components Name"][j]])
				

	
for p in range(len(xmlfiles)):
	soup = BeautifulSoup(open(xmlfiles[p]),"xml")
	name = soup.application.apkFile.next_sibling.next_sibling.contents[0]
	for ele in soup.usesPermissions.find_all('permission'):
		per.append([name,ele.string])

data={
'interacting Components':senderreceiver,
'Permissions':per
}

json_str = json.dumps(data)
f= open('compared.json',"w")
f.write(json_str) 

f.close()
