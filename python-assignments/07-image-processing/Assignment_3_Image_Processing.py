# Hello ,This is Assignment 3 for CS 87B where we will create an Image Processing App
# Name: Tanjim Ahmed Al Zabeer
# This program will load an image for us and it will aslo give us a menu to resize, flip, or turn it gray.
# I reused the image object to keep the code easier and shorter.


import cv2

counter = 1

def resize_image(img):
    height, width = img.shape[:2]
    print("1. Resize Up (double size)")
    print("2. Resize Down (half size)")
    choice = input("Enter your choice: ")

    if choice == '1':
        resized = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_LINEAR)
        filename = f"resized_tiger_up_{get_count()}.jpg"
    else:
        resized = cv2.resize(img, (width//2, height//2), interpolation=cv2.INTER_AREA)
        filename = f"resized_tiger_down_{get_count()}.jpg"

    cv2.imwrite(filename, resized)
    print("Saved:", filename)

def flip_image(img):
    print("1. Flip Horizontally")
    print("2. Flip Vertically")
    print("3. Flip Both")
    choice = input("Enter your choice: ")

    if choice == '1':
        flipped = cv2.flip(img, 1)
        filename = f"flipped_tiger_h_{get_count()}.jpg"
    elif choice == '2':
        flipped = cv2.flip(img, 0)
        filename = f"flipped_tiger_v_{get_count()}.jpg"
    else:
        flipped = cv2.flip(img, -1)
        filename = f"flipped_tiger_both_{get_count()}.jpg"

    cv2.imwrite(filename, flipped)
    print("Saved:", filename)

def grayscale_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filename = f"grayscale_tiger_{get_count()}.jpg"
    cv2.imwrite(filename, gray)
    print("Saved:", filename)

def get_count():
    global counter
    current = counter
    counter += 1
    return current

def main():
    img = cv2.imread("Sundarban_Tiger.jpg")
    if img is None:
        print("Image not found. Please check the filename.")
        return

    while True:
        print("\nImage Processing Menu")
        print("1. Resize")
        print("2. Flip")
        print("3. Grayscale")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            resize_image(img)
        elif choice == '2':
            flip_image(img)
        elif choice == '3':
            grayscale_image(img)
        elif choice == '4':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Try again.")

main()
