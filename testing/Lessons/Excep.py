class CalcError(Exception):
    pass


def get_num_sqr(a):
    try:
        return a**2
    except Exception as e:
        raise CalcError
def main():
    sqr_1 = get_num_sqr('5')
    print(sqr_1)


try:
    main()
except Exception as e:
    print(e)
    exit(2)
