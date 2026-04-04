"""
3、jieba库的分词原理是利用一个中文词库，将待分词的内容与分词词库进行比对，
通过图结构和动态规划方法找到最大概率的词组。除了分词jieba还提供增加自定义中文单词的功能。
4、iieba库支持三种分词模式:
精确模式: 将句子最精确地切开，适合文本分析;
全模式: 把句子中所有可以成词的词语都扫描出来，速度非常快，但是不能解决歧义;
搜索引擎模式: 在精确模式基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
"""
# 精确模式：
# 1、jieba.lcut(s)是最常用的中文分词函数，用于精准模式，即将字符串分割成等量的中文词组，返回结果是列表类型
import jieba
ls = jieba.lcut("全国计算机等级考试python科目刘伟大")
print(ls)

# 全模式
# 2、jieba.lcut(s, cut_al = True)用于全模式，即将字符串的所有分词可能均列出来，返回结果是列表类型，冗余性最大。
import jieba
ls = jieba.lcut("全国计算机等级考试python科目刘伟大", cut_all = True)
print(ls)

# 搜索引擎模式
# 3、jieba.lcut for search(s)返回搜索引擎模式，该模式首先执行精确模式，然后再对其中长词进一步切分获得最终结果。
import jieba
ls = jieba.lcut_for_search("全国计算机等级考试python科目刘伟大")
print(ls)

# 向jieba词库增加新的单词。
# 4、jieba.add word()函数，顾名思义，用来向jieba词库增加新的单词。
import jieba
jieba.add_word("奥里给")
ls = jieba.lcut("全国计算机等级考试python科目刘伟大奥里给")
print(ls)