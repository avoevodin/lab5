"""Draw Koch snowflake fractal with recursion.

"""
import turtle
from koch_curve import draw_koch_curve

turtle.speed('fastest')


def draw_koch_snowflake(edge_width: int, rec_deep: int):
    """Draw Koch snowflake.

        Keyword args:
            edge_width -- width of snowflake's edge (int)
            rec_deep -- deep of recursion (int)

    """
    for i in range(3):
        if i:
            turtle.right(120)
        draw_koch_curve(edge_width, rec_deep)


if __name__ == "__main__":
    draw_koch_snowflake(250, 4)
