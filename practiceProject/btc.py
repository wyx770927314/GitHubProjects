import hashlib
import binascii


def get_final_btc_address(x, y):
    """
        BASE58:base58编码的对照表
        x:公钥x值
        y:公钥y值
        用到的方法说明：
            1）bytes.fromhex方法是将表示16进制的字符串转换成bytes对象
            2）hashalib.sha256()的参数需要穿传bytes对象
            3）hashlib对象的hexdigest方法是将哈希对象转换成16进制数据的字符串值，类型是<str>
            4）hashlib对象的digest方法是将哈希对象转换成2进制数据的字符串值，类型是<bytes>
            5) binascii.hexlify()传入的参数是bytes类型，作用是将2进制的bytes转换成16进制
            6）int.from_bytes()传入参数是bytes对象，作用是将bytes对象转换成int对象
    """
    BASE58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

    uncompressed_public_key = '04' + x + y
    print('1.拼接未压缩的X、Y公钥之后得(字符串)：' + uncompressed_public_key)

    uncompressed_public_key_hexbytes = bytes.fromhex(uncompressed_public_key)
    print('2.将步骤1中表示16进制的字符串转成bytes对象：', uncompressed_public_key_hexbytes)

    sha256_public_key = hashlib.sha256(uncompressed_public_key_hexbytes)
    print('3.将步骤2中的bytes对象进行SHA256加密后的结果：', sha256_public_key.hexdigest().upper(), type(sha256_public_key))

    h = hashlib.new('ripemd160', sha256_public_key.digest())
    print('4.将步骤3中的结果进行RIPEMD160加密后的结果', h.hexdigest().upper())

    first_sha256 = hashlib.sha256(bytes.fromhex('00') + h.digest())
    print('5.进行第一次SHA256加密后的结果', first_sha256.hexdigest().upper())

    second_sha256 = hashlib.sha256(first_sha256.digest())
    print('6.进行第二次SHA256加密后的结果', second_sha256.hexdigest().upper())

    checknums = second_sha256.digest()[0:4]  # 提取校验码
    payload = bytes.fromhex('00') + h.digest() + checknums  # 将提取到的校验码放到ripemd160加密之后的地址后面
    print('7.将校验码加上之后得到的地址：', binascii.hexlify(payload).decode().upper())

    num = int.from_bytes(payload, byteorder="big")
    padding = len(payload) - len(payload.lstrip(b'\0'))  # 计算第7步中左侧的b'\0'
    encoded = []  # 用来存放余数(num除以58)对照BASE58表之后的值
    while num != 0:
        num, remainder = divmod(num, 58)
        encoded.append(BASE58[remainder])
    print('8.最终的BTC地址为：', padding * "1" + "".join(encoded)[::-1])


if __name__ == '__main__':
    get_final_btc_address('1E25ECA6C24E4438DB9AD6E66A63D97855F0E910DDF15D3EEF256AD9D541CD5A',
                          'F22469776B19A8F60D170CDB566CC90EB56DC1FBBD14BE5A6086A759594AD08F')
