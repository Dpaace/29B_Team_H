class RegisterPage:
    txt_username_id = "rusername"
    txt_firstname_id = "rfirstname"
    txt_lastname_id = "rlastname"
    txt_email_id = "remail"
    txt_password_id = "rpassword"
    txt_conpassword_id = "cpassword"
    btn_register_xpath = '//*[@id="home"]/main/div[2]/div/div[1]/form[2]/div[2]/input'



    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_id(self.txt_username_id).send_keys(username)

    def setfirstname(self, name):
        self.driver.find_element_by_id(self.txt_firstname_id).send_keys(name)

    def setlastname(self, lastname):
        self.driver.find_element_by_id(self.txt_lastname_id).send_keys(lastname)

    def setemail(self, email):
        self.driver.find_element_by_id(self.txt_email_id).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)

    def setconpassword(self, cpassword):
        self.driver.find_element_by_id(self.txt_conpassword_id).send_keys(cpassword)

    def clickOnRegister(self):
        self.driver.find_element_by_xpath(self.btn_register_xpath).click()