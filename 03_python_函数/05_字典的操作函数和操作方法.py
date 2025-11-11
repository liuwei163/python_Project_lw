# 操作函数                    描述
# len(d)                    字典d的元素个数(长度)
# min(d)                    字典d中键的最小值(键之间具有可比性)
# max(d)                    字典d中键的最大值(键之间具有可比性)
# dict()                    生成一个空字典

d = {2: "刘伟", 10: "张三"}
print(len(d))  # 一个键值对为一个元素
print(min(d))
print(max(d))

lw = dict()
print(lw)

############################################################################################
"""
# 字典类型存在一些操作方法，使用语法为：
# <字典变量>.<方法名称>(<方法参数>)

操作方法                        描述
d.keys()                        返回所有的键信息
d.values()                      返回所有的值信息
d.items()                       返回所有的键值对
d.get(key, default)             键存在则返回相应值，否则返回默认值
d.pop(key, default)             键存在则返回相应值，同时删除键值对，否则返回默认值
d.popitem()                     随机从字典中取出一个键值对，以元组(key,value)形式返回
d.clear()                       删除所有的键值对
"""
d = {2: "刘伟", 10: "张三"}
print(d.keys())    # dict_keys([2, 10])
print(d.values())  # dict_values(['刘伟', '张三'])
print(d.items())   # dict_items([(2, '刘伟'), (10, '张三')])

d = {"name": "刘伟", "age": "20"}
print(d.get("name"))
print(d.get("sex"))  # 找不到返回空None
print(d.get("sex", "男"))  # 当查找内容为空时，给一个默认值 男

d = {"name": "刘伟", "age": "20"}
print(d.pop("name"))   # 删除name键值对并打印删除的值
print(d)
print(d.pop("sex", "女"))  # 当查找内容为空时，给一个默认值 女 （不做删除操作）

d = {"name": "刘伟", "age": "20", "sex": "男"}
print(d.popitem())

print(d.clear())  # 清空字典
print(d)
