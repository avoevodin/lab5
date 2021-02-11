"""Draw Minkowski curve fractal.

"""
import turtle

turtle.speed('fast')


def draw_minkowski_curve(segment_length: int, rec_deep: int):
    """Draw Minkowski curve with recursion.

    """
    new_segment_length = segment_length // 8
    if rec_deep == 0:
        turtle.forward(segment_length)
        return
    draw_minkowski_curve(new_segment_length, rec_deep - 1)
    turtle.left(90)
    draw_minkowski_curve(new_segment_length, rec_deep - 1)
    turtle.right(90)
    draw_minkowski_curve(new_segment_length, rec_deep - 1)
    turtle.right(90)
    draw_minkowski_curve(new_segment_length, rec_deep - 1)
    draw_minkowski_curve(new_segment_length, rec_deep - 1)
    turtle.left(90)
    draw_minkowski_curve(new_segment_length, rec_deep - 1)
    turtle.left(90)
    draw_minkowski_curve(new_segment_length, rec_deep - 1)
    turtle.right(90)
    draw_minkowski_curve(new_segment_length, rec_deep - 1)


if __name__ == "__main__":
    draw_minkowski_curve(2000, 3)
