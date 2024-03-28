
class WindowManager:
    __running = True

    @property
    def running(self):
        return self.__running

    def quit(self):
        self.__running = False
