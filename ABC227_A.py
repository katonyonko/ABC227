import io
import sys

_INPUT = """\
6
3 3 2
1 100 1
3 14 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K,A=map(int,input().split())
  print((A+K-2)%N+1)