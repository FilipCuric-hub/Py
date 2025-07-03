def unatrag_rijec(s):
    if s == "":
        return""
    
    return unatrag_rijec(s[1:])+s[0]


print(unatrag_rijec("zdravo"))
