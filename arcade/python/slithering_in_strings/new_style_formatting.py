def newStyleFormatting(s):
    """
    return new-style string formatting syntax
    -----------------------------------------
    Parameters:
    -----------------------------------------
    s - string -- formatted in old-style string formatting syntax
        
    >>> newStyleFormatting("We expect the %f%% growth this week")
    'We expect the {}% growth this week'
    """
    types = ["b", "c", "d", "e", "E", "f", "F", "g",
             "G", "n", "o", "s", "x", "X", "%"]
    new_style_string = ""
    i = 0
    while i < len(s):
        if s[i] == "%":
            if s[i+1] in types:
                if s[i+1] =="%":
                    new_style_string+=s[i]
                else:    
                    new_style_string+="{}"
                i+=2
        else:
            new_style_string+=s[i]
            i+=1

    return new_style_string

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

