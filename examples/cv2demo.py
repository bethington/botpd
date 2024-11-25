import cv2

def show_image():
    # Load an image from file
    image = cv2.imread('example.jpg')

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load image.")
        return

    # Display the image in a window
    cv2.imshow('Demo Image', image)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_image()