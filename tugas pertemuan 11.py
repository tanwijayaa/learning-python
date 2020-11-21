def palindrome (kata, h, z):
    if h == z//2 :
        return 'Yes, it is a palindrome'
    elif z % 2 == 0:
        if kata[z//2 - h - 1] == kata[z//2 + h]:
            return palindrome (kata, h + 1, z)
        else:
            return 'No, it is not a palindrome'
    else:
        if kata[z//2 - h - 1] == kata[z//2 + 1 + h]:
            return palindrome (kata, h + 1, z)
        else:
            return 'No, it is not a palindrome'


while True:
    x = input('kata? ')
    print(palindrome(x,0,int (len(x))))