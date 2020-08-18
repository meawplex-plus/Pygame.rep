import pygame, sys
from pygame.locals import*
from pygame import mixer

mixer.init()
pygame.init()



def quit():
    pygame.quit()
    sys.exit()




def play():
    c = mixer.Sound('creepysound.wav')
    print('Invoke a spirit')
    pygame.time.wait(1000)
    print('1 = Tartarus - Monsters more powerful, health higher - WIP do not use')
    pygame.time.wait(1000)
    print('2 = Aeolus - Wind speed higher, but less monster health')
    pygame.time.wait(1000)
    cv = int(input())
    print("Okay! With your spirit chosen, let's...")
    pygame.time.wait(1000)
    print('Beee....')
    pygame.time.wait(1000)
    print('...gin!')
    c.play()
    pygame.time.wait(3000)
    if cv == 2:
        aeolusplay()
    elif cv == 1:
        tartarusplay()


print('WARNING: This game has lots of creepy sounds. \
NOT FOR THE FAINT-HEARTED!')
pygame.time.wait(2000)


def backstory():
    a = mixer.Sound('horror.wav')
    print('Skip to menu? y/n')
    rhg = str(input())
    if rhg == 'y':
        titlescreen()
    elif rhg == 'n':
        pass

    a.play()
    pygame.time.wait(4000)
    print('It was...')
    pygame.time.wait(2000)
    print('It was... but... how...?')
    pygame.time.wait(4000)
    print("You're okay, bud. That explosion knocked you unconscious!")
    pygame.time.wait(3000)
    print('And so the game begins...')
    pygame.time.wait(1000)
    a.stop()
    pygame.time.wait(1000)


def titlescreenorigin():
    backstory()
    channel1 = mixer.Channel(0)
    channel1.play(mixer.Sound('bell.wav'), loops=-1)
    mixer.music.load('raven.mp3')
    mixer.music.play(-1)
    c = input('Welcome to The 20 Horrors. Play? y/n ')
    if str(c) == "y":
        mixer.music.fadeout(1000)
        channel1.fadeout(1000)
        pygame.time.wait(2000)
        play()
    elif str(c) == 'n':
        mixer.music.fadeout(500)
        channel1.fadeout(500)
        print('Okay! Type play() to play, backstory() to start backstory over, \
        quit() to quit')


def aeolusplay():
    dfg = ('open sky.')
    dfh = ('snow on your boots.')
    dfj = ('a tall cliff rising above your head.')
    dfl = ('a snowy, icy trail ahead of you.')
    dfk = ('a valley covered in snow. you look to see if anything is there, \
    but there are no signs of civilization.')

    chosen = False

    def hikeChoice():
        print('You see ' + dfl + ' Would you like to hike the trail? y/n')
        hikeChoice = str(input())
        if hikeChoice == 'y':
            print('You set off on the trail.')
            chosen = True
        elif hikeChoice == 'n':
            aeoluscommand()

    def TorF():
        if not chosen:
            aeoluscommand()

    def aeoluscommand():
        aeolus = str(input())
        if aeolus == 'look up':
            print('You see ' + dfg)
        elif aeolus == 'look down':
            print('You see ' + dfh)
        elif aeolus == 'look left':
            print('You see ' + dfj)
        elif aeolus == 'look right':
            print('You see ' + dfk)
        elif aeolus == 'look forward':
            hikeChoice()
        elif aeolus == 'title screen':
            titlescreen()

    aeolusfx = mixer.Sound('wind.wav')
    aeolusfx.play()
    pygame.time.wait(6000)
    aeolusfx.fadeout(2000)
    pygame.time.wait(2000)
    print('You wake up to a cold, windy, environment.')
    pygame.time.wait(2000)
    print('The area looks vaguely familiar, a "deja vu" you might call it.')
    pygame.time.wait(3000)
    print('"Anyone?" you shout, but it is so windy even you can'+"'"+'t hear \
    your shout.')
    pygame.time.wait(4000)
    print('What wil you do? Type title screen to return to title screen')
    print("Type look <direction up, down, left, right, forward>\
     to look around")
    print('Type inspect <itemName> to inspect objects (e.g. inspect drawer)')
    aeoluscommand()
    while True:
        TorF()


def tartarusplay():
    tartarusfx = mixer.Sound('tartarusnoise.wav')
    mixer.music.load('hauntedpit.mp3')
    tartarusfx.play()
    mixer.music.play()
    mixer.music.set_volume(50)
    pygame.time.wait(6000)
    tartarusfx.fadeout(2000)
    mixer.music.fadeout(2000)
    pygame.time.wait(2000)
    print('You wake up to a creepy pit full of darkness.')
    pygame.time.wait(2000)
    print('Monsters prowl the area, you have no memory of being here.')
    pygame.time.wait(4000)
    print('"Hello?" you shout, no answer.')


def titlescreen():
    pygame.time.wait(1000)
    channel1 = mixer.Channel(0)
    channel1.play(mixer.Sound('bell.wav'), loops=-1)
    mixer.music.load('raven.mp3')
    mixer.music.play(-1)
    c = input('Welcome to The 20 Horrors. Play? y/n ')
    if str(c) == "y":
        mixer.music.fadeout(1000)
        channel1.fadeout(1000)
        pygame.time.wait(2000)
        play()
    elif str(c) == 'n':
        mixer.music.fadeout(500)
        channel1.fadeout(500)
        print('Okay! Type play() to play, backstory() to start backstory over,\
         quit to quit')


titlescreenorigin()
