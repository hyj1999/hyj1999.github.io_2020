from PIL import Image
import os

def get_size(file):
    # 获取文件大小:KB
    size = os.path.getsize(file)
    return size / 1024

def get_outfile(infile, outfile):
    '''拼接输出文件地址'''
    if outfile:
        return outfile
    dir, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(dir, suffix)
    return outfile

def compress_image(infile, outfile='', mb=100, step=10, quality=80):
    '''压缩文件到指定大小，我期望的是100KB,step和quality可以修改到最合适的数值'''
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
    o_size = get_size(infile)
    if o_size <= mb:
        return infile
    outfile = get_outfile(infile, outfile)
    while o_size > mb:
        im = Image.open(infile)
        #出现 OSError: cannot write mode RGBA as JPEG 错误时加入下方语句
        #im = im.convert("RGB")
        im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = get_size(outfile)
    return outfile, get_size(outfile)

def resize_image(infile, outfile='', x_s=1376):
    '''修改图片尺寸，如果同时有修改尺寸和大小的需要，可以先修改尺寸，再压缩大小'''
    """修改图片尺寸
    :param infile: 图片源文件
    :param outfile: 重设尺寸文件保存地址
    :param x_s: 设置的宽度
    :return:
    """
    im = Image.open(infile)
    x, y = im.size
    y_s = int(y * x_s / x)
    out = im.resize((x_s, y_s), Image.ANTIALIAS)
    outfile = get_outfile(infile, outfile)
    out.save(outfile)

if __name__ == '__main__':
    compress_image(r'D:\learn\space.jpg')
    resize_image(r'D:\learn\space.jpg')
    
