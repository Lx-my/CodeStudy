import pandas as pd


def process_column_and_unstack(df, col_name):
    """
    对 DataFrame 的指定列进行处理，并取消堆叠
    """
    # 复制 DataFrame，以免影响原始数据
    df_copy = df.copy()

    # 将指定列中的换行符替换为逗号，并处理空值和开头的逗号
    df_copy[col_name] = df_copy[col_name].str.replace('\n', ',').str.strip(',').str.split(',')

    # 使用 apply(pd.Series) 将指定列的列表展开成多个列
    df_processed = df_copy[col_name].apply(pd.Series)

    # 将列名中的 NaN 值去除，将数据从宽格式变为长格式
    df_processed = df_processed.stack()

    # 将指定列的索引级别去除，并删除列名中的多余信息
    df_processed = df_processed.reset_index(level=-1, drop=True)

    # 重置索引，使其成为默认的整数索引
    df_processed = df_processed.reset_index()

    return df_processed


# 示例调用
df_original = pd.DataFrame({
    'C': ['ab\ncd\nef,', 'gh,ij,kl', 'mn\nop,qrs']
}, index=[1000, 1010, 2000])

# 传递整个 DataFrame，并指定处理的列为 'C'
result_df = process_column_and_unstack(df_original, 'C')

# 打印处理后的结果
print(result_df)
