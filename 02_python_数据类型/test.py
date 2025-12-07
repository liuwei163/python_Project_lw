f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs1.txt", "w")
ls = str(["liuwei", 1, 3, "刘伟", "aaa"])
f.writelines(ls)
f.close()