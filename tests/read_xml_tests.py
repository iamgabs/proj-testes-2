import unittest
from unittest.mock import patch, mock_open
from xml.etree.ElementTree import ParseError
from src.services.read_xml import read_xml as read_xml

class TestCaseReadXml(unittest.TestCase):

    def test_read_xml_valid(self):
        
        xml_content = '''<?xml version="1.0"?>
            <procedimentos>
                <procedimento desc="soma">
                    <caso>
                        <dado1>10</dado1>
                        <dado2>20</dado2>
                    </caso>
                </procedimento>
            </procedimentos>'''
        
        with patch('builtins.open', mock_open(read_data=xml_content)):
            result = read_xml('procedimentos.xml')

        self.assertEqual(result, [('soma', ['10 20'])])
    
    def test_read_xml_unsupported(self):

        xml_content = '''<?xml version="1.0"?>
            <procedimentos>
                <procedimento desc="*">
                    <caso>
                        <dado1>10</dado1>
                        <dado2>20</dado2>
                    </caso>
                </procedimento>
            </procedimentos>'''
        
        with patch('builtins.open', mock_open(read_data=xml_content)):
            result = read_xml('procedimentos.xml')   
        
        self.assertEqual(result, [])

    def test_read_xml_invalid_file(self):
        with patch('xml.etree.ElementTree.parse', side_effect=ParseError('invalid XML')):
            result = read_xml('invalid_file.xml')
        
        self.assertEqual(result, [])

    def test_read_xml_empty_file(self):

        xml_content = ''

        with patch('builtins.open', mock_open(read_data=xml_content)):
            result = read_xml('procedimentos.xml')
        
        self.assertEqual(result, [])