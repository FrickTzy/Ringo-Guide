from pygame import image, transform, draw, mouse


class LessonWindowBackground:
    __IMAGE_PATH = "Frontend/Utils/Files/Images/lesson_window_background.jpg"
    __current_background_image = None

    def __init__(self, window_size):
        self.__background_image = image.load(self.__IMAGE_PATH)
        self.__corner = Corner(window_size=window_size)
        self.update_size(window_size=window_size)

    def show(self, screen):
        self.__corner.show(background_image=self.__current_background_image)
        screen.blit(self.__current_background_image, (0, 0))

    def check_if_click(self):
        return self.__corner.check_if_click(mouse_pos=mouse.get_pos())

    def update_size(self, window_size):
        self.__corner.update_size(window_size=window_size)
        self.__current_background_image = transform.scale(self.__background_image, window_size)


class Corner:
    __COLOR = (196, 10, 0)

    def __init__(self, window_size):
        self.__pos = CornerPos(window_size=window_size)

    def show(self, background_image):
        draw.polygon(background_image, self.__COLOR, self.__pos.left_corner_coordinates)
        draw.polygon(background_image, self.__COLOR, self.__pos.right_corner_coordinates)

    def check_if_click(self, mouse_pos):
        return self.__pos.check_if_click(mouse_pos=mouse_pos)

    def update_size(self, window_size):
        self.__pos.update_size(window_size)


class CornerPos:
    __CORNER_SIZE_RATIO = 4.74

    def __init__(self, window_size):
        self.__window_size = window_size

    def update_size(self, window_size):
        self.__window_size = window_size

    @property
    def left_corner_coordinates(self):
        return [(0, 0), (self.__corner_size, 0), (0, self.__corner_size)]

    @property
    def right_corner_coordinates(self):
        window_width = self.__window_size[0]
        return [(window_width, 0), (window_width-self.__corner_size, 0), (window_width, self.__corner_size)]

    @property
    def __corner_size(self):
        window_height = self.__window_size[1]
        return window_height // self.__CORNER_SIZE_RATIO

    def check_if_click(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        mouse_area = mouse_x + mouse_y
        if mouse_area < self.__corner_size:
            return True
        return False
