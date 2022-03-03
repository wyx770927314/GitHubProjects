import numpy as np

# 冒泡排序
# def list_sort(sorted_list):
#     for i in range(0, len(sorted_list)):
#         for j in range(0, len(sorted_list) - 1 - i):
#             if sorted_list[j] > sorted_list[j + 1]:
#                 temp = sorted_list[j]
#                 sorted_list[j] = sorted_list[j+1]
#                 sorted_list[j+1] = temp
#     return sorted_list


# numpy中ndarray的简单使用
# def array_jieshao():
#     # 一维数组
#     a = np.array([1, 2, 3, 4])
#     # 多维数组
#     b = np.array([[4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 16]])
#     print(a.shape)  # 打印一维数组
#     print(b.shape)  # 打印多维数组
#     print(a.dtype)  # 打印a里面的数据类型
#     print(b.dtype)  # 打印b里面的数据类型
#     print(a.size, b.size)  # 打印a和b的长度
#     print(b)  # 打印b
#     b[3, 2] = 15  # 修改多维数组b中的某个值
#     print(b)  # 再次打印b


#结构化数组
def array_jiegouhua():
    student_array_type = np.dtype({'names':['name','age','chinese','math','english'],'formats':['S32','i','i','i','f']})
    student_array = np.array([(),(),(),()])
if __name__ == '__main__':
    # array_jieshao()
    pass
