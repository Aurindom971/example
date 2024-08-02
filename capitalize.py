'''
A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
'''


import os

def solve(s):
    '''
    l=s.strip().split()
    t=""
    cnt=0
    for i  in l:
        if cnt==0:
            
            t=t+""+i.capitalize()
            cnt+=1
        else:
             t=t+" "+i.capitalize()    
    '''
    
    l=s.strip().split(" ")
    l1=[]
    for i in l:
        l1.append(i.capitalize())
    
    result=" ".join(l1)
    
    return result
    
    






    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

