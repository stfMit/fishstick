from PIL import Image, ImageGrab
import numpy as np
import cv2 as cv
import time
from threading import Thread
from fishing.fishing_agent import FishingAgent


class MainAgent:
    def __init__(self) -> None:
        self.agents = []
        self.fishing_thread = None

        self.cur_img = None
        self.cur_imgHSV = None

        self.zone = "Feralas"
        self.time = "night"


def update_screen(agent):
    t0 = time.time()
    while True:
        agent.cur_img = ImageGrab.grab()
        agent.cur_img = np.array(agent.cur_img)
        agent.cur_img = cv.cvtColor(agent.cur_img, cv.COLOR_RGB2BGR)
        agent.cur_imgHSV = cv.cvtColor(agent.cur_img, cv.COLOR_BGR2HSV)

        # cv.imshow("Computer vision", agent.cur_img)
        key = cv.waitKey(1)
        if key == ord('q'):
            break
        ex_time = time.time() - t0
        t0 = time.time()
        time.sleep(5)
        # print("FPS: " + str(1 / ex_time))


def print_menu():
    print("Enter a command:")
    print("\tS\t Start the main agent.")
    print("\tZ\t Set zone.")
    print("\tF\t Start the fishing agent.")
    print("\tQ\t Quit fishingBOT.")


if __name__ == "__main__":
    main_agent = MainAgent()
    print_menu()
    while True:
        user_input = input()
        user_input = str.lower(user_input).strip()
        if user_input == 's':
            update_screen_thread = Thread(
                target=update_screen,
                args=(main_agent,),
                name="update screen thread",
                daemon=True)
            update_screen_thread.start()
        elif user_input == 'z':
            pass
        elif user_input == 'f':
            fishing_agent = FishingAgent(main_agent)
            fishing_agent.run()
        elif user_input == 'q':
            cv.destroyAllWindows()
            break
        else:
            print("Input error.")
            print_menu()
    print("FINISHED")
