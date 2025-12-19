# tests/test_lavadero_unittest.py

import unittest
import sys
from pathlib import Path

from antlr4 import IllegalStateException

# Añadimos el directorio src al path para importar lavadero
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from lavadero import Lavadero

class TestLavadero(unittest.TestCase):
    
    # Método que se ejecuta antes de cada test.
    # Es el equivalente del @pytest.fixture en este contexto.
    def setUp(self):
        """Prepara una nueva instancia de Lavadero antes de cada prueba."""
        self.lavadero = Lavadero()

    # ----------------------------------------------------------------------    
    # Función para resetear el estado cuanto terminamos una ejecución de lavado
    # ----------------------------------------------------------------------
    def test_reseteo_estado_con_terminar(self):
        self.lavadero.hacerLavado(True, True, True)
        self.lavadero._cobrar()
        self.lavadero.terminar()
        
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertTrue(self.lavadero.ingresos > 0) # Los ingresos deben mantenerse
        
    # ----------------------------------------------------------------------
    # TESTS  
    # ----------------------------------------------------------------------
        
    def test1_estado_inicial_correcto(self):
        """Test 1: Verifica que el estado inicial es Inactivo y con 0 ingresos."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)
   
    def test2_excepcion_encerado_sin_secado(self):
        """Test 2: Comprueba que encerar sin secado a mano lanza ValueError."""
        # _hacer_lavado: (Prelavado: False, Secado a mano: False, Encerado: True)
        with self.assertRaises(ValueError):
            self.lavadero.hacerLavado(False, False, True)

    def test3_excepcion_lavado_ocupado(self):
        """Test 3: Verifica que intentar lavar cuando el lavadero está ocupado lanza IllegalStateException."""
        self.lavadero.hacerLavado(True, False, False)  # Inicia un lavado
        with self.assertRaises(IllegalStateException):
            self.lavadero.hacerLavado(False, True, False)  # Intenta iniciar otro lavado

    def test4_prelavadoamano_ingresos_correctos(self):
        """Test 4: Verifica que el prelavado a mano añade 6.5 a los ingresos."""
        self.lavadero.hacerLavado(True, False, False)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 6.5)
    
    def test5_secadoamano_ingresos_correctos(self):
        """Test 5: Verifica que el secado a mano añade 6.0 a los ingresos."""
        self.lavadero.hacerLavado(False, True, False)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 6.0)

    def test6_secadoamano_y_encerado_ingresos_correctos(self):
        """Test 6: Verifica que el secado a mano y encerado añaden 7.2 a los ingresos."""
        self.lavadero.hacerLavado(False, True, True)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 7.2)

    def test7_prelavadoamano_y_secadoamano_ingresos_correctos(self):
        """Test 7: Verifica que el prelavado a mano y secado a mano añaden 7.5 a los ingresos."""
        self.lavadero.hacerLavado(True, True, False)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 7.5)

    def test8_todas_opciones_ingresos_correctos(self):
        """Test 8: Verifica que todas las opciones añaden 8.7 a los ingresos."""
        self.lavadero.hacerLavado(True, True, True)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 8.7)

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

# Bloque de ejecución para ejecutar los tests si el archivo es corrido directamente
if __name__ == '__main__':
    unittest.main()