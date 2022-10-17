#Juego del ahorcado

#Libreria limpiar pantalla
import os
import random #Generate randoms

def count(x, G):
    word = []
    for i in range(len(x)):
        word.append("_")

    for i in range(len(x)):
        try:
            if x[i] == G[0]:
                word[i] = x[i]
            elif x[i] == G[1]:
                word[i] = x[i]
            elif x[i] == G[2]:
                word[i] = x[i]
            elif x[i] == G[3]:
                word[i] = x[i]
            elif x[i] == G[4]:
                word[i] = x[i]
            elif x[i] == G[5]:
                word[i] = x[i]
            elif x[i] == G[6]:
                word[i] = x[i]
            elif x[i] == G[7]:
                word[i] = x[i]
            elif x[i] == G[8]:
                word[i] = x[i]
            elif x[i] == G[9]:
                word[i] = x[i]
            elif x[i] == G[10]:
                word[i] = x[i]
            elif x[i] == G[11]:
                word[i] = x[i]
            elif x[i] == G[12]:
                word[i] = x[i]
            elif x[i] == G[13]:
                word[i] = x[i]
            elif x[i] == G[14]:
                word[i] = x[i]
            elif x[i] == G[15]:
                word[i] = x[i]
            elif x[i] == G[16]:
                word[i] = x[i]
            elif x[i] == G[17]:
                word[i] = x[i]
            elif x[i] == G[18]:
                word[i] = x[i]
            elif x[i] == G[19]:
                word[i] = x[i]
            elif x[i] == G[20]:
                word[i] = x[i]
            elif x[i] == G[21]:
                word[i] = x[i]
            elif x[i] == G[22]:
                word[i] = x[i]
            elif x[i] == G[23]:
                word[i] = x[i]
            elif x[i] == G[24]:
                word[i] = x[i]
            elif x[i] == G[25]:
                word[i] = x[i]
            elif x[i] == G[26]:
                word[i] = x[i]
            elif x[i] == G[27]:
                word[i] = x[i]
        except:
            pass

    return word

def eval(x):
    word = [] #Palabra a mostrar
    G = [] #Letras adivinadas hasta ahora
    li = [] #Lista de cada letra

    for i in range(len(x)):
        word.append("_")
    
    for i in range(len(x)):
        li.append(x[i])

    while word != li:
        os.system("cls") #clear
        print("¡Adivina la palabra!")

        g = ""
        for i in range(len(word)):
            g = g + word[i] + " "
        print(g)


        guess = str(input("Ingresa una letra: "))
        G.append(guess)
        word = count(x, G)
    
    os.system("cls") #clear
    print(x)



def run():
    #Read Data
    with open("./archivos/data.txt", "r", encoding = "utf-8") as f: 
        words = [line.replace('\n', '') for line in f] #Replace \n and add to list
    n = random.randint(0, len(words)-1)
    eval(words[n])


if __name__ == '__main__':
    os.system("cls") #clear
    run()
    print("You won!!")