a=55
match a:
    case a if a>90:
        print("A")
    case a  if a<90:
        print("B")
    case _:
        print("C")

