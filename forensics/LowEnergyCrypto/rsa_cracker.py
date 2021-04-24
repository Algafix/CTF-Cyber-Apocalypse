
from Crypto.PublicKey import RSA
import libnum

key = RSA.importKey(open('pub_key.pem').read())
n = key.n
e = key.e

#ct = 0x392969b018ffa093b9ab5e45ba86b4aa070e78b839abf11377e783626d7f9c4091392aef8e13ae9a22844288e2d27f63d2ebd0fb90871016fde87077d50ae538
ct = 2993804760167633099930505498648506239640172270016559466390218887201150673861396609844588440275261454637918712842058609100864369907294618342413502769718584
p = 92270847179792937622745249326651258492889546364106258880217519938223418258871
q = 92270847179792937622745249326651258492889546364106258880217519938223418249279


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

phi = (p-1)*(q-1)

gcd, a, b = egcd(e, phi)
d = a

pt = pow(ct, d, n)

bytes_text = pt.to_bytes((pt.bit_length() + 7) // 8, 'big')

print(bytes_text)
#CHTB{5p34k_fr13nd_4nd_3n73r}
