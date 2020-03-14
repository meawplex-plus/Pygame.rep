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
    
    
    mixer.music.load('pawsandplay.mp3')
    mixer.music.load('whisker.mp3')
    x = int(input('Song: '))

    if x == 1:
        mixer.music.load('mp3d.mp3')
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
                    an = mixer.music.get_pos()
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
                    an = mixer.music.get_pos()
                    pygame.time.wait(an)
                    print('Song over. Reset? y/n')
                    xv = str(input())
                    if xv == 'y':
                        rego()
                elif xg == 'n':
                    terminate()

            
    elif x == 2:
        mixer.music.load('meowterspace.mp3')
        songplay1 = str(input('Looped? y/n '))
        if songplay1 == 'y':
            print('Playing')
            mixer.music.play(-1)
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
                    an = mixer.music.get_pos()
                    pygame.time.wait(an)
                    print('1 repitition over. Break loop and reset? y/n')
                    xv = str(input())
                    if xv == 'y':
                        rego()
                elif xg == 'n':
                   terminate()

        elif songplay1 == 'n':
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
                    an = mixer.music.get_pos()
                    pygame.time.wait(an)
                    print('Song over. Reset? y/n')
                    xv = str(input())
                    if xv == 'y':
                        rego()
                elif xg == 'n':
                    terminate()


    elif x == 3:
        mixer.music.load('pawsandplay.mp3')
        songplay2 = str(input('Looped? y/n '))
        if songplay2 == 'y':
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
                    an = mixer.music.get_pos()
                    pygame.time.wait(an)
                    print('1 repitition over. Break loop and reset? y/n')
                    xv = str(input())
                    if xv == 'y':
                        rego()
                elif xg == 'n':
                   terminate()

        elif songplay2 == 'n':
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
                    an = mixer.music.get_pos()
                    pygame.time.wait(an)
                    print('Song over. Reset? y/n')
                    xv = str(input())
                    if xv == 'y':
                        rego()
                elif xg == 'n':
                    terminate()


    elif x == 4:
        mixer.music.load('whisker.mp3')
        songplay3 = str(input('Looped? y/n '))
        if songplay3 == 'y':
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
                    an = mixer.music.get_pos()
                    pygame.time.wait(an)
                    print('1 repitition over. Break loop and reset? y/n')
                    xv = str(input())
                    if xv == 'y':
                        rego()
                elif xg == 'n':
                   terminate()

        elif songplay3 == 'n':
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
                    an = mixer.music.get_pos()
                    pygame.time.wait(an)
                    print('Song over. Reset? y/n')
                    xv = str(input())
                    if xv == 'y':
                        rego()
                elif xg == 'n':
                    terminate()



menu()


