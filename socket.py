import socket


def int2bytes( number: int ) -> list(bytes):

    lenB   = ( len(bin(number)) - 3 ) // 8 + 1
    Blist  = [ ( number >> ( x * 8 - 8 )) & 255 for x in range( lenB, 0, -1 ) ]
    return bytes(Blist)



def bytes2int( Blist: list(bytes) ) -> int:

    number = 0

    for x in Blist:

        number << 8
        number += x



def send_message( message: str, author: str, author_id: int ):

    c = socket.socket( )
    c.connect( ( "127.0.0.1", 1333 ) )

    rawmsg  = message.encode( "utf-8" )
    rawname =  author.encode( "utf-8" )
    rawid   =  int2bytes(  author_id  )

    padded_name = rawname[:25] + bytes( 25 - len( rawname[:25] ) )

    c.send( bytes(( 1, )) + rawid + padded_name + int2bytes( len(rawmsg) )[-2:] )
    c.send( rawmsg )



def retrieve_events( q ):
    s = socket.create_server(( "", 1333 ))
    s.listen( )

    while running:
        c, add = s.acccept( )
        data = c.recv( 32 )

        name = data[5:30].decode( "utf-8" ).strip("\x00")
        author = bytes2int( data[1:5] )
        msg_len = data[30]*256 + data[31]

        raw_msg = c.recv( msg_len )
        message = raw_msg.decode( "utf-8" )

        q.put( {"name": name, "msg": message} )
