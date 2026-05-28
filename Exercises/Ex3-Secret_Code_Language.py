# Secret Code Language
# Rules:
# Remove the first letter and add it at the end
# Then add three random letters at the start
# Step 1 :- Coding
# Step 2 :- Decoding
import random
import string

def Encode(message):
    global en_mes
    words = message.split()
    en_mes_lst = []
    for word in words:
        tp_word = word[1:] + word[0]
        random_letters = random.choices(string.ascii_letters, k=3)
        tp_word = "".join(random_letters) + tp_word
        en_mes_lst.append(tp_word)
    en_mes = " ".join(en_mes_lst)
    print(f"Your Encoded Message is : {en_mes}")
    opt = input("Do you want to decode this Message (Y/N): ").upper()
    if opt == 'Y':
        Decode(en_mes)
    else:
        Start()


def Decode(message):
    global de_mes
    words = message.split()
    de_mes_lst = []
    for word in words :
        tp_word = word[-1] + word[3:-1]
        de_mes_lst.append(tp_word)
    de_mes = " ".join(de_mes_lst)
    print(f"Your Decoded Message is : {de_mes}")
    opt = input("DO You Want to Encode this Message (Y/N): ").upper()
    if opt == 'Y':
        Encode(de_mes)
    else:
        Start()

def Encode_Input():
    global mes
    mes = input("Enter Your Message: ")
    Encode(mes)

def Decode_Input():
    global mes
    mes = input("Enter Your Encoded Message: ")
    Decode(mes)

def Start():
    while True:
        task = input("Type 'Encode' for encoding message OR Type 'Decode' for decoding message OR Type 'Quit' to quit : ").strip().capitalize()
        if task == 'Encode':
            Encode_Input()
            break
        elif task == 'Decode':
            Decode_Input()
            break
        elif task == 'Quit':
            break
        else :
            print("Wrong Input...")
    return 1

Start()