def fact(n):
        """assumes n is an integer greater than 0 and returns n!"""
        if n==1:    
            return n
        else:
                return n*fact(n-1)
