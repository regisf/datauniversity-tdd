import unittest
from validate import validate_ip_address


class TestIpAddress(unittest.TestCase):
    def test_validate_ip_address(self):
        result = validate_ip_address('124.65.89.254')
        self.assertTrue(result)
        
    def test_casting_is_not_valid(self):
        result = validate_ip_address('255.255.255.255')
        self.assertFalse(result)
       
    def test_every_body_is_not_valid(self):
        result = validate_ip_address('0.0.0.0')
        self.assertFalse(result)
       
    def test_local_is_not_valid(self):
        result = validate_ip_address('127.0.1.1')
        self.assertFalse(result)
     
    def test_private_10_is_not_valid(self):
        result = validate_ip_address('10.0.1.1')
        self.assertFalse(result)
    
    def test_private_192_168_is_not_valid(self):
    
        result = validate_ip_address('192.168.1.1')
        self.assertFalse(result)
       
    
       
if __name__ == '__main__':
    unittest.main()
   
