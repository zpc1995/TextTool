import threading

class CalThread (threading.Thread):
    data = []
    condition = {}
    need = []
    res = {}
    split_character = ''
    list_name = []
    sign_index = 0
    exclude = []
    exit_flag = False
    def __init__(self, threadID, data, condition, need, split_character, list_name, sign_index, exclude):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.data = data
        self.condition = condition
        self.need = need
        self.split_character = split_character
        self.list_name =list_name
        self.sign_index = sign_index
        self.exclude = exclude
        self.exit_flag = False
        self.res = {}
    def run(self):
        self.cal()
        return True
    def cal(self):
        for str in self.data:
            temp_list = str.split(self.split_character)
            if self.res.get(temp_list[self.sign_index], None) == None:
                self.res[temp_list[self.sign_index]] = {}
            temp = self.res[temp_list[self.sign_index]]
            for temp_condition in self.condition:
                for temp_condition_son in self.condition[temp_condition]:
                    flag = False
                    for temp_condition_son_son in temp_condition_son:
                        if temp_list[self.list_name.index(temp_condition)] == temp_condition_son_son:
                            if temp.get(self.condition[temp_condition][self.condition[temp_condition].index(temp_condition_son)][0], None) == None:
                                temp[self.condition[temp_condition][self.condition[temp_condition].index(temp_condition_son)][0]] = {}
                            temp = temp[self.condition[temp_condition][self.condition[temp_condition].index(temp_condition_son)][0]]
                            flag = True
                            break
                    if flag :
                        break;
            for temp_need in self.need:
                flag = False
                for exclude in self.exclude:
                    if temp_list[self.list_name.index(temp_need)] == exclude:
                        flag = True
                if flag:
                    continue
                if temp.get(temp_need, None) == None:
                    temp[temp_need] = []
                temp[temp_need].append(float(temp_list[self.list_name.index(temp_need)]))
        self.exit_flag = True;
        return True


