from CalThread import *
class Operation(object):
    # 文件路径
    file_path = ''
    # 分隔符
    split_character = ''
    # 列名
    list_name = []
    # 数据
    data_dic = {}
    # 唯一标识位置
    sign_index = 0
    # 条件字典
    condition_dic = {}
    # 返回值字典
    res_dic = {}
    # 需要的数据的列名
    need = []
    # 需要排除的数据
    exclude = []
    # 行数限制
    line_limt = 0
    def __init__(self):
        self.file_path = ''
        self.split_character = ''
        self.list_name = []
        self.data_dic = {}
        self.sign_index = 0
        self.condition_dic = {}
        self.res_dic = {}
        self.need = []
        self.exclude = []
        self.line_limt = 10000
    '''
   设置文件路径和各文件内分割符号 
    '''
    def setFilePath(self, file_path, split_character):
        self.file_path = file_path
        self.split_character = split_character
        return True
    '''
    初始化列名
    并且获取文件内数据
    '''
    def setListName(self):
        file = open(self.file_path, "r", encoding='UTF-8')
        self.list_name = file.readline().strip().split(self.split_character)
        temp_date_limt = 0
        temp_date_name = 0
        self.data_dic[temp_date_name] = []
        for line in file.readlines():
            temp_date_limt += 1
            self.data_dic[temp_date_name].append(line.strip())
            if temp_date_limt == self.line_limt:
                temp_date_limt = 0
                temp_date_name += 1
                self.data_dic[temp_date_name] = []
        file.close()
        return True
    '''
    设置唯一标识在列名中的位置
    '''
    def setSgin(self, sgin):
        self.sign_index = self.list_name.index(sgin)
        return True
    '''
    设置条件
    '''
    def setCondition(self, condition_dic):
        self.condition_dic = condition_dic
        return True
    '''
    添加条件
    '''
    def addCondition(self, condition_list_name, condition):
        if self.condition_dic.get(condition_list_name, None) != None:
            self.condition_dic[condition_list_name].append(condition)
        else:
            self.condition_dic[condition_list_name] = [condition]
        return True
    '''
    设置需要的结果
    与需要排除的数据
    '''
    def setNeed(self, need, exclude):
        self.need = need
        self.exclude = exclude
    '''
    设置行数限制
    即多少行开启一个线程
    默认每10000行开启一个新线程
    '''
    def setLineLimt(self, line_limt):
        self.line_limt = line_limt
    '''
    根据条件获取结果
    '''
    def getRes(self):
        thread_dic = {}
        thread_temp = 0
        for data in self.data_dic:
            thread_dic[thread_temp] = CalThread(thread_temp, self.data_dic[data], self.condition_dic, self.need, self.split_character, self.list_name, self.sign_index, self.exclude)
            thread_dic[thread_temp].start()
            thread_temp += 1
        flag = len(thread_dic)
        while flag:
            need_pop = []
            for key in thread_dic:
                if thread_dic[key].exit_flag:
                    flag -= 1
                    need_pop.append(key)
            for pop_key in need_pop:
                self.res_dic.update(thread_dic[pop_key].res)
                thread_dic.pop(pop_key)

        return self.res_dic