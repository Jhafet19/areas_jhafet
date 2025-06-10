while True:
    print('Elige un area la cualcalcular: ')
    print('1. cuadrado')
    print('2. rectangulo')
    print('3. circulo')
    print('4. triangulo')
    figura=input()
    if figura=='1':
        lado=input('Dame la medidad de un lado del cuadrado: ')
        print(f'El area de tu figura es: {lado*lado} ')
    if figura=='2':
        altura=input('Dame la medidad de la altura del rectangulo: ')
        base=input('Dame la medidad de la base del rectangulo: ')
        print(f'El area de tu figura es: {altura*base} ')
    if figura=='3':
        altura=input('Dame la medidad de la altura del triangulo: ')
        base=input('Dame la medidad de la base del triangulo: ')
        print(f'El area de tu figura es: {(altura*base)/2} ')
    if figura=='4':
        radio=input('Dame la medidad del  radio de tu circulo: ')
        print(f'El area de tu figura es: {radio*radio*3.14} ')