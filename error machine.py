import sys
import pygame
def run():
    def finalcode():
        print('type linux_interaction()')
        xvb = str(input())
        if xvb == 'linux_interaction()':
            try:
                linux_interaction()
            except AssertionError as error:
                print(error)
                print('So close!')
                pygame.time.wait(1000)
                print('Restart? y/n')
                sd = str(input())
                if sd == 'y':
                    run()
                elif sd == 'n':
                    print('Quitting...')
            pygame.time.wait(2000)
            print('.')
            pygame.time.wait(500)
            print('..')
            pygame.time.wait(500)
            print('...')
            pygame.time.wait(1000)
            print('.')
            pygame.time.wait(500)
            print('..')
            pygame.time.wait(500)
            print('...')
            pygame.time.wait(1000)
            print('.')
            pygame.time.wait(500)
            print('..')
            pygame.time.wait(500)
            print('...')
            pygame.time.wait(500)
                    
        elif xvb != 'linux_interaction()':
            print('You won!')
            pygame.time.wait(2000)
            print('Quitting...')
            pygame.time.wait(2000)
            print('.')
            pygame.time.wait(500)
            print('..')
            pygame.time.wait(500)
            print('...')
            pygame.time.wait(1000)
            print('.')
            pygame.time.wait(500)
            print('..')
            pygame.time.wait(500)
            print('...')
            pygame.time.wait(1000)
            print('.')
            pygame.time.wait(500)
            print('..')
            pygame.time.wait(500)
            print('...')
            pygame.time.wait(500)
            
    def linux_interaction():
        assert('linux' in sys.platform), 'cannot execute command on current sys.platform'


    def nextcode():
        f = str(input('Run code? y/n '))
        if f == 'y':
            assert ('linux' in sys.platform), "Cannot run on current sys.platform"
        elif f == 'n':
            print('passed 2/3 of the test')
            finalcode()


    c = int(input('Input number more than 5 or less than 0: '))
    if c > 5 or c < 0:
        raise ValueError('Cannot exceed 5')
    else:
        print('passed 1/3 of the test')
        nextcode()
    
run()

        
        

