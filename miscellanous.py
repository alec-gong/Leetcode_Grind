def cutTheSticks(arr):
    
    arr.sort(reverse = True)
    res = []
    
    while arr:
        res.append(len(arr))
        for i in range(len(arr)):
            arr[i] -= arr[-1]
        while arr and arr[-1] == 0:
            arr.pop()
    return res


def wordOrder():
    import sys

    input_words = sys.stdin.read()
    lines = input_words.splitlines()

    dic, ans = {}, []
    for i in range(1, len(lines)):
        dic[lines[i]] = dic.get(lines[i], 0) + 1
    for key in dic:
        ans.append(dic[key])
    l = " ".join(str(a) for a in ans)
    print(len(dic))
    print(l)
