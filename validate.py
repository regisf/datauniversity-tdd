import re


def validate_ip_address(ip_address):
    return re.match(r'\d+\.\d+\.\d+\.\d+\.', ip_address) is not None    
    
