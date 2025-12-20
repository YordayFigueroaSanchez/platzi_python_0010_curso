import unittest

class AllAssertsTest(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(1, 1)
        self.assertEqual("hola", "hola")

    def test_assert_not_equal(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual("hola", "adios")

    def test_assert_true(self):
        self.assertTrue(1 == 1)
        self.assertTrue("hola" == "hola")

    def test_assert_false(self):
        self.assertFalse(1 == 2)
        self.assertFalse("hola" == "adios")

    def test_assert_is(self):
        self.assertIs(1, 1)
        self.assertIs("hola", "hola")

    def test_assert_is_not(self):
        self.assertIsNot(1, 2)
        self.assertIsNot("hola", "adios")

    def test_assert_is_none(self):
        self.assertIsNone(None)
        self.assertIsNotNone(1)

    def test_assert_raises(self):
        self.assertRaises(ZeroDivisionError, lambda: 1 / 0)

    def test_assert_raises_regex(self):
        self.assertRaisesRegex(ZeroDivisionError, "division by zero", lambda: 1 / 0)

    # test in list
    def test_assert_in(self):
        self.assertIn(1, [1, 2, 3])
        self.assertIn("hola", "hola")

    # test not in list
    def test_assert_not_in(self):
        self.assertNotIn(1, [2, 3])
        self.assertNotIn("hola", "adios")

    # test de conjuntos
    def test_assert_set(self):
        self.assertSetEqual({1, 2, 3}, {1, 2, 3}, "Los conjuntos no son iguales")
        self.assertSetEqual({"hola", "adios"}, {"adios", "hola"}, "Los conjuntos no son iguales")

    # test de diccionarios
    def test_assert_dict(self):
        self.assertDictEqual({"hola": "adios"}, {"hola": "adios"})