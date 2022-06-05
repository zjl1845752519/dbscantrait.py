from student import *
class StudentManager(object):
    def __init__(self):
        self.student_list = [] #存储数据所用的列表
        #程序入口函数，启动程序后执行的函数
    def run(self):
        self.load_student()
        while True:
            self.show_menu()

            menu_num = int(input('请输入您需要的功能序号：'))
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()

            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()

            elif menu_num == 7:
                break

    @staticmethod
    def show_menu():
        print('请选择功能序号：')
        print('1.添加学员')
        print('2.删除学院')
        print('3.修改学员')
        print('4.查询学员')
        print('5.显示所有学员')
        print('6.保存学员信息')
        print('7.退出系统')
    def add_student(self):
        name = input('请输入你的姓名：')
        gender = input('请输入你的性别：')
        tel = input('请输入你的手机号：')
        student = Student(name, gender, tel)

        self.student_list.append(student)
        print(self.student_list)
        print(student)

    def del_student(self):
        del_name = input('请输入需要删除的学生姓名：')
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                break
        else:
            print('查无此人')
        print(self.student_list)

    def modify_student(self):
        modify_name = input('请输入需要修改的学员姓名：')
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('姓名')
                i.gender = input('性别')
                i.tel = input('电话')
                print(f'修改学员信息成功')
                break
        else:
            print('查无此人')

    def search_student(self):
        search_name = input('请输入您要搜索的学员姓名：')
        for i in self.student_list:
            if search_name == i.name:
                print(f'姓名是{i.name},性别是{i.gender},电话号码是{i.tel}')
                break
        else:
            print('查无此人')

    def show_student(self):
        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    def save_student(self):
        f = open('student.data','w')
        new_list = [i.__dict__ for i in self.student_list]
        f.write(str(new_list))
        f.close()

    def load_student(self):
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'],i['gender'], i['tel']) for i in new_list]
        finally:
            f.close()


