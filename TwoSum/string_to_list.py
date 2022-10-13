s = "string" 
# TURN IT INTO LIST IT WITHOUT USING TYPE CASTING
a,b,c,d,e,f="string"
print(a,b,c,d,e,f)
l=[]
l.extend(a.split())
l.extend(b.split())
l.extend(c.split())
l.extend(d.split())
l.extend(e.split())
l.extend(f.split())
print(l)
