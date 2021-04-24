

pt = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."

with open('output.txt') as ctxt:
    ct = bytearray.fromhex(ctxt.readline().strip())
    flag = bytearray.fromhex(ctxt.readline().strip())


iv_encrypted = bytearray([pt_b ^ ct_b for pt_b, ct_b in zip(pt, ct)])

pt_flag = bytearray([f_b ^ iv_b for f_b, iv_b in zip(flag, iv_encrypted)])

print(pt_flag)
# CHTB{r3u53d_k3Y_4TT4cK

