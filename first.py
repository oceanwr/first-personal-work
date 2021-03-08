# 提取网页源代码
import requests
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
           "authoration":"apicode","apicode":"15744099d0f8479d8a6ff1947d5dbbd6"}
comment=[]
comments=[]
source='1614258198921'

# 提取评论
import re
for i in range (0,1270):
    url='https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=0&' \
        'scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_='+source
    html=requests.get(url,headers=headers).content.decode()
    comment=re.findall('content":"(.*?)"',html,re.S)
    comments.append(comment)
    source=str(int(source)+1)

print(comments)

# 保存到json并用分词器分词
import thulac
thu1 = thulac.thulac(seg_only=True)
f = open("comments.json", "w", encoding='utf-8')
for list in comments:
    for comment in list:
        text=thu1.cut(comment,text=True)
        f.write(text)
        f.write('\n')
f.close()
