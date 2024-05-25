class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    def calculate_area(self):
        return self.width * self.height
    def draw_rectangle(self):
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print("*" * self.width)
            else:
                print("*" + " " * (self.width - 2) + "*")
                
def main():
    while True:
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enther the height of the rectangle: "))
        rectangle = Rectangle(width, height)
        print("Perimeter:" , rectangle.calculate_perimeter())
        print("Area:" , rectangle.calculate_area())
        print("Rectangle: ")
        rectangle.draw_rectangle()
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != "yes":
            break
        
if __name__ == "__main__":
    main()
    
