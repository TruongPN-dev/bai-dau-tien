def longest():
    # s = "pwwkew"
    s = "abcuiebgwjbewbgijvbiusdheoehebv98phqe"
    # s = "bbbbbbbb"
    # s = "abcacbacbb"
    nho = ""
    ghi = ""
    i = 0
    while i < len(s):
        j = i
        while j < len(s):
            for k in nho:
                if k == s[j]:
                    if len(nho) > len(ghi):
                        ghi = nho
                        nho = ""
                    else:
                        nho = ""
            nho += s[j]
            j += 1
        nho = ""
        i += 1
    return ghi

print(longest())