"""Draw dragon curve fractal.

"""
import turtle
turtle.left(90)
turtle.speed('fastest')

def draw_dragon_curve(edge_width: int, rec_deep: int, shift = 0):
    """Draw dragon curve fractal with recursion.

        Keyword args:
            edge_width -- current width of edge (int)
            rec_deep -- current recursion deep (int)

    """
    first_rotation = turtle.right if shift == 1 else turtle.left
    second_rotation = turtle.left if shift == 1 else turtle.right
    if rec_deep == 0:
        turtle.forward(edge_width)
        return
    new_edge_width = (edge_width ** 1 / 2) / 2
    first_rotation(45)
    draw_dragon_curve(new_edge_width, rec_deep - 1)
    second_rotation(90)
    draw_dragon_curve(new_edge_width, rec_deep - 1, 1)
    first_rotation(45)


if __name__ == "__main__":
    draw_dragon_curve(25000000000, 16)
