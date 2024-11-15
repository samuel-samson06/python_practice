m=int(input())
M=set(map(int, input().split()))
n=int(input())
N=set(map(int,input().split()))
final_output=(M-N).union(N-M)
for i in sorted(final_output):
    print(i)