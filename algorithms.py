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


# testing
if __name__ == "__main__":
    import turtle
    import time
    import sys

    pen = turtle.Turtle()

    pen.speed(0)
    turtle.title("plo3rino")
    goto_counter = 0
    format = "full"


    @runtime
    def gotoPoints(points, up_to_go=True):
        global goto_counter
        print("||||| gotoPoints |||||\n")
        if up_to_go:
            for i in points:
                pen.up()
                pen.goto(i[0], i[1])
                goto_counter += 1
                pen.down()
                break
        for idx, i in enumerate(points):
            pen.goto(round(i[0]), round(i[1]))
            goto_counter += 1
            print(f"{idx}:\t({round(i[0])}, {round(i[1])})")
        print("\n")


    def main():
        from gcode_manage import decode_gcode
        
        decode_gcode()


    main()

