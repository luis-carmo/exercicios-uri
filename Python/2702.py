ref1, ref2, ref3 = map(int, input().split())
pass1, pass2, pass3 = map(int, input().split())
test1 = 0
test2 = 0
test3= 0
if pass1 >ref1:
    test1 = pass1-ref1
if pass2 >ref2:
    test2 = pass2-ref2
if pass3 >ref3:
    test3 = pass3-ref3
final = test1+test2+test3
print(final)