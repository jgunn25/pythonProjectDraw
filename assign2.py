
import area_calculation
import draw_shape

T = True

area_list = []



def is_valid_shape(shape):
    if shape == "square" or shape == "circle" or shape == "triangle":
        return True
    else:
        return False


def main():
    """
    Gives conditional statements withing the while function to ask which symbols and variables are needed to be
    used for the draw_shape file

    main() gets automatically executed which then asks for inputs on what the user wishes to draw. This information
    then gets passed to draw_shape tool.
    """
    while True:
        shape = input("What shape would you like to draw?\n").lower()
        if shape == "done":
            return False
        if is_valid_shape(shape) == True:

            if shape.lower() == "circle":
                colour = input("What color would you like the shape to be?\n")
                position_x = float(input("what is the x position?\n"))
                position_y = float(input("what is the y position?\n"))
                radius = float(input("what is the radius of the circle\n"))
                cir_area = float(area_calculation.circle_area(radius))
                area_list.append(cir_area)
                draw_shape.draw_circle(radius, position_x, position_y, colour)
                print(cir_area)

            elif shape.lower() == "square":
                colour = input("What color would you like the shape to be?\n")
                position_x = float(input("what is the x position?\n"))
                position_y = float(input("what is the y position?\n"))
                length = float(input("what is the length of the side of the square?\n"))
                sq_area = float(area_calculation.square_area(length))
                draw_shape.draw_square(length, position_x, position_y, colour)
                area_list.append(sq_area)
                print(sq_area)

            elif shape.lower() == "triangle":
                colour = input("What color would you like the shape to be?\n")
                position_x = float(input("what is the x position?\n"))
                position_y = float(input("what is the y position?\n"))
                base = float(input("what is the length of the triangle base?\n"))
                tri_area = float(area_calculation.triangle_area(base))
                area_list.append(tri_area)
                draw_shape.draw_triangle(base, position_x, position_y, colour)
                print(tri_area)

        else:
            print("sorry, but that shape doesn't exist in our system. Please try again.")


main()
# Once input = 'done' the while loop turns false and sorts all area calculations then prints them.
area_list.sort()
print(f"Thank you for using this program! Here isa list of the area that we calculated for you: {area_list}")
draw_shape.turtle.mainloop()
