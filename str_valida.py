'''
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True
'''

if __name__ == '__main__':
    s = input().strip()
    
    al=a=d=l=u=False
    
    for i in s:
        if i.isalnum():
            al=True
            
        if i.isalpha():
            a=True
        
        if i.isdigit():
            d=True

            
        if i.islower():
            l=True
            
        if i.isupper():
            u=True
            
    print(al)
    print(a)
    print(d)
    print(l)
    print(u)
            
    