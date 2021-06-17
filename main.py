import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from whatsapp_response import response

# Requires opencv-python package for image recognition confidence
# Mouse click workaround for MAC OS
mouse = Controller()
# Instructions for our WhatsApp Bot
class WhatsApp:

    # Defines the starting values
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    # Navigate to the green dots for new messages
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot): ', e)

    #Navigate to our message input box
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_input_box): ', e)
    
    #Navegate to the message we want to respond to
    def nav_message(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, -40, duration=self.speed)  # x,y has to be adjusted depending on your computer
        except Exception as e:
            print('Exception (nav_message): ', e)

    # Copies the message that we want to process
    def get_message(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)
        pt.moveRel(10, 10, duration=self.speed)  # x,y has to be adjusted depending on your computer
        mouse.click(Button.left, 1)
        sleep(1)

        # Gets and processes the message
        self.message = pc.paste()
        print('A mensagem recebida foi: ', self.message)

        #Enviado mensagem para o usuário
    def send_message(self):
        try:
            if self.message != self.last_message:
                bot_response = response(self.message)
                print('You say', bot_response)
                pt.typewrite(bot_response, interval=.1)
                pt.typewrite("\n")

                self.last_message = self.message
            else:
                print("SEM NOVAS MENSAGENS...")
                
        except Exception as e:
            print("Exception (send_message): ",e )

wa_bot = WhatsApp(speed=.5, click_speed=.4)
sleep(2)

while True:
    wa_bot.nav_green_dot()
    wa_bot.nav_message()
    wa_bot.get_message()
    wa_bot.nav_input_box()
    wa_bot.send_message()

    sleep(10)