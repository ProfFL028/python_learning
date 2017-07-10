import itchat
# 登陆
itchat.login()
# 获取所有friends
friends = itchat.get_friends(update=True)[0:]

male = female = other = 0
#friends[0] 存储自已的信息
for i in friends[1:] :
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
#计算朋友总数
total = len(friends[1:])

print ("男性%d, 女性%d, 未知%d" % (male, female, other))

# 获取变量信息
def get_var(var): 
    variable = []
    for i in friends: 
        value = i[var]
        variable.append(value)
    return variable

NickName = get_var("NickName")
Sex = get_var("Sex")
Province = get_var("Province")
City = get_var("City")
Signature = get_var("Signature")
from pandas import DataFrame
data = {'NickName': NickName, 'Sex': Sex, 'Province': Province, 'City': City, 'Signature': Signature}
frame = DataFrame(data)
frame.to_csv('data.csv', index=True)

#将所有的签名拼接在一起
import re 
siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)

#分词
import jieba
wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)

# word cloud generator
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

coloring = np.array(Image.open("yellow.jpg"))
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=coloring,max_font_size=60, 
    random_state=42, scale=2, font_path="simhei.ttf").generate(word_space_split)
image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()