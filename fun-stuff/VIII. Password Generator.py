import re
import secrets
import string
import time
import pyperclip as pc


def main():

    def copy2clip(txt):
        cmd='echo '+txt.strip()+'|clip'
        return subprocess.check_call(cmd, shell=True)

    def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

        # Define the possible characters for the password
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        # Combine all characters
        all_characters = letters + digits + symbols

        while True:
            password = ''
            # Generate password
            for _ in range(length):
                password += secrets.choice(all_characters)
            
            constraints = [
                (nums, r'\d'),
                (special_chars, fr'[{symbols}]'),
                (uppercase, r'[A-Z]'),
                (lowercase, r'[a-z]')
            ]

            # Check constraints        
            if all(
                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints
            ):
                break

        return password
    
    #Outputs the password
    print('Generated Password:', generate_password())
    #Ask the user if they want to generate a new password
    while True:
        #Waits before shoping the prompt
        time.sleep(1)
        restart = str(input('Generate a new password? y/n\n').lower())
        #If the answer is 'y' it outputs another newly generated password
        if restart == 'y':
            print('\nNew password:', generate_password())

            #time.sleep(.5)
            #print('Password has been copied to clipboard')

        ##If the answer is 'n' the script stops
        else:
            print('Exiting the script...')
            break

main()




        

