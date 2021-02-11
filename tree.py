"""Draw tree-fractal with recursion.

"""
import turtle

turtle.seth(90)
turtle.speed('fastest')


def draw_tree(branch_len, nodes_amount):
    """Draw tree-fractal.
        Keyword args:
            branch_len -- current len of branch (int)
            nodes_amount -- current amount of nodes (int)

    """
    if nodes_amount == 0:
        turtle.left(180)
        return

    x = branch_len / (nodes_amount + 1)
    for i in range(nodes_amount):
        turtle.forward(x)
        turtle.left(45)
        draw_tree(0.5 * x * (nodes_amount - i - 1), nodes_amount - i - 1)
        turtle.left(90)
        draw_tree(0.5 * x * (nodes_amount - i - 1), nodes_amount - i - 1)
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(branch_len)


if __name__ == "__main__":
    draw_tree(300, 5)
