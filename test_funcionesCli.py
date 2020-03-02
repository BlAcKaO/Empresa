from unittest import TestCase


class Test(TestCase):
    def test_validar_dni(self):
        from funcionesCli import validarDNI
        self.assertTrue(validarDNI('39453557R'))
