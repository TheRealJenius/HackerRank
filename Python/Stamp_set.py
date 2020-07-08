# Enter your code here. Read input from STDIN. Print output to STDOUT
stamp_set = set()
N = int(input()) # needs to be an integer as it reads input as a string

for i in range(N):
    stamp = input()
    stamp_set.add(stamp) # sets are mutable

print(len(stamp_set))

'''
First input will be the number of country stamps
Task - finding the number of disticnt countries

Example:
7
UK
China
USA
France
New Zealand
UK
France 

answer = 5 Distinct countries
'''