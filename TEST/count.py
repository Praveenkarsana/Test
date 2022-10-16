def count(a):
    count={}
    words=a.split()
    for words in words:
        if words in count:
            count[words]+=1
        else:
            count[words]=1
    print(count)
count("""strength is life and weakness is death. Expansion is life and contraction is death. Hatred is death and love is life.- Swami Vivakanand:""")                