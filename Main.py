from Operation import *

# 1. 新建实体类
obj = Operation()
# 2. 设置txt文件路径与分割符
obj.setFilePath("data.txt", " ")
# 3.设置多少行文本开启一个线程, 默认10000行开启一个新线程
obj.setLineLimt(10000)
# 4. 读取text第一行获得列名，同时按照line_limt限制将余下内容创建成多个list
obj.setListName()
print(obj.list_name)
#5. 设置唯一标识行
obj.setSgin("测试1")
#6. 设置条件，要求传入一个字典。
obj.setCondition({"测试2": [["11", "22"], ["33", "44", "55"],["66"],["77"]],
                  "测试3": [["111"], ["222"]] })
#7. 设置需要的列名和需要排除的数据
obj.setNeed(["测试4","测试5"], ['0'])
#8. 获取结果
dic = obj.getRes()
print(dic)