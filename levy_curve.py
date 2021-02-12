"""Draw Levy curve fractal.

"""
import turtle
turtle.speed('fastest')


def draw_levy_curve(edge_width: int, rec_deep: int):
    """Draw Levy curve fractal.

        Keyword args:
            edge_width -- current width of edge (int)
            rec_deep -- current recursion deep (int)

    """
    if rec_deep == 0:
        turtle.forward(edge_width)
        return
    new_edge_width = (edge_width ** 1 / 2) / 2
    turtle.left(45)
    draw_levy_curve(new_edge_width, rec_deep - 1)
    turtle.right(90)
    draw_levy_curve(new_edge_width, rec_deep - 1)
    turtle.left(45)


if __name__ == "__main__":
    draw_levy_curve(3000000, 9)
