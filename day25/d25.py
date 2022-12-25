snafu = {
    "0": 0,
    "1": 1,
    "2": 2,
    "-": -1,
    "=": -2,
}

dec = {
    0: "0",
    1: "1",
    2: "2",
    3: "=",
    4: "-",
}

def snafu_to_dec(n):
    if len(n) == 1:
        return snafu[n]
    else:
        return snafu_to_dec(n[:-1])*5 + snafu[n[-1]]

def dec_to_pent(n):
    e = n//5
    q = n%5
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return dec_to_pent(e) + str(q)

def pent_to_snafu_help(n):
    if n<5:
        return(dec[n])
    else:
        u = dec[n%5]
        if u =="-" or u =="=":
            n+=5
        r = pent_to_snafu_help(n//5)
        return (r+u)

def pent_to_snafu(n):
    s = pent_to_snafu_help(n)
    return "1"+s if s[0]=="-" or s[0]=="=" else s





ans = 0
with open("input.txt", "r") as f:
    for line in f:
        ans += snafu_to_dec(line.strip())



# print(pent_to_snafu(344))
# print(snafu_to_dec("1-0-"))
print(pent_to_snafu(ans))
