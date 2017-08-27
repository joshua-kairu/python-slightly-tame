def do_four ( f, value ):
    do_twice( f, value )
    do_twice( f, value )

def do_twice( f, value ):
    f( value )
    f( value )
    
def print_twice( s ):
    print ( s )
    print ( s )

do_four( print_twice, "spam" )

