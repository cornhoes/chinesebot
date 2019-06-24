

nameresponse = input("你叫什么名字？ ")

#punctionation testing

nameresponse = nameresponse.replace("!",(""))
nameresponse = nameresponse.replace("！",(""))
nameresponse = nameresponse.replace(",",(""))
nameresponse = nameresponse.replace("，",(""))
nameresponse = nameresponse.replace("?",(""))
nameresponse = nameresponse.replace("？",(""))
nameresponse = nameresponse.replace(".",(""))
nameresponse = nameresponse.replace("。",(""))


 #end punctuation testing

if "叫" in nameresponse:
	name = nameresponse.split("叫")[1]
elif "是" in nameresponse:
	name = nameresponse.split("是")[1]
else:
	name = nameresponse
print(name + "，你好。你有很漂亮的名字！我叫麦伊茹。我很高心认识你。")
