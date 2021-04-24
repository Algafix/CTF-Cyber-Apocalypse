
def xor(short_text, long_text):
    return bytearray([s_b ^ l_b for s_b, l_b in zip(short_text, long_text)])

with open('output.txt') as ctxt:
    ct = bytearray.fromhex(ctxt.readline().strip())
    flag = bytearray.fromhex(ctxt.readline().strip())

xored_pt = xor(flag, ct)

rec_pt = xor(b'CHTB{', xored_pt)

print(rec_pt)

# b'I alo
# Famous quote, "I alo"ne?
# Last quote was from Whitfield Diffie, maybe this from Martin Hellman?
# No luck

# But there's a quote from Mother Teresa:

quote = b'I alone cannot change the world, but I can cast a stone across the water to create many ripples.'

print(len(quote))
print(len(xored_pt))

rec_flag = xor(xored_pt, quote)

print(rec_flag)

# CHTB{stream_ciphers_with_reused_keystreams_are_vulnerable_to_known_plaintext_attacks}

