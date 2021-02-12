"""Draw Cantor set factorial.

"""
import turtle

turtle.speed('fastest')
turtle.penup()
turtle.backward(300)
turtle.pendown()

VERTICAL_SHIFT = 30


def draw_cantor_set(line_width, rec_deep):
    """Draw cantor set factorial.
        Keyword args:
            line_width -- current width of line (int)
            rec_deep -- current deep of recursion (int)

    """
    if rec_deep == 0:
        return
    turtle.forward(line_width)
    turtle.penup()
    turtle.backward(line_width)

    if rec_deep > 1:
        turtle.right(90)
        turtle.forward(VERTICAL_SHIFT)
        turtle.left(90)
    turtle.pendown()

    if rec_deep > 1:
        new_line_width = line_width // 3
        draw_cantor_set(new_line_width, rec_deep - 1)
        turtle.penup()
        turtle.forward(line_width - new_line_width)
        turtle.pendown()
        draw_cantor_set(new_line_width, rec_deep - 1)
        turtle.penup()
        turtle.backward(line_width - new_line_width)
        turtle.left(90)
        turtle.forward(VERTICAL_SHIFT)
        turtle.right(90)
        turtle.pendown()


if __name__ == "__main__":
    draw_cantor_set(600, 6)
