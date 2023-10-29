def search(pat, txt):  # time : O(n to the power m), space: O(1)
    m = len(pat)
    n = len(txt)
    k = float('inf')
    for i in range(n - m):
        for j in range(m):
            k = j + 1
            if txt[i + j] != pat[j]:
                break
        if k == m:
            print("Pattern found at index ", i)


txt_ = "AABAACAADAABAAABAA"
pat_ = "AABA"
search(pat_, txt_)