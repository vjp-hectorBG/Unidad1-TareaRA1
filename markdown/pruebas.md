# Pruebas unitarias

En este documento mi objetivo es realizar en código de python algunas pruebas unitarias y comprobar su resultado, el esquema que seguiré será ir una por una explicando la prueba, si da error y luego explicar el código solucionado con una catura de pantalla.

---

### Prueba 1

```python
    def test1_estado_inicial_correcto(self):
        """Test 1: Verifica que el estado inicial es Inactivo y con 0 ingresos."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)
```
Aquí comprueba que los valores base son los correctos utilizando `assert.

![test1_pass](/imgs/unitest/test1-pass.png)

Como se puede apreciar en la imagen el test1 se pasa sin problema.

---

### Prueba 2

```python
   def test2_excepcion_encerado_sin_secado(self):
        """Test 2: Comprueba que encerar sin secado a mano lanza ValueError."""
        # _hacer_lavado: (Prelavado: False, Secado a mano: False, Encerado: True)
        with self.assertRaises(ValueError):
            self.lavadero.hacerLavado(False, False, True)
```

En este test se comprueba que cuando se va a comenzar la fase de encerar sin haber secado a mano el programa lance un ValueError (En la práctica especifica otro tipo de excepción IllegalArgumentException pero esta al parecer no es un error de python y el que se utilza en python es ValueError), esto se comrpueba con la línea de `assertRaises` la cual comprobará si la excepción es la que esperamos.

![test2_pass](/imgs/unitest/test2-pass.png)

Como se puede ver en la imagen , nos devuelve la excepción que queremos por lo tanto este test también lo pasa.

---

### Prueba 3

```python
def test3_excepcion_lavado_ocupado(self):
        """Test 3: Verifica que intentar lavar cuando el lavadero está ocupado lanza IllegalStateException."""
        self.lavadero.hacerLavado(True, False, False)  # Inicia un lavado
        with self.assertRaises(IllegalStateException):
            self.lavadero.hacerLavado(False, True, False)  # Intenta iniciar otro lavado
```

Como en el anterior buscamos que nos salga el error que especificamos (IllegalStateException).

![test3-fail](/imgs/unitest/test3-fail.png)

¡Vaya! Parece que esta vez no ha pasado el test nuestro código, si analizamos el error vemos que nos levanta otra excepción , por suerte eso tiene facil solución, en el método de `hacerLavado` dentro del primer if debemos cambiar la excepción que levanta a IllegalStateException e importarla.

![test3-fix](/imgs/unitest/test3-fix.png)

Una vez arreglado y guardado nuestro código, comprobamos que esta vez pasa el test.

![test3-pass](/imgs/unitest/test3-pass.png)

---

### Prueba 4

```python
 def test4_prelavadoamano_ingresos_correctos(self):
        """Test 4: Verifica que el prelavado a mano añade 6.5 a los ingresos."""
        self.lavadero.hacerLavado(True, False, False)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 6.5)
```

Este test hace una prueba de un lavado con un prelavado a mano y luego al cobrar verifica que el resultado sea 6.5.

![test4-pass](/imgs/unitest/test4-pass.png)

Como se puede apreciar en la imagen , se ha pasado el test a la primera y si nos fijamos en el código podemos ver que el lavado tiene un precio base de 5 y el prelavado a mano añade 1.5, acabamos de comprobar que nuestro test funciona y que nuestro código lo ha pasado.

---

### Prueba 5

```python
 def test5_secadoamano_ingresos_correctos(self):
        """Test 5: Verifica que el secado a mano añade 6.0 a los ingresos."""
        self.lavadero.hacerLavado(False, True, False)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 6.0)
```

La lógica es la misma que con el test 4 solo que el secado a mano debería dar como resultado 6.

![test5-fail](/imgs/unitest/test5-fail.png)

Falla el test, en la variable se suman 20 ctms más de los que se deberían así que cambio el valor de sumar a 1 en vez de 1.20.

![test5-fix](/imgs/unitest/test5-fix.png)

Y comprobamos que pasa el test.

![test5-pass](/imgs/unitest/test5-pass.png)

---

### Prueba 6

```python
 def test6_secadoamano_y_encerado_ingresos_correctos(self):
        """Test 6: Verifica que el secado a mano y encerado añaden 7.2 a los ingresos."""
        self.lavadero.hacerLavado(False, True, True)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 7.2)
```

Lo mismo pero juntando secado a mano y encerado, los ingresos deberían ser 7.2

![test6-fail](/imgs/unitest/test6-fail.png)

Nos da error ya que cuenta 20 ctms de menos, se arregla cambiando el valor de el encerado y subiendole 0.20.

![test6-fix](/imgs/unitest/test6-fix.png)

Comprobación : 

![test6-pass](/imgs/unitest/test6-pass.png)

---

### Prueba 7

```python
def test7_prelavadoamano_y_secadoamano_ingresos_correctos(self):
        """Test 7: Verifica que el prelavado a mano y secado a mano añaden 7.5 a los ingresos."""
        self.lavadero.hacerLavado(True, True, False)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 7.5)
```
El resultado de esta prueba deberá ser 7.5 ya que junta prelavado a mano y secado a mano.

![test7-pass](/imgs/unitest/test7-pass.png)

Da el resultado correcto ya que con los test anteriores he cambiado los valores para que cuadren.

---

### Prueba 8

```python
 def test8_todas_opciones_ingresos_correctos(self):
        """Test 8: Verifica que todas las opciones añaden 8.7 a los ingresos."""
        self.lavadero.hacerLavado(True, True, True)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 8.7)
```

Este test comprueba que teniendo todas las opciones de lavado activadas de 8.70 euros de ingresos.

![test8-pass](/imgs/unitest/test8-pass.png)

Como en el test anterior este da la cantidad correcta porque hemos modificado las variables anteriormente.

---

### Prueba 9

```python
 def test9_avanzarfases_sin_extras(self):
        """Test 9: Verifica la secuencia de fases: 0,1,3,4,5,6,0."""
        # Para alcanzar la fase 6 (secado automático) activamos el "secado a mano"
        self.lavadero.hacerLavado(False, False, False)

        fases = [self.lavadero.fase]
        while self.lavadero.ocupado:
            self.lavadero.avanzarFase()
            fases.append(self.lavadero.fase)

        esperado = [
            Lavadero.FASE_INACTIVO,
            Lavadero.FASE_COBRANDO,
            Lavadero.FASE_ECHANDO_AGUA,
            Lavadero.FASE_ENJABONANDO,
            Lavadero.FASE_RODILLOS,
            Lavadero.FASE_SECADO_AUTOMATICO,
            Lavadero.FASE_INACTIVO,
        ]

        self.assertEqual(fases, esperado)
```

Estas pruebas empiezan a ser un poco más complicadas que las anteriores, lo que estoy haciendo en este test es hacer un lavado y luego crear e¡un bucle que seguira mientra el lavadero está ocupado, este avanzará las fases y las guardará en *fases* , luego hago una tupla llamada *esperado* que son las fases por las que debería pasar sin ningún extra.

![test9-fail](/imgs/unitest/test9-fail.png)

Nos da error ya que pasa por la fase 7 en vez de por la fase 6, esto se debe a que hay un `elif` dentro de el método para cambiar de pase que las condiciones están al reves.

```python
 elif self.__fase == self.FASE_RODILLOS:
            if self.__secado_a_mano:
                self.__fase = self.FASE_SECADO_AUTOMATICO 
            else:
                self.__fase = self.FASE_SECADO_MANO
```

Esto se arregla facilmente dandole la vuelta a las constantes.

![test9-fix](/imgs/unitest/test9-fix.png)

Comprobación : 

![test9-pass](/imgs/unitest/test9-pass.png)

---

### Prueba 10

```python
def test10_avanzarfases_con_prelavado(self):
        """Test 10: Verifica la secuencia de fases con prelavado a mano: 0,1,2,3,4,5,6,0."""
        self.lavadero.hacerLavado(True, False, False)

        fases = [self.lavadero.fase]
        while self.lavadero.ocupado:
            self.lavadero.avanzarFase()
            fases.append(self.lavadero.fase)

        esperado = [
            Lavadero.FASE_INACTIVO,
            Lavadero.FASE_COBRANDO,
            Lavadero.FASE_PRELAVADO_MANO,
            Lavadero.FASE_ECHANDO_AGUA,
            Lavadero.FASE_ENJABONANDO,
            Lavadero.FASE_RODILLOS,
            Lavadero.FASE_SECADO_AUTOMATICO,
            Lavadero.FASE_INACTIVO,
        ]

        self.assertEqual(fases, esperado)


# Bloque de ejecución para ejecutar los tests si el archivo es corrido directamente
if __name__ == '__main__':
    unittest.main()
```

Sigue la misma lógica que en el 9 solo que esta vez con prelavado a mano.

![test10-pass](/imgs/unitest/test10-pass.png)

El código pasa el test a la primera.

---

### Prueba 11

```python
def test11_avanzarfases_con_secadoamano(self):
        """Test 11: Verifica la secuencia de fases con secado a mano: 0,1,3,4,5,7,0."""
        self.lavadero.hacerLavado(False, True, False)

        fases = [self.lavadero.fase]
        while self.lavadero.ocupado:
            self.lavadero.avanzarFase()
            fases.append(self.lavadero.fase)

        esperado = [
            Lavadero.FASE_INACTIVO,
            Lavadero.FASE_COBRANDO,
            Lavadero.FASE_ECHANDO_AGUA,
            Lavadero.FASE_ENJABONANDO,
            Lavadero.FASE_RODILLOS,
            Lavadero.FASE_SECADO_MANO,
            Lavadero.FASE_INACTIVO,
        ]

        self.assertEqual(fases, esperado)
```
![test11-pass](/imgs/unitest/test11-pass.png)

Con secado a mano tambien se pasa el test a la primera.

---

### Prueba 12

```python
 def test12_avanzarfases_con_secadoamano_y_encerado(self):
        """Test 12: Verifica la secuencia de fases con secado a mano y encerado: 0,1,3,4,5,7,8,0."""
        self.lavadero.hacerLavado(False, True, True)

        fases = [self.lavadero.fase]
        while self.lavadero.ocupado:
            self.lavadero.avanzarFase()
            fases.append(self.lavadero.fase)

        esperado = [
            Lavadero.FASE_INACTIVO,
            Lavadero.FASE_COBRANDO,
            Lavadero.FASE_ECHANDO_AGUA,
            Lavadero.FASE_ENJABONANDO,
            Lavadero.FASE_RODILLOS,
            Lavadero.FASE_SECADO_MANO,
            Lavadero.FASE_ENCERADO,
            Lavadero.FASE_INACTIVO,
        ]   
        self.assertEqual(fases, esperado)
```

![test12-fail](/imgs/unitest/test12-fail.png)

Da error con secado a mano y encerado porque en el método de cambiar de fase cuando llega a secado a mano este termina y no comprueba nubnca si la variable *encerado* está en `true`. Este sería el arreglo.

![test12-fix](/imgs/unitest/test12-fix.png)

Después de agregar esa condición `if`comprobamos que se completa el test.

![test12-pass](/imgs/unitest/test12-pass.png)

---

### Prueba 13

```python
 def test13_avanzarfases_con_prelavado_y_secadoamano(self):
        """Test 13: Verifica la secuencia de fases con prelavado a mano y secado a mano: 0,1,2,3,4,5,7,0."""
        self.lavadero.hacerLavado(True, True, False)

        fases = [self.lavadero.fase]
        while self.lavadero.ocupado:
            self.lavadero.avanzarFase()
            fases.append(self.lavadero.fase)

        esperado = [
            Lavadero.FASE_INACTIVO,
            Lavadero.FASE_COBRANDO,
            Lavadero.FASE_PRELAVADO_MANO,
            Lavadero.FASE_ECHANDO_AGUA,
            Lavadero.FASE_ENJABONANDO,
            Lavadero.FASE_RODILLOS,
            Lavadero.FASE_SECADO_MANO,
            Lavadero.FASE_INACTIVO,
        ]

        self.assertEqual(fases, esperado)
```

![test13-pass](/imgs/unitest/test13-pass.png)

Prelavado y secado a mano pasan el test de las fases a la primera.

---

### Prueba 14

```python
 def test14_avanzarfases_con_todas_opciones(self):
            """Test 14: Verifica la secuencia de fases con todas las opciones: 0,1,2,3,4,5,7,8,0."""
            self.lavadero.hacerLavado(True, True, True)

            fases = [self.lavadero.fase]
            while self.lavadero.ocupado:
                self.lavadero.avanzarFase()
                fases.append(self.lavadero.fase)

            esperado = [
                Lavadero.FASE_INACTIVO,
                Lavadero.FASE_COBRANDO,
                Lavadero.FASE_PRELAVADO_MANO,
                Lavadero.FASE_ECHANDO_AGUA,
                Lavadero.FASE_ENJABONANDO,
                Lavadero.FASE_RODILLOS,
                Lavadero.FASE_SECADO_MANO,
                Lavadero.FASE_ENCERADO,
                Lavadero.FASE_INACTIVO,
            ]

            self.assertEqual(fases, esperado)    
```
![test14-pass](/imgs/unitest/test14-pass.png)

Último test también pasado a la primera.

---

## TODAS LAS PRUEBAS PASADAS

![ALL-TESTS](/imgs/unitest/all-tests.png)