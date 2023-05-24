import numpy as np

# Function that returns the largest y values and their corresponding x
def takeupper(x,y):
    x_init = x[0]
    y_ret = []
    x_ret = []
    x_ret.append(x[0])
    top = min(y)

    for i in range(len(x)):
        if x[i] == x_init:
            if top < y[i]:
                top = y[i]
        else:
            x_ret.append(x[i])
            y_ret.append(top)
            top = y[i]
            x_init = x[i]
    y_ret.append(top)

    return x_ret,y_ret

# Function that returns the lowest y values and their corresponding x
def takelower(x,y):
    x_init = x[0]
    y_ret = []
    x_ret = []
    x_ret.append(x[0])
    bot = max(y)

    for i in range(len(x)):
        if x[i] == x_init:
            if bot > y[i]:
                bot = y[i]
        else:
            x_ret.append(x[i])
            y_ret.append(bot)
            bot = y[i]
            x_init = x[i]
    y_ret.append(bot)

    return x_ret,y_ret

# Function that returns the lowest y values and their corresponding x
def takemean(x,y):
    # Calculating mean waggles:
    init = x[0]
    y_ret = []
    x_ret = []
    x_ret.append(init)
    mean = 0
    iterat = 0

    for i in range(len(x)):
        if x[i] == init:
            mean+=y[i]
            iterat+=1
        else:
            init = x[i]
            x_ret.append(init)
            y_ret.append(mean/iterat)
            mean = y[i]
            iterat = 1
    y_ret.append(mean/iterat)

    return x_ret,y_ret