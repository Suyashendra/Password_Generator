def rules():
    print("****************Password Must Contain Following******************* ")
    print("1.At least one uppercase character (A-Z).")
    print("2.At least one lowercase character (a-z).")
    print("3.At least one digit (0-9).")
    print("4.At least one special symbol (@, !, #, $, %, ^, &, *, ?, ~).")
    print("5.At least eight characters.")
    print("Enter a Password:")
def check_password(pasw, pasw_len):
    c = 1
    d = l = u = s = 0
    special = "@!#$%^&*?~"
    for i in range(pasw_len):
        if pasw[i].isdigit():
            d = 1
            continue
        elif pasw[i].islower():
            l = 1
            continue
        elif pasw[i].isupper():
            u = 1
            continue
        elif pasw[i] in special:
            s = 1
            continue
        else:
            c = 0
            return c
    if (d==1 & l==1 & u==1 & s==1):
        return c
    else:
        return 0    

if __name__ == "__main__":
    print("Create a Password:")
    res = 0
    while(res!=1):  
        password = input()
        x = list(password)
        n = len(x)
        if n<8:
            res = 0
            print("You have entered wrong password")
            rules()
            continue
        else:
            res = check_password(x,n)
            if res==0:
                print("You have entered wrong password")
                rules()
            else:
                print("Password Updates Successfully")    