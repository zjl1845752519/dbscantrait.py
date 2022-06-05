class student(object):
    def __init__(self,name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel
    def __str__(self):
        return f'{self.name},{self.gender},{self.tel}'

# class studentManager(object):
#     def __init__(self):
#         self.student_list = []
# aa = student('aa','nv', 111)
# # print(aa)