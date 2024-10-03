

def main():
    s = "aagctt"

    print(s)
    print('chop by 1:', chop(s, 1))
    print('chop by 2:', chop(s, 2))
    print('chop by 3:', chop(s, 3))
    print('chop by 4:', chop(s, 4))
    


def chop(s, n):
    i = 0
    out = []
    while i < len(s):
        out.append(s[i:i+n])
        i += n
    return out
        
        

if __name__ == '__main__': 
    main()
