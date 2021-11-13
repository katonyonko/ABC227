import io
import sys

_INPUT = """\
6
3 3
2 3 4
4 2
1 1 3 4
4 3
1 1 3 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  A.sort(reverse=True)
  l,r=0,10**20
  # print(A)
  while r-l>1:
    mid=(l+r)//2
    flag=False
    row,col=0,0
    for i in range(N):
      if A[i]>=mid:
        row+=1
      else:
        if col+A[i]>=mid:
          row+=1
          col=col+A[i]-mid
        else:
          col+=A[i]
      if row>=K:
        flag=True
        break
    if flag==True:
      l=mid
    else: r=mid
  print(l)