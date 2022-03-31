# Muhammad Didik Wahyudi
# 20051397040


def main(string):
    print('Menampilkan huruf pertama dari string:')
    print(string.split()[0][0])
    for word in string.split():
        print('%s' % word[0], end = ' ')
    print()

# show last letter of each word in a string
def main2(string):
    print('Menampilkan huruf terakhir dari string:')
    for word in string.split():
        print('%s' % word[-1], end = ' ')
    print()
    

# show choice letter of each word in a string
def main3(string, choice):
    print('Menampilkan huruf ke %s dari string:' % choice)
    for word in string.split():
        print('%s' % word[choice], end = ' ')
    print()

string = 'PRAKTIKUM ALPRO1'
main(string)
main2(string)
main3(string, 2)