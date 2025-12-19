# DEPURACIÓN DEL CÓDIGO

---

En un primer intento voy a tratar de ejecutar el código de forma normal, simplemente dandole al botón de arriba a la izquierda en VS Code.

![ejecuccion-fallo](/imgs/run&debug/ejecuccion-fallo.png)

Como se puede apreciar en la consola de salida, el programa funciona hasta cierto momento en el que este nos avisa de un error entonces lo siguiente que debemos hacer es ejecutar una **depuración del código**, en este caso no necesitamos un **breakpoint** ya que al dar un error de ejecucción el programa parará en el momento exacto en el que sucede.

Para ejecutar una depuración en VS Code podemos apreciar que hay una pestañita para desplegar al lado del botón de ejecucción , dentro de ese menú encontraremos la opción de depurar el código.

![boton](/imgs/run&debug/btn.png)

O también en el menú del lateral izquierdo tendremos un apartado para ejecutar y depurar nuesto código.

![debug](/imgs/run&debug/debug.png)

Como se puede apreciar , nos salta el mismo error, este dicta que nos falta el parametro *encerado* al llamar al método *"ejecutarSimulación"*, asi que una vez añadamos ese parametro en `false` como especifica el comentario, el programa debería funcionar a las mil maravillas.

![ejecuccion-correcto](/imgs/run&debug/ejecuccion-correcto.png)



