import hashlib
import ecdsa
import sys
import binascii

def get_final_btc_address(x,y):
    # x: 公钥x值
    # y: 公钥y值
    # 拼接04后的16进制字符串
    first_string = '04' + x + y
    print(first_string)
    print(bytes.fromhex(first_string))
    print(binascii.hexlify(bytes.fromhex(first_string)).decode().upper())



if __name__ == '__main__':
    final_address = get_final_btc_address('1E25ECA6C24E4438DB9AD6E66A63D97855F0E910DDF15D3EEF256AD9D541CD5A','F22469776B19A8F60D170CDB566CC90EB56DC1FBBD14BE5A6086A759594AD08F')