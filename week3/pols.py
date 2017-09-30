import sys
from flask import Flask

app = Flask(__name__)

ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '^': lambda a, b: a ** b,
}


def convert_exp(exp):
    '''
    3 +4 * 2 / (1-5) ^ 2
    '''
    hpo = '*/'
    lpo = '-+^'
    stak = []
    result = []
    for el in exp:
        if el.isdigit():
            result.append(el)
        elif el == '(':
            stak.append(el)
        elif el == ')':
            elFromStak = stak.pop()
            result.append(elFromStak)
            stak.pop()
        else:
            if not stak:
                lse = lambda: True

            if el in lpo or lse():
                stak.append(el)
            else:
                elFromStak = stak.pop()
                result.append(elFromStak)
                stak.append(el)

            lse = lambda: False if stak[-1] in hpo else True

    for el in reversed(stak):
        result.append(el)

    return ' '.join(result)


def my_eval(expression):
    '''
    :param expression: 9 99 +
    :return sum:
    '''

    tokens = expression.split()
    stak = []
    print(tokens)

    for token in tokens:
        if token in ops:
            arg2 = float(stak.pop())
            arg1 = float(stak.pop())
            result = ops[token](arg1, arg2)
            stak.append(result)
        else:
            stak.append(token)

    return stak.pop()

def main(expr):
    text = expr
    exp = convert_exp(text)
    result = my_eval(exp)
    return result

@app.route("/<expr>")
def pol(expr):
    return "{}".format(main(expr))

if __name__ == '__main__':
    app.run(debug=True)