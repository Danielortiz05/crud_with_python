

PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('Cuál es la contrasena? ')
        
        if password == PASSWORD:
            return func()
        else: 
            print('La contrasena no es correcta')
            
    return wrapper


@password_required
def needs_password():
    print('La contrasena es correcta')
    

def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        return result.upper()
    
    return wrapper


@upper
def say_my_name(name):
    return f'Hola {name}'

if __name__ == '__main__':
    needs_password()
    print(say_my_name('Daniel'))
