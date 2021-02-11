"""Draw Koch curve fractal with recursion.

"""
import turtle
turtle.speed('fastest')


def draw_koch_curve(line_length, rec_deep: int):
    """Draw Koch curve fractal.

        Keyword args:
            line_length -- length of base line (int)
            rec_deep -- deep of recursion (int)

    """
    segment_length = line_length / 3
    draw_koch_segment(segment_length, rec_deep)
    turtle.left(60)
    draw_koch_segment(segment_length, rec_deep)
    turtle.right(120)
    draw_koch_segment(segment_length, rec_deep)
    turtle.left(60)
    draw_koch_segment(segment_length, rec_deep)


def draw_koch_segment(segment_length, rec_deep):
    """Draw segment of Koch curve.

        Keyword args:
            segment_length -- length of base line (int)
            rec_deep -- deep of recursion (int)

    """
    if rec_deep == 1:
        turtle.forward(segment_length)
    else:
        draw_koch_curve(segment_length, rec_deep - 1)


if __name__ == "__main__":
    draw_koch_curve(250, 2)
