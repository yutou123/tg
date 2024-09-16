from logs import *
import pyautogui,time
class pinaMnia(object):
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    #长按重复函数
    def longPressMouse(self,repeat=100, press_time=3):
        """
        模拟鼠标长按动作的函数。
        :param repeat: 长按重复的次数，默认为100次。
        :param press_time: 每次长按的时间（秒），默认为3秒。
        """
        for i in range(repeat):
            x, y = pyautogui.position()
            log.info(f"当前鼠标位置：({x}, {y})")
            if x != self.x:
                log.info(f"鼠标位置和设置的位置不一致 将关闭脚本")
                break
            time.sleep(2)
            log.info(f"按下鼠标 {i}")
            pyautogui.mouseDown()
            time.sleep(press_time)
            pyautogui.mouseUp()
            log.info(f"释放鼠标 {i}")
            time.sleep(2)
 
    def main(self):
        # 等待3秒，以便你可以将鼠标移动到你想要点击的位置
        time.sleep(3)
        x, y = pyautogui.position()
        log.info(f"当前鼠标位置：({x}, {y})")
        pyautogui.moveTo(self.x, self.y, duration=1)

        #repeat 需要按多少次
        self.longPressMouse(repeat=100, press_time=4)

#获取当前鼠标坐标
def position():
    time.sleep(3)
    x, y = pyautogui.position()
    log.info(f"当前鼠标位置：({x}, {y})")

position() #配置好后这个函数就 注释掉



x,y = 744, 567 #需要长按的屏幕坐标位置
pinaMnia(x,y).main()
