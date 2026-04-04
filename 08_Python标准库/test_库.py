import jieba
jieba.add_word("奥里给")
ls = jieba.lcut("全国计算机等级考试python科目刘伟大奥里给")
print(ls)