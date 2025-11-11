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
