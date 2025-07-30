import sys

#  WHy does this work

def ZAlg(string):
    n = len(string)
    zarr = [0]*n
    x=0;y=0
    for i in range(1,n):
        zarr[i] = max(0,min(zarr[i-x],y-i+1))
        while (i+zarr[i] < n and string[zarr[i]] == string[i+zarr[i]]):
            x = i; y = i + zarr[i]
            zarr[i]+=1
    return zarr



print(ZAlg("ACBACDACBACBACDA"))
# print(ZAlg("abababcab"))

# print(ZAlg("ATT#HATTIVATTI"))


# 


def manacher_odd(s):
    n = len(s)
    s = "$" + s + "^"  # Add boundaries to simplify edge cases
    p = [0] * (n + 2)  # Initialize the array to store palindrome radii
    l, r = 1, 1  # Left and right bounds of the current palindrome

    for i in range(1, n + 1):
        p[i] = max(0, min(r - i, p[l + (r - i)]))  # Mirror property
        while s[i - p[i]] == s[i + p[i]]:  # Expand around the center
            p[i] += 1
        if i + p[i] > r:  # Update bounds if the palindrome expands beyond r
            l = i - p[i]
            r = i + p[i]
    
    return p[1:-1]
  

# "#a#b#c#b#c#b#a#"
# "#a#b#b#a#"
# print(manacher_odd("#a#b#c#b#c#b#a#"))
