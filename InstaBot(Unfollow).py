# InstaBot!(Request remover)
# Programmer : Mohammadreza.D
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Python Version : 3.9.6
# Selenium Version : 21.1.2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Company Name : *_* Every Developer *_*
# Github >>> https://github.com/Every-Developer
# _________________________________________________________#

from selenium import webdriver

from User_Password import User_name, Password

import time



class Bot():

    def __init__(self):

        self.Login(User_name, Password)

    
    def Login(self, User, Pin):

        self.driver = webdriver.Edge()
        
        self.driver.get('https://www.instagram.com')
        time.sleep(2)
        
        # Username input
        User_Box = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        User_Box.send_keys(User)

        time.sleep(2)

        # Password input
        Pin_Box = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        Pin_Box.send_keys(Pin)

        time.sleep(1)

        # Sigh_in Button
        Login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        Login.click()

        time.sleep(5)
        
        # All Requests
        self.driver.get('https://www.instagram.com/accounts/access_tool/current_follow_requests')

        time.sleep(2)

        # Click on *view more*
        # View_more = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/main/button')
        # View_more.click()

        Accounts_list = []
        
        Class_name = self.driver.find_elements_by_class_name('-utLf')

        
        for accounts in Class_name:

            Accounts_list.append(accounts.text)

        # print(Accounts_list)

        time.sleep(2)

        
        for id_address in Accounts_list:

            self.driver.get(f'https://www.instagram.com/{id_address}/')
            time.sleep(1)

            # REQUESTED button
            Requested = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button')
            Requested.click()

            time.sleep(1)

            # Unfollowing user requested
            Unfollow = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]')
            Unfollow.click()

            time.sleep(2)


def main():

    My_instaBot = Bot()


if __name__ == '__main__':

    main()

# I hope you enjoyed the codes😍