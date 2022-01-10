# InstaBot!(Request remover) v12.1
# Programmer : Mohammadreza.D
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Python Version : 3.9.9
# Selenium Version : 4.0.0
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Developer name : *_* Every Developer *_*
# Github >>> https://github.com/Every-Developer/InstagramBot
# _________________________________________________________#

from selenium import webdriver

# from User_Password import User_name,  Password

from time import sleep

User_name = input('Enter your Username or Email : ')
Password  = input('Enter Password : ')


# YOUR REQUESTED IDs
try:
    ids_file = open('All User IDs.txt', encoding="utf-8")
    All_ids = str(ids_file.read())
    ids_file.close()

except FileNotFoundError:

    with open('All User IDs.txt', 'w') as ids_file:

        All_ids = ''
        ids_file.write(str(All_ids))

# ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^

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

        
        try:

            # Current Follow REQUESTS
            self.driver.get('https://www.instagram.com/accounts/access_tool/current_follow_requests')

            sleep(2)


        except Exception:
            
            try:
                
                Pin_Error = self.driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')

                print('''Sorry, your Username or password was X_X incorrect X_X.Please double-check your user/pass.''')
                
                sleep(10)
                quit()

            except Exception:
                
                print('''Address bar not found *__* 
                    Please run the robot again (Unable to locate element)''')
                sleep(10)
                quit()

        # >"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<>"<
        
       
        # Click on *view more*
        Num_Click = 0
        Selector = True

        try:

            while Selector == True:

                View_more = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/main/button')
                View_more.click()

                sleep(1)
                Num_Click += 1

        except Exception:

            Selector = False
            

        Accounts_list = []
        
        
        if All_ids == '':
            
            Class_name = self.driver.find_elements_by_class_name('-utLf')

            for accounts in Class_name:

                Accounts_list.append(accounts.text)

            # print('File is empty')

        else:
            with open('All User IDs.txt', encoding="utf-8") as ids_file:

                for accounts in ids_file:
                    Accounts_list.append(accounts.strip())

            # print('User included in the file')


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
