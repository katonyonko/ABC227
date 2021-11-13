import io
import sys

_INPUT = """\
6
4
100
100000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  ans=0
  A=1
  while A**3<=N:
    B=A
    while A*B*B<=N:
      ans+=N//(A*B)-B+1
      B+=1
    A+=1
  print(ans)