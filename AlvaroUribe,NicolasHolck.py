# Proyecto Calfún's Planet
#Alumnos: Alvaro Uribe y Nicolas Holck
# Importando la función
import random;

# Variables
me_quiere = random.randint(1, 15);
ultimo_mensaje = "";

print("\n.::¡Bienvenido a Calfún's Planet THE GAME!::.\n");
#Preguntamos al usuario si quiere jugar o no
respuesta = input("¿Quieres jugar? (s/n): ");
#ejecutamos un if si el usuario indica que quiere jugar
if respuesta.lower() == ("s"):
    print("OK, ¡Jugemos!");
    for i in range(me_quiere):
        if i % 3 == 0:
            ultimo_mensaje = ("Me quiere nada");
            print(ultimo_mensaje);
        elif i % 3 == 1:
            ultimo_mensaje = ("Me quiere poquito");
            print(ultimo_mensaje);
        else:
            ultimo_mensaje = ("Me quiere mucho");
            print(ultimo_mensaje);
    
    # printear el mensaje  basado en el último texto random 
    if ultimo_mensaje == ("Me quiere mucho"):
        print("\nFelicidades, ¡¡¡Te Quieren Mucho!!!");
        print("Mucho!!!");
        print("Mucho!!!\n");
    elif ultimo_mensaje == ("Me quiere poquito"):
        print("\nÁnimo, te quiere poquito :/");
    else:
        print("\npobrecito, parece que no te quiere nada :c.");
#imprimimos este mensaje si el usuario indica que no quiere jugar
elif respuesta.lower() == ("n"):
    print("Vaya, nos vemos para la próxima :,V");
#mensaje de error por si indica un caracter no valido
else:
    print("ERROR, elija 's' o 'n'...");