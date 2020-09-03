# -*- coding = utf-8 -*-
# @time:2020/9/2 9:25
# Author:唐成
# @File:词云.py
# @Software:PyCharm

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
data=pd.read_csv("E:\\爬虫\\爬虫终版\\result.csv",header=0,engine='python')
# content=pd.read_csv(open("E:\\爬虫\\爬虫终版\\result.csv",header=1))
print(data.head())
# print(data.tail())

content=data["内容"].agg(sum)
# print("\n",content)

content.replace(' ','')
content.replace('\n', '').replace('\r', '')
print('\n',type(content))
print(content)

import jieba
import jieba.analyse as ana
import nltk

dict="E:/project/usedict/投资理财.txt"
jieba.load_userdict(dict)
ana.set_stop_words('E:/project/stopwords-master/stopwords-master/stop.txt')
jieba.lcut(content)
#ana.set_idf_path 自定义idf路径
s=ana.extract_tags(content,topK=20) #使用更多
# split=ana.textrank(content,topK=20,
#                    withWeight=True, #返回权重
#                    allowPOS=('ns','n','vn','v')#选择词性
#                        ) #整句分割，语义关系
s=[w for w in s if len(w)>1] #if w not in stoplist
text=' '.join(s) #nltk只能识别空格作为词条分割方式
print(text)

#fdist=nltk.FreqDist(text)

# tmpdf=pd.read_csv('E:/project/stopwords-master/stopwords-master/stop.txt',names=['w'],encoding='utf-8')
# [w for w in jieba.cut if w not in list(tmpdf.w)]

#wordcloud需要用空格/标点符号分割单词，否则不能正确分词
##基于文本的分词
import wordcloud
from imageio import imread
myfont='C:/Windows/Fonts/simhei.ttf'
cloudobj=wordcloud.WordCloud(font_path=myfont,
                             width=360,
                             height=180,
                             mask=imread('E:/project/图片/草莓.png'),
                             mode='RGBA',
                             background_color=None).generate(text)
imgarray=np.array(imread('E:/project/图片/草莓.png'))
bimgcolors=wordcloud.ImageColorGenerator(imgarray)
cloudobj.recolor(color_func=bimgcolors)
import matplotlib.pyplot as plt
plt.imshow(cloudobj)
plt.axis('off')
plt.show()


