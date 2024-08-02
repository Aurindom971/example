'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example





: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

if __name__ == '__main__':
    N = int(input())
    l=[]
    c=[]
    for i in range(N):
        b=input().strip().split()

        if b[0]=="insert":
            l.insert(int(b[1]),int(b[2]))
        elif b[0]=="append":
            l.append(int(b[1]))
        elif b[0]=="remove":
            l.remove(int(b[1]))
        elif b[0]=="sort":
            l.sort()
        elif b[0]=="pop":
            l.pop()
        elif b[0]=="reverse":
            l=l[::-1]
        elif b[0]=="print":
            print(l)
        else:
            pass
            
        