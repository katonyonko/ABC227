import io
import sys

_INPUT = """\
6
3
10 20 39
5
666 777 888 777 666
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=list(map(int,input().split()))
  ans=0
  for i in range(N):
    flag=False
    for a in range(1,340):
      for b in range(1,340):
        if 4*a*b+3*a+3*b==S[i]:
          flag=True
    if flag==False: ans+=1
  print(ans)