import json
with open('imdbdata.json') as json_data:
	jsonData=json.load(json_data)
	while(True):
		print("Enter 1 for movie comparision")
		print("Enter 2 for movie Details")
		print("Enter 3 for searching movie by genre")
		print("Enter 4 to exit")
		ch=int(input())
		if ch==1:
			print("enter 2 movie names with initials in capital and with commas")
			x=0.0
			y=0.0
			t=[i for i in input().split(',')]
			a=t[0]
			b=t[1]
			print(a)
			print(b)
			for i in jsonData:
				if i["name"]==a:
					x=i["rating"]
					break
			for j in jsonData:
				if j["name"]==b:
					y=j["rating"]
					break
			if x>y:
				print(a,"is a better movie")
			elif x<y:
				print(b,"is a better movie")
			else:
				print("Both are equally good")
		elif ch==2:
			print("Enter the movie name")
			a=input()
			for i in jsonData:
				if i["name"]==a:
					print("year :",i["year"])
					print("Ratings :",i["rating"])
					print("description :",i["description"])
					print("length :",i["runtime"])
					print("Genre :",i["genre"])
		elif ch==3:
			print("Enter a genre with capital initials")
			a=input()
			new={}
			a_list_of_dicts=[]
			print("Movies with this genre are :")
			for i in jsonData:
				g=[x for x in i["genre"].split(',')]
				for q in g:
					q=q.strip()
					if q==a:
						print(i["name"])
						print(i["year"])
						print(i["rating"])
		elif ch==4:
			break
