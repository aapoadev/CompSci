def dashify_substring(s, sub):
    if not sub:
        out = 'ei subii'
    else:
        dash = '-'+ sub + '-'
        out = s.replace(sub,dash, count=1)
    return (out)
s = 'moikka'
sub='moi'
print(dashify_substring(s,sub)) 
