import pygame, sys
from pygame import mixer
mixer.init()

def terminate():
    pygame.quit()
    sys.exit()

def rego():
    print("Resetting...")
    mixer.stop()
    menu()

def menu():
    print('Choose between various azazal songs')
    print('1 = The Meowchine')
    print('2 = Meowter Space')
    print('3 = Paws And Play')
    print('4 = Whisker')
    songs = ["mp3d.mp3", "meowterspace.mp3", "pawsandplay.mp3", "whisker.mp3"]
    x = int(input('Song: '))

    
    mixer.music.load(songs[x - 1])
    songplay = str(input('Looped? y/n '))
    if songplay == 'y':
        print('Playing')
        mixer.music.play(-1)
        pygame.time.wait(30000)
        mixer.music.pause()
        print('Choose again? y/n')
        xf = str(input())

        if xf == 'y':
            rego()
        elif xf == 'n':
            print('Continue? y/n')
            xg = str(input())
            if xg == 'y':
                mixer.music.unpause()
                an = (mixer.music.get_length() - mixer.music.get_pos * -1)
                pygame.time.wait(an)
                print('1 repitition over. Break loop and reset? y/n')
                xv = str(input())
                if xv == 'y':
                    rego()
            elif xg == 'n':
               terminate()

        mixer.music.play(-1)
    elif songplay == 'n':
        print('Playing')
        mixer.music.play()
        pygame.time.wait(30000)
        mixer.music.pause()
        print('Choose again? y/n')
        xf = str(input())

        if xf == 'y':
            rego()
        elif xf == 'n':
            print('Continue? y/n')
            xg = str(input())
            if xg == 'y':
                mixer.music.unpause()
                an = (mixer.music.get_length() - mixer.music.get_pos * -1)
                pygame.time.wait(an)
                print('Song over. Reset? y/n')
                xv = str(input())
                if xv == 'y':
                    rego()
            elif xg == 'n':
                terminate()

    
        


menu()


