def validate(n):
    try:
        if n.isdigit():
            return True
        else:
            return "Please enter integer number greater than 0"
    except Exception as e:
        return str(e)


def ackvalidate(fnum1,fnum2):
    try:
        if fnum1.isdigit() & fnum2.isdigit():
            return True
        else:
            return "Input Error! Please input a positive integer number in both inputs"

    except Exception as e:
        return str(e)
