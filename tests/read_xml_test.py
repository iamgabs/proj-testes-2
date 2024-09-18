import unittest
from unittest.mock import patch, mock_open
from xml.etree.ElementTree import ParseError
from src.services.read_xml import read_xml as read_xml

class TestCaseReadXml(unittest.TestCase):

    def test_read_xml_valid(self) -> None:
        
        xml_content = '''<?xml version="1.0" encoding="utf-8"?>
            <procedimentos>
                <!-- SOMA -->
                <procedimento num="0" desc="soma">
                    <caso num="0">
                        <dado>10</dado>
                        <dado>20</dado>
                        <resultado>30</resultado>
                    </caso>
                </procedimento>
            </procedimentos>
            '''
        
        with patch('builtins.open', mock_open(read_data=xml_content)):
            result = read_xml('procedimentos.xml')

        self.assertEqual(result, "[('soma', ['10 20'], [30.0])]")
    
    def test_read_xml_unsupported(self) -> None:

        xml_content = '''<?xml version="1.0" encoding="utf-8"?>
            <procedimentos>
                <!-- SOMA -->
                <procedimento num="0" desc="*">
                    <caso num="0">
                        <dado>10</dado>
                        <dado>20</dado>
                        <resultado>30</resultado>
                    </caso>
                </procedimento>
            </procedimentos>
            '''
        
        with patch('builtins.open', mock_open(read_data=xml_content)):
            result = read_xml('procedimentos.xml')   
        
        self.assertEqual(result, ("Operação "*" não suportada.", []))

    def test_read_xml_empty_file(self) -> None:

        xml_content = ''

        with patch('builtins.open', mock_open(read_data=xml_content)), \
             patch('xml.etree.ElementTree.parse', side_effect=ParseError('no element found: line 1, column 0')):
            result = read_xml('procedimentos.xml')
        
        self.assertEqual(result, [])