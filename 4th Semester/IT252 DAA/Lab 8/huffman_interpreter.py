def main():
    lines = [line.rstrip('\n') for line in open('code.txt','r')]
    codes = [(i[:-1:],i[-1]) for i in lines]

    str_file = ''
    str_ = input('Enter text to be encoded')

    n_c = len(codes)
    n_s = len(str_)

    for j in range(n_s):
        for i in range(n_c):
            if str_[j] == codes[i][1]:
                str_file += codes[i][0]
                break

    file = open('encode.txt','w+')
    file.write(str_file)
    file.close()

if __name__ == '__main__':
    main()