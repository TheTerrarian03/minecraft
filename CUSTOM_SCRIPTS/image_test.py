import pyautogui
import time
import os

def get_button_image_paths(folder_path):
    image_paths = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            image_paths.append(image_path)

    return image_paths

def click_green_play_button():
    # Find the coordinates of the green play button
    image_paths = get_button_image_paths("mc_play_buttons")
    print(image_paths)

    for image in image_paths:
        print(image)
        button_position = pyautogui.locateOnScreen(image, confidence=0.9)
        if button_position is not None:
            break

    if button_position is None:
        print("Button not found")
        return

    # Calculate the center of the button
    button_x, button_y, button_width, button_height = button_position
    button_center_x = button_x + button_width // 2
    button_center_y = button_y + button_height // 2

    # Move the mouse to the button and click it
    pyautogui.moveTo(button_center_x, button_center_y)
    pyautogui.click()

if __name__ == '__main__':
    # Wait for the user to switch to the target program
    time.sleep(2)  # Adjust the delay as needed

    # Click the green play button
    click_green_play_button()