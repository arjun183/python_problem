def countDistinct(s) : 
    m = {} 
    m = m.fromkeys(s, 0)

    for i in range(len(s)) : 
        m[s[i]] += 1
  
    return len(m.keys()) 
  
if __name__ == "__main__" : 
  
    str = input("")
    print(countDistinct(str))