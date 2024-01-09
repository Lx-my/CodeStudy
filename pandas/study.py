
import pandas as pd

# 读取原始数据
# file_path = r"F:\WorkSpace\demo\CodeStudy\pandas\test.xlsx"
# df = pd.read_excel(file_path)

# 读取原始数据
df = pd.DataFrame({
    'id': [1000, 1010, 2000],
    'B': ['test1,test2', 'test1,test2', 'test1,test2,test3'],
    'C': ['a,b', 'c,d', 'e,f']
})

# 将逗号替换为换行符
df.replace({',': '\n'}, regex=True, inplace=True)

# 将换行符替换为逗号
df.replace({'\n': ','}, regex=True, inplace=True)
# 更换某行数据
df['B'] = df['B'].apply(lambda x: x.replace("\n", ","))
# inplace无须赋值，直接修改原始数据
df['B'].replace("\n", ",", inplace=True)


# 复制原始数据框
df_copy = df.copy()

# 将 "C" 列按逗号拆分并堆叠
df_copy['C'] = df_copy['C'].str.split(',')
df_copy = df_copy.set_index(['id', 'B'])['C'].apply(pd.Series).stack().reset_index(level=-1, drop=True).reset_index()

'''
# 将 "C" 列中的字符串按逗号拆分成列表
df_copy['C'] = df_copy['C'].str.split(',')

# 使用 set_index 将 "id" 列和 "B" 列作为索引
# 然后使用 apply(pd.Series) 将 "C" 列的列表展开成多个列
df_copy = df_copy.set_index(['id', 'B'])['C'].apply(pd.Series)

# 将列名中的 NaN 值去除，将数据从宽格式变为长格式
df_copy = df_copy.stack()

# 将 "B" 列的索引级别去除，并删除列名中的多余信息
df_copy = df_copy.reset_index(level=-1, drop=True)

# 重置索引，使其成为默认的整数索引
df_copy = df_copy.reset_index()
'''

# 重新命名列名
df_copy.columns = ['id', 'B', 'C']

# 获取所有唯一的 "test" 值
unique_tests = set(','.join(df['B']).split(','))

# 创建 ExcelWriter 对象，指定 Excel 文件名
with pd.ExcelWriter("out_put.xlsx") as writer:
    for test in unique_tests:
        # 创建临时数据框，避免修改原始数据框
        temp_df = df_copy.copy()

        # 将包含当前 "test" 的行的 "B" 列的值全部设为当前 "test"
        temp_df.loc[temp_df['B'].str.contains(test, na=False), 'B'] = test

        # 创建包含特定 "test" 值的子表
        sub_table = temp_df[temp_df['B'] == test]

        # 将子表保存至 Excel 文件，工作表名为 "test1", "test2", ...
        sub_table.to_excel(writer, sheet_name=f'test{test}', index=False)
