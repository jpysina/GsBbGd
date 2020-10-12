# -*- encoding: utf-8 -*-
"""
@File        :  pro.py
@Built Time  :  2020/10/11 01:13:08
@Author      :  jpysina 
@Contact     :  754927753@qq.com
"""

# here put the import lib

import pandas as pd
import pandas_profiling as pp
import numpy as np
import pyecharts
import jieba
import jieba.posseg as pseg
import collections
import re
from pyecharts.globals import _RenderType

from pyecharts.options.global_options import InitOpts

#%%
# 目标
cmt = pd.read_csv("GBible.csv", names="v", encoding="utf-8")
# 停用词
stopwords1 = pd.read_table(
    "Dict/stopwords/cn_stopwords.txt", sep="\n", names="v", encoding="utf-8"
)
stopwords2 = pd.read_table(
    "Dict/stopwords/scu_stopwords.txt", sep="\n", names="v", encoding="utf-8"
)
stopwords3 = pd.read_table(
    "Dict/stopwords/baidu_stopwords.txt", sep="\n", names="v", encoding="utf-8"
)
stopwords = pd.concat([stopwords1, stopwords2, stopwords3], axis=0)
# 预处理
cmt = cmt["v"].tolist()
stopwords = stopwords["v"].to_list()
# 自定义字典
jieba.load_userdict("Dict/dict/Offical/dictBig.txt")
#%%
# 分词处理
words_list = []
for i in cmt:
    # 正则选汉字
    i = "".join(re.findall("[\u4e00-\u9fa5]", i))
    # 分词
    h = jieba.lcut(i)
    for j in h:
        if j not in stopwords:
            words_list.append(j)
# 清理内存
# del stopwords, stopwords1, stopwords2, stopwords3
# del cmt
# %%
# 统计
word_counts = collections.Counter(words_list)
word_counts_top = word_counts.most_common(150)
# %%
# 渲染
from pyecharts import options as opts
from pyecharts.charts import WordCloud
c = (
    WordCloud(init_opts=opts.InitOpts(width='50%',height='800px',renderer = 'RenderType.SVG'))
    .add(
        "",
        word_counts_top,
        word_size_range=[15, 75],
        textstyle_opts=opts.TextStyleOpts(font_family="思源宋体 Heavy"),
        mask_image= 'img/god.png'
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="The Bible of ゲンシン"))
    
)
# %%
