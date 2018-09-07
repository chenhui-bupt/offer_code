"""
输入:
输入数据包含两行，
第一行，上述格式的语义模板表达式
第二行，用户的自然语言指令（即：用户query）
输出:
当前query是否匹配当前语义模板表达式。匹配，则输出1，否则输出0.
输入范例:
<[播]放|来>[一|几]<首|曲|个>@{singer}的<歌[曲]|[流行]音乐>
来几首@{singer}的流行歌曲
输出范例:
0
"""

pattern = input()
query = input()

cnt = 0
cnt2 = 0
flag = 0
for ch in query:
    if ch in pattern:
        cnt += 1
    if ch == '<' or ch == '>':
        cnt2 += 1
    else:
        cnt2 -= 1
flag = 1
if len(pattern) < 0:
    print("pattern error")
else:
    flag = 1
print(flag)
