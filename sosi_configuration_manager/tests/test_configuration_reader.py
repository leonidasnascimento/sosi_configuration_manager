from configuration_reader import reader
import unittest

class test_configuration_reader(unittest.TestCase):
    def test_should_read_configuration_successfully(self):
        configReader = reader("tests/test.configreader.settings.json", "RealValue")
        val = configReader.getValue("WEBSITE_SITE_NAME", None)
        self.assertEqual(str(val).lower(), "sosi-ms001-stockmktlisting")
        pass
    
if __name__ == "__main__":
    unittest.main()