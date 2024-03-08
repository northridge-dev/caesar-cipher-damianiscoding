#!/usr/bin/env python

#this turns the order of the letter to the actually letter
def turn_num_to_letter(letter):
    letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','','','','','','','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter -= 65
    letter = letter_list[letter]
    return letter


def decrypt(ciphertext, shift=0):
    #seperating characters
    ciphertext_list = [*ciphertext]

    #shifting letters
    ciphertext2 = ""
    new_list = []
    counter = 0
    for i in range(len(ciphertext_list)):
        letter = ord(ciphertext_list[counter])
        #If upper case
        if letter >= 65 and letter <= 90:
            letter -= shift
            while letter < 65:
                letter += 26
            while letter > 90:
                letter -= 26
            letter = turn_num_to_letter(letter)
        #If lowercase   
        elif letter >= 97 and letter <= 122:
            letter -= shift
            while letter < 97:
                letter += 26
            while letter > 122:
                letter -= 26
            letter = turn_num_to_letter(letter)
        else:
            letter = ciphertext_list[counter]
        new_list.append(letter)
        counter += 1
    
    #make new decrypt
    ciphertext2 = ciphertext2.join(new_list)

    """
    Decrypts a Caesar cipher encrypted message.
    :param ciphertext: The message to be encrypted
    :param shift: The number of positions to shift each letter
    """
    return ciphertext2


if __name__ == "__main__":
    ciphertext = input("Message to decrypt: ")
    shift = int(input("Shift: "))
    print(decrypt(ciphertext, shift))
