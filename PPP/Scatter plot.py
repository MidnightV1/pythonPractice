import xlrd
from matplotlib import pyplot as plt

#获取数据
workbook = xlrd.open_workbook(r"C:\Users\John\Desktop\testcase.xlsx")
worksheet = workbook.sheet_by_index(0)

x = worksheet.col_values(0, 1)
y = worksheet.col_values(1, 1)

print(x)
print(y)

#绘制散点图
plt.scatter(x, y)

plt.title("test")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
