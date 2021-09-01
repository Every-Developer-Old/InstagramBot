# InstaBot!(Request remover) V11.0-beta
# Programmer : Mohammadreza.D
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Python Version : 3.9.6
# Selenium Version : 21.2.4
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Developer name : *_* Every Developer *_*
# Github >>> https://github.com/Every-Developer/InstagramBot
# _________________________________________________________#

from selenium import webdriver

# from User_Password import User_name,  Password

from time import sleep

User_name = input('Enter your Username or Email : ')
Password  = input('Enter Password : ')



class Bot():

    def __init__(self):

        self.Login(User_name, Password)

    
    def Login(self, User, Pin):

        self.driver = webdriver.Edge()

        self.driver.get('https://www.instagram.com')
        sleep(2)

        # ¬_¬ ¬_¬ ¬_¬ ¬_¬ ¬_¬ ¬_¬ ¬_¬ ¬_¬ ¬_¬ ¬_¬ ¬_¬ ¬_¬ ¬_¬ ¬_¬ ¬_¬ ¬_¬

        # Username input
        User_Box = self.driver.find_element_by_xpath(
                    '//*[@id="loginForm"]/div/div[1]/div/label/input')
        User_Box.send_keys(User)

        sleep(1)

        # Password input
        Pin_Box = self.driver.find_element_by_xpath(
                    '//*[@id="loginForm"]/div/div[2]/div/label/input')
        Pin_Box.send_keys(Pin)

        sleep(1)

        # Sigh_in Button
        Login = self.driver.find_element_by_xpath(
                    '//*[@id="loginForm"]/div/div[3]')
        Login.click()

        sleep(5)


        # ^_____^ ^_____^ ^_____^ ^_____^ ^_____^ ^_____^ ^_____^ ^_____^ ^_____^ ^_____^

        try:

            # Profile button
            Profile = self.driver.find_element_by_class_name('_6q-tv')
            Profile.click()

            sleep(1.5)

        except Exception:

            try:
                Pin_Error = self.driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')

                print('''Sorry, your Username or password was X_X incorrect X_X.Please double-check your user/pass.''')
                
                sleep(10)
                quit()

            except Exception:
                
                print('''Profile button not found *__* 
                    Please run the robot again (Unable to locate element)''')
                sleep(10)
                quit()

        # >"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<
    
        # Open Setting
        self.driver.get('https://www.instagram.com/accounts/edit/')

        sleep(2.5)


        # Privacy & Security
        Privacy = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/ul/li[7]/a').click()

        sleep(2.5)

        # View Account data
        Account_data = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/main/section[6]/a').click()

        sleep(2.5)

        # Current follow requests
        Requests = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/main/div/div[2]/section[1]/section[1]/a').click()

        sleep(1)

        # Number click on *view more*
        Num_Click = 0
        
        # pay attention! This number can vary depending on your needs
        # For example, I needed to click the View More button 5 times. You may need to click the button 10 times

        # while Num_Click <= 5:

        #     View_more = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/main/button')
        #     View_more.click()

        #     sleep(2)
        #     Num_Click += 1
            

        Accounts_list = []
        
            
        Class_name = self.driver.find_elements_by_class_name('-utLf')

        for accounts in Class_name:

            Accounts_list.append(accounts.text)

        # print(Accounts_list)

        sleep(2)

        
        for id_address in Accounts_list:

            self.driver.get(f'https://www.instagram.com/{id_address}/')
            sleep(1)

            # REQUESTED button
            Requested = self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button')
            Requested.click()

            sleep(2)

            # Unfollowing user requested
            Unfollow = self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div/div[3]/button[1]')
            Unfollow.click()

            sleep(2)


def Request_remover():

    My_instaBot = Bot()


if __name__ == '__main__':

    Request_remover()

# THE END OF CODE
# I hope the program works properly😊