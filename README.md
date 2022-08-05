# stockholm
Ransomeware por motivos educativos

Como utilizar el programa:

- A lo mejor tienes que instalar el modulo cryptography para python. El comando "pip install cryptography" deberia de solucionar este posible problema. Ya es feo pedirte que te instales tu el algoritmo con el que secuestrarte los datos. Hare un script bonito que instale todo y luego ejecute el punto py.

- Ve a la carpeta donde hayas descargado el archivo y ejecuta el comando "python3 stockholm.py" (Hay varias opciones a la hora de ejecutarlo, se recomienda ejecutar antes "python3 stockholm.py -h" y echarle un vistazo a la maravillosa ayuda que aporta)

Es importante que exista el directorio /home/infection, si no, nada de esto va a funcionar (gracias a Dios), dado que es una prueba y no queremos encriptar nada de utilidad. Para poder vivir la experiencia plena, deberia haber algun archivo dentro de esta carpeta o en sus subcarpetas con contenido para poder ser encriptado. En el repositorio se incluye una carpeta llamada infection con el material con el que se hicieron las pruebas durante el proceso por si pudiese ser de utilidad. 

El propio programa (stocholm.py) va a crear un archivo, en la carpeta en la que se encuentre, con el nombre ".claves.key". esto por supuesto no es para nada eficiente en cuanto a dejar la clave usada para encriptar la informacion si la intencion fuese pedir algun tipo de rescate por los datos, pero es una medida de seguridad para esta prueba y tambien es una forma de almacenar la relacion de "usuario infectado/clave usada". En un futuro cuando quiera infectar a alguien de verdad la idea es ir acumulando esta informacion en un sitio que no sea accesible para nadie excepto para mi. Aunque no sea para nada eficiente no he podido resistirme a hacerla oculta, asi que si de primeras no la ves no te asustes, aunque el proceso de desencriptado lee automaticamente el fichero, pero por si quieres cotillear el archivo.