nameresponse = input("你叫什么名字？ ")

if "叫" in nameresponse:
	name = nameresponse.split("叫")[1]
elif "是" in nameresponse:
	name = nameresponse.split("是")[1]
else:
	name = nameresponse
print(name + "，你好。你有很漂亮的名字！我叫麦伊茹。我很高心认识你。")
	
ageresponse = input(name +"， 你多大？")

if "岁" in ageresponse:
	age = ageresponse.split("岁")[0]
	if "我" in age:
		age = age.split("我")[1]
elif "有" in ageresponse:
	age = ageresponse.split("有")[1]
	if "年" in age:
		age = age.split("年")[0]
else:
	age = ageresponse
print("你" + age + "岁.")

correct = input("对不对？ ")
while correct != "对":
	ageresponse = input(name +"， 你多大？")

	if "岁" in ageresponse:
		age = ageresponse.split("岁")[0]
		if "我" in age:
			age = age.split("我")[1]
	elif "有" in ageresponse:
		age = ageresponse.split("有")[1]
		if "年" in age:
			age = age.split("年")[0]
	else:
		age = ageresponse
	print("你" + age + "岁.")
	correct = input("对不对？ ")
print("好啊。")

#offer game or convo, rps or sports, politics, climate change, tourism, religion

path = input(name + ", 你想玩游戏吗? ")
if "不" in path:
	home = input("好啊。我们可以聊天儿！你是从哪里来的？ ")

	if "中国" in home:
		print("真的假的！我的家也在中国🇨🇳 🇨🇳 🥰")

	elif "美国" in home:
		ny = input("真的吗？🇺🇸 🇺🇸 🌈 美国很漂亮！你去到纽约吗？ ")
		if "没" in ny:
			print("end")
		else: 
			print("end")

	elif "日本" in home:
		print("🇯🇵")

	elif "西班牙" in home:
		print("🇪🇸")

	elif "罗马尼亚" in home:
		print("🇷🇴 🇷🇴 🇷🇴 🇷🇴 🇷🇴 🇷🇴 🇷🇴 🥰 🥰 🥰 🥰 ✨ ✨ ✨")

	elif "法国" in home:
		print("不好 👎 🇫🇷 💩")

	else:
		print("我想去哪儿路行！ ")


else:
	import random
	print("石 (shi)...")
	print("纸 (zhi).....")
	print("刀 (dao).......")

	players = input("单人还是多人？ ").lower()
	print("")
	if (players == "一个" or players == "一个人" or players == "1" or players == "单人"):

		player1 = input("对手，做你的举动吧：").lower()
		rand_num = random.randint(0,2)
		if rand_num == 0:
			player2 = "石"
		elif rand_num == 1:
			player2 = "纸"
		else:
			player2 = "刀"

		print(f"电脑选择了：{player2}")

		if ((player1 == "石" and player2 == "刀") or (player1 == "纸" and player2 == "石") or (player1 == "刀" and player2 == "纸")):
			print("✧･ﾟ: *✧･ﾟ:*  你赢了！ *:･ﾟ✧*:･ﾟ✧")

		elif ((player2 == "石" and player1 == "刀") or (player2 == "纸" and player1 == "石") or (player2 == "刀" and player1 == "纸")):
			print("")
			print("      . ⋆ ˚｡⋆୨୧˚ 电脑赢了！˚୨୧⋆｡˚ ⋆ .")
			print("")

		elif player1 == player2:
			print("有一个平局!")
		else:
			print("Invalid input. Please try again.")
         

	elif players == "multi" or players == "多人" or players == "多" or players == "2" or players == "两个人" or players == "两个":

		player1 = input("球员1, 做你的举动吧: ").lower()
		#while player1 != ("石" or "纸" or "刀"):
		#	player1 = input("我不懂。 你写了什么? 石，纸，还是 刀？ ")
		#print("好啊。")

		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")		
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")		
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")		
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")		
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")
		print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ 别作弊! ｡･:*:･ﾟ★,｡･:*:･ﾟ☆")



		player2 = input("球员2, 做你的举动吧: ").lower()

		if ((player1 == "石" and player2 == "刀") or (player1 == "纸" and player2 == "石") or (player1 == "刀" and player2 == "纸")):
			print("球员1赢了!")

		elif ((player2 == "石" and player1 == "刀") or (player2 == "纸" and player1 == "石") or (player2 == "刀" and player1 == "纸")):
			print("球员2赢了!")

		elif player1 == player2:
			print("有一个平局!")

		else:
			
			print("我不懂。 你写了什么？ ")
	else:
			print("我不懂。 你写了什么？ ")







		#home = input("对不起, 我不意识。你家在那个国家？ ")


		#do you like sports? which sport? watch or play? my favorite sport is___.  i like ___ player in each sport. else: i don't know/like that sport, which others do you like?
		#are you from china? 
		#where do you like to travel? have you been to beijing? have you been to ___? talk about sites
		#climate change: paris accords, india coal responsilitty, beijing pollution

