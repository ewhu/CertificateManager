# test_certificatemanager.py
"""
Tests for CertificateManager module.
"""

import unittest
from certificatemanager import CertificateManager

class TestCertificateManager(unittest.TestCase):
    """Test cases for CertificateManager class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CertificateManager()
        self.assertIsInstance(instance, CertificateManager)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CertificateManager()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
