import cv2
import numpy as np


def compute_difference(bg_img, input_img):
    # Resize input_img to match bg_img dimensions
    input_img_resized = cv2.resize(
        input_img, (bg_img.shape[1], bg_img.shape[0]))
    difference_single_channel = cv2.absdiff(bg_img, input_img_resized)
    return difference_single_channel


def compute_binary_mask(difference_single_channel):
    gray = cv2.cvtColor(difference_single_channel, cv2.COLOR_BGR2GRAY)
    _, difference_binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    return difference_binary


def replace_background(bg1_image, bg2_image, ob_image):
    # Resize bg2_image and ob_image to match bg1_image dimensions
    bg2_image_resized = cv2.resize(
        bg2_image, (bg1_image.shape[1], bg1_image.shape[0]))
    ob_image_resized = cv2.resize(
        ob_image, (bg1_image.shape[1], bg1_image.shape[0]))

    difference_single_channel = compute_difference(bg1_image, ob_image_resized)
    binary_mask = compute_binary_mask(difference_single_channel)
    output = np.where(binary_mask[:, :, np.newaxis]
                      == 255, ob_image_resized, bg2_image_resized)
    return output


def main():
    # Load the images
    bg1_image = cv2.imread('Module_2/Week_2/Image_data/GreenBackground.png')
    bg2_image = cv2.imread('Module_2/Week_2/Image_data/NewBackground.jpg')
    ob_image = cv2.imread('Module_2/Week_2/Image_data/Object.png')
    # Check if images are loaded successfully
    if bg1_image is None or bg2_image is None or ob_image is None:
        print("Error: Unable to load one or more images.")
        return

    # Perform background subtraction and replacement
    result = replace_background(bg1_image, bg2_image, ob_image)

    # Display the results
    cv2.imshow('Original Object', ob_image)
    cv2.imshow('New Background', bg2_image)
    cv2.imshow('Result', result)

    # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally, save the result
    cv2.imwrite('Result.png', result)


if __name__ == "__main__":
    main()
