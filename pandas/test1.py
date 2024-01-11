# import pandas as pd
#
# # 创建一个示例 DataFrame
# data = {
#     'Key': ['A', 'B', 'C', 'D', 'E'],
#     'Values': ['1\n2\nvalue13\n4', 'value1\n3\n5', '6\n7\n8', '9\nvalue1\n11', '12\n13\n14']
# }
#
# df = pd.DataFrame(data)
#
# # 定义要匹配的子串
# substring_to_match = 'value1'
#
# # 使用布尔索引过滤出满足条件的行
# filtered_df = df[df['Values'].str.contains(substring_to_match, regex=True)]
# filtered_df2 = df[df['Values'].str.contains(r'\b' + substring_to_match + r'\b', regex=True)]
#
#
# # 打印结果
# print(filtered_df[['Key', 'Values']])

import pandas as pd

# 创建一个示例 DataFrame
data = {
    'Key': ['a', 'b', 'c', 'd', 'e'],
    'Values': ['1', '2', '3', '4', '5']
}

df = pd.DataFrame(data)

# 将 'Key' 列设为索引
df.set_index('Key', inplace=True)

# 访问索引值为 'b' 的整行数据
row_b_data = df.loc['b']

# 打印结果
print(row_b_data)

