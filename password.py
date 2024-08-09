"""password genarator"""
import random
import string

def generating(length):
    ch=string.ascii_letters+string.digits+string.punctuation

    password=''.join(random.choice(ch) for _ in range(length))
    return password
def main():
    length=int(input("enter the password length :"))
    password=generating(length)
    print("genaerting length",password)

if __name__=="__main__":
    main()