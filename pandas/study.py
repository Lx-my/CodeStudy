import pandas as pd

# 创建一个示例 DataFrame
data = {
    'Key': ['A', 'B', 'C', 'D', 'E'],
    'Values': ['1\n2\nvalue1\n4', 'value1\n3\n5', '6\n7\n8', '9\nvalue1\n11', '12\n13\n14']
}

df = pd.DataFrame(data)

# 定义要匹配的子串
substring_to_match = 'value1'

# 使用布尔索引过滤出满足条件的行
filtered_df = df[df['Values'].str.contains(substring_to_match, regex=True)]

# 将 'Key' 列设为索引
filtered_df.set_index('Key', inplace=True)

# 定义复杂的条件，例如删除包含 '2' 的索引
complex_condition = filtered_df.index.str.contains('A')

# 删除满足条件的行（这里应该对原 DataFrame 进行操作）
df = df[~df['Key'].isin(filtered_df[complex_condition].index)]

# 打印结果
print(df)
