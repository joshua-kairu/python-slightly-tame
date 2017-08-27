def right_justify( s ):
    length = len( s )
    remainder = 70 - length
    print ( " " * remainder, s )
    
right_justify( "allen" )
