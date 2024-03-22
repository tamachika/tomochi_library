def rle(s):
    n = len(s)
    if n == 0:
        return '', []
    ret = ['', []]
    c = s[0] #１文字目がどこまで続くか
    cnt = 0
    for i in range(n):
        if c == s[i]:
            cnt += 1
        else:
            ret[0] += c #１文字目の連続具合の記録
            ret[1].append(cnt) 
            c = s[i] #次の文字に移る
            cnt = 1
    if cnt > 0: #例えばAAABBだったら、B,2を記録する場所
        ret[0] += c
        ret[1].append(cnt)
    return ret