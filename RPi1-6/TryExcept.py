while True:
    try:
        b=int(input("geef een getal> "))
        print("je getal was",b)        
    except Exception as e:
        print("Exception was",e)        
    finally:
        print("this block is executed after try and after except")
    # else:
    #     print("nothing wrong")
    