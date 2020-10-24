#запихнуть параметры в генератор

import sys

def main(src, dst):
    file_in = open(src)
    res = file_in.read()
    file_in.close()
    file_out = open(dst, 'w')
    file_out.write(res)
    file.out.close()

if __name__ == "__main__":
    params = sys.argv
    main(params[1]. params[2])