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

#not sold on branch below, might introduce game .. input(name + “, 你想玩游戏吗？ ")

condition = input("你是不是电脑？ ")
if "不" in condition:
	input("你是什么东西? ")
else:
	input("我也是电脑！你是什么    的电脑? ")
