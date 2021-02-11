"""Draw Koch curve fractal with recursion.

"""
import turtle
turtle.speed('fastest')


def draw_koch_curve(line_length, rec_deep: int):
    """Draw Koch curve fractal.

    """
    segment_length = line_length / 3
    if rec_deep == 1:
        turtle.forward(segment_length)
        turtle.left(60)
        turtle.forward(segment_length)
        turtle.right(120)
        turtle.forward(segment_length)
        turtle.left(60)
        turtle.forward(segment_length)
        return
    draw_koch_curve(segment_length, rec_deep - 1)
    turtle.left(60)
    draw_koch_curve(segment_length, rec_deep - 1)
    turtle.right(120)
    draw_koch_curve(segment_length, rec_deep - 1)
    turtle.left(60)
    draw_koch_curve(segment_length, rec_deep - 1)


if __name__ == "__main__":
    draw_koch_curve(250, 4)
