#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 21:14:17 2018

@author: madawei1
"""
#https://blog.csdn.net/Eastmount/article/details/50323063

from sklearn.feature_extraction.text import CountVectorizer
 
#语料
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]
#将文本中的词语转换为词频矩阵
vectorizer = CountVectorizer()
#计算个词语出现的次数
X = vectorizer.fit_transform(corpus)
#获取词袋中所有文本关键词
word = vectorizer.get_feature_names()
print(word)#查看词频结果
print(X.toarray())

from sklearn.feature_extraction.text import TfidfTransformer
 
#类调用
transformer = TfidfTransformer()
print(transformer)
#将词频矩阵X统计成TF-IDF值
tfidf = transformer.fit_transform(X)
#查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重
print(tfidf.toarray())




import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
 
if __name__ == "__main__":
    corpus=["我 来到 北京 清华大学",#第一类文本切词后的结果，词之间以空格隔开
		"他 来到 了 网易 杭研 大厦",#第二类文本的切词结果
		"小明 硕士 毕业 与 中国 科学院",#第三类文本的切词结果
		"我 爱 北京 天安门"]#第四类文本的切词结果
    vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
    tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    word=vectorizer.get_feature_names()#获取词袋模型中的所有词语
    weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
        print(u"-------这里输出第",i,u"类文本的词语tf-idf权重------")
        for j in range(len(word)):
            print(word[j],weight[i][j])