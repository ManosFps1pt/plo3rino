import time

def runtime(func):
    def wrapper(*args, **kwargs):
        time1 = time.perf_counter()
        ret = func(*args, **kwargs)
        time2 = time.perf_counter()
        print(f"function '{func.__name__}' executed in {time2 - time1} seconds")
        return ret

    return wrapper


@runtime
def dda(x1, y1, x2, y2, format):
    dx = x2 - x1
    dy = y2 - y1
    if format.lower() == "full":
        steps = max(abs(dx), abs(dy))
    elif format.lower() == "goto":
        steps = min(abs(dx), abs(dy))
    else:
        raise ValueError("incorrect format type. You should use 'full' or 'goto'. ")
    try:
        x_inc = dx / steps
        y_inc = dy / steps
    except ZeroDivisionError:
        raise ValueError("cannot create a line that has the length of a pixel. Try making a longer line")
    for _ in range(steps + 1):
        returning_x = round(x1)
        returning_y = round(y1)
        x1 += x_inc
        y1 += y_inc
        yield returning_x, returning_y


@runtime
def circle(cx: int, cy: int, rad: int, format: str, extend: bool = True):
    if format.lower() != "goto" and format.lower() != "full":
        raise ValueError("incorrect format type. You should use 'full' or 'goto'.")
    res = []
    x, y = 0, rad
    d = 3 - (2 * rad)
    res.append((x, y))
    while y >= x:
        x += 1
        if d <= 0:
            d = d + 4 * x + 6
        else:
            y -= 1
            d = d + 4 * (x - y) + 10
            if format.lower() == "goto":
                res.append((x, y))
        if format.lower() == "full":
            res.append((x, y))

    for i in res:
        yield i[0] + cx, i[1] + cy
    if extend:
        for i in res[::-1]:
            yield i[1] + cx, i[0] + cy
        for i in res:
            yield i[1] + cx, -i[0] + cy
        for i in res[::-1]:
            yield i[0] + cx, -i[1] + cy
        for i in res:
            yield -i[0] + cx, -i[1] + cy
        for i in res[::-1]:
            yield -i[1] + cx, -i[0] + cy
        for i in res:
            yield -i[1] + cx, i[0] + cy
        for i in res[::-1]:
            yield -i[0] + cx, i[1] + cy


def lerp(a, b, t):
    return a[0] + (a[1] - a[0]) * t, b[0] + (b[1] - b[0]) * t


def quadratic(a, b, c, t):
    p0 = lerp(a, b, t)
    p1 = lerp(b, c, t)
    return lerp(p0, p1, t)


def cubic(a, b, c, d, t):
    p0 = quadratic(a, b, c, t)
    p1 = quadratic(b, c, d, t)
    return lerp(p0, p1, t)


def lineH(x0, y0, x1, y1):
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    direction = -1 if dy < 0 else 1
    dy *= direction

    if dx != 0:
        y = y0
        p = 2 * dy - dx
        for i in range(dx + 1):
            yield x0 + i, y
            if p >= 0:
                y += direction
                p = p - 2 * dx
            p = p + 2 * dy


def lineV(x0, y0, x1, y1):
    if y0 > y1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    direction = -1 if dx < 0 else 1
    dx *= direction

    if dy != 0:
        x = x0
        p = 2 * dx - dy
        for i in range(dx + 1):
            yield x, y0 + i
            if p >= 0:
                x += direction
                p = p - 2 * dy
            p = p + 2 * dx


def line(x0, y0, x1, y1):
    if abs(x1 - x0) > abs(y1 - y0):
        return lineH(x0, y0, x1, y1)
    else:
        return lineV(x0, y0, x1, y1)




