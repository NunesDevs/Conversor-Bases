import unittest
import subprocess
import sys
from pathlib import Path
from program import convert_decimal


class ConversionTests(unittest.TestCase):
    def test_cli_retries_invalid_input_and_exits_on_eof(self):
        script = str(Path(__file__).resolve().parents[1] / 'program.py')
        process = subprocess.run([sys.executable, '-X', 'utf8', script], input='abc\n0\nn\n', text=True, encoding='utf-8', capture_output=True, timeout=5)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(process.stdout.count('\n0\n'), 5)
        self.assertIn('Valor inválido', process.stdout)
        eof = subprocess.run([sys.executable, '-X', 'utf8', script], input='', text=True, encoding='utf-8', capture_output=True, timeout=5)
        self.assertEqual(eof.returncode, 0, eof.stderr)
        self.assertIn('Encerrando', eof.stdout)

    def test_zero_sign_and_supported_bases(self):
        expected = {2: "10011", 4: "103", 8: "23", 16: "13", 20: "J"}
        for base, text in expected.items():
            self.assertEqual(convert_decimal(19, base), text)
            self.assertEqual(convert_decimal(-19, base), "-" + text)
            self.assertEqual(convert_decimal(0, base), "0")

    def test_round_trip_all_bases_and_large_integers(self):
        for base in (2, 4, 8, 16, 20):
            for value in (-12345, 1, 255, 2 ** 200):
                self.assertEqual(int(convert_decimal(value, base), base), value)

    def test_reject_invalid_values(self):
        for value in (True, 1.5, "12", None):
            with self.assertRaises(TypeError):
                convert_decimal(value, 2)
        for base in (True, 1, 2.0, 3, 36, None):
            with self.assertRaises(ValueError):
                convert_decimal(1, base)


if __name__ == "__main__":
    unittest.main()
