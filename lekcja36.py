#argumenty funkcji lista parametrow

def funkcja(arg1, arg2 ="world", *args, **kwargs):
    print(arg1, arg2, len(args), kwargs)
    for x in args:
        print(x)
    for x in kwargs.values():
        print(x)
        
funkcja("Hello")
funkcja("hi", "YouTube")
funkcja("hi", "YouTube", "!", ":-)", autor="Mateusz", rok=2023)

print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)