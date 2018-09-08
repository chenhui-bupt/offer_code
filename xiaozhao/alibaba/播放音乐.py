"""
输入:
输入数据包含两行，
第一行，实体列表，多种实体之间用分号隔开，实体名和实体值之间用下划线隔开，多个实体值之间用竖线隔开，所有标点都是英文状态下的，格式如下：
实体名称1_实体值1|实体值2|…;实体名称2_实体值1|实体值2|…;…
第二行，用户的自然语言指令
输出:
被标记了关键词的指令。指令中的关键词前后加一个空格被单独分出来，并在后面跟上"/"+实体名称来标记。如果一个实体值属于多个实体，将这些实体都标记出来，并按照实体名称的字符串顺序正序排列，并以逗号分隔。
输入范例:
singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪
请播放周杰伦的七里香给我听
输出范例:
请播放 周杰伦/actor,singer 的 七里香/song 给我听
"""

entities = input().split(';')
query = input()
dct = {}
for entity in entities:
    key, value = entity.split('_')
    dct[key] = value.split('|')
print(dct)
print(query)

def MaximumForwardMatching(s1, dictionary):
    s2 = ""
    begin = 0
    end = len(s1)
    attributes = {'singleDictWord': 0, 'nonDictWord': 0, "numOfWords": 0}
    while begin != end:
        while end - begin > 1 and s1[begin: end] not in dictionary:
            end -= 1
        if end-begin == 1:
            if s1[begin: end] in dictionary:
                attributes['singleDictWord'] += 1
            else:
                attributes['nonDictWord'] += 1
        attributes['numOfWords'] += 1
        s2 = s2 + s1[begin: end] + "/"
        begin = end
        end = len(s1)
    print(s2)
    return s2, attributes

def helper(s1, key):
    s2 = ""
    begin = 0
    end = len(s1)
    while begin != end:
        while end - begin > 1 and s1[begin: end] not in dct[key]:
            end -= 1
        if s1[begin: end] in dct[key]:
            s2 += ' ' + s1[begin: end] + '/%s ' % key
        else:
            s2 = s2 + s1[begin: end]
        begin = end
        end = len(s1)
    return s2

for key in dct:
    query = helper(query, key)
    print(query)

# query = list(query)
i = 0
while i < len(query):
    if i > 0 and query[i] == '/' and query[i-1] == ' ':
        query = query[:i-1] + ',' + query[i+1:]
        i -= 1
    i += 1
i = 0
while i < len(query):
    if query[i] == ' ':
        j = i + 1
        while j < len(query) and query[j] == ' ':
            j += 1
        query = query[:i+1] + query[j:]
        i = j
    i += 1

print(query)
