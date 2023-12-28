import pygame

import queue
import threading
from .socket import retrieve_events



def main():
    pygame.init()
    q = queue.Queue()

    events = threading.Thread( target = retrieve_events, daemon = True, args = (q,) )
    events.start( )

    screen = pygame.display.set_mode( ( 1280,720 ) )
    text = pygame.font.Font( size = 36 )


    while running:

        for event in pygame.event.get( ):
            if event.type == pygame.QUIT: running = False

        screen.fill( 0 )
        if not q.empty( ): e = q.get( )

        if e:
            name = e["name"]; msg = e["msg"]

            txt = text.render( f"{ name }: { message }", 0, ( 255,255,255 ) )
            screen.blit( txt, ( 30,480 ) )


        pygame.display.flip( )



if __name__ == "__main__":
    main( )
