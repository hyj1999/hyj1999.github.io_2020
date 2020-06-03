from Crypto.Cipher import AES
import requests

def readts(root, name):
    key='f28024d7cbad8f9e'
    key = key.encode(encoding = "utf-8")
    cryptor = AES.new(key, AES.MODE_CBC, key)
    with open(root+name, 'rb') as f:
        ts = f.read()
        f.close()
    return cryptor.decrypt(ts)

def writemp4(root, name, ts):
    with open(root+name, 'ab') as f:
        f.write(ts)
        f.close()



def main():
    root = './VideoData/780bba6237271add93e96fe4c4bff88c7ff50724/'
    mp4name = '48.mp4'
    for i in range(529):
         tsname = 'Y2hlbmppbmdjb25n{}'.format(i)
         print( "\r读取{}    ".format(tsname), end = '')
         ts = readts(root, tsname)
         print( "转换{}    ".format(tsname), end = '' )
         writemp4(root, mp4name, ts)
         print( "{}转换完成".format(tsname), end = '' )

main()
