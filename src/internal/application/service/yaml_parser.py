import yaml
from typing import Dict, Any, Optional
from pathlib import Path
from abc import ABC, abstractmethod

class YamlParser(ABC):
    """
    A class for parsing YAML files into Python dictionaries.
    
    This class provides methods to load YAML content from files or strings
    and convert them to Python dictionaries.
    """

    @staticmethod
    @abstractmethod
    def from_file(file_path: str) -> Dict[str, Any]:
        """
        Parse a YAML file into a dictionary.
        
        Args:
            file_path: Path to the YAML file
            
        Returns:
            Dictionary representation of the YAML content
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            yaml.YAMLError: If the YAML is invalid
        """


    @staticmethod
    @abstractmethod
    def from_string(yaml_string: str) -> Dict[str, Any]:
        """
        Parse a YAML string into a dictionary.
        
        Args:
            yaml_string: String containing YAML content
            
        Returns:
            Dictionary representation of the YAML content
            
        Raises:
            yaml.YAMLError: If the YAML is invalid
        """


class YamlParserImpl:
    
    @staticmethod
    def from_file(file_path: str) -> Dict[str, Any]:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"YAML file not found: {file_path}")
    
        with open(path, 'r', encoding='utf-8') as file:
            try:
                return yaml.safe_load(file)
            except yaml.YAMLError as e:
                raise yaml.YAMLError(f"Error parsing YAML file: {e}")
    
    @staticmethod
    def from_string(yaml_string: str) -> Dict[str, Any]:

        try:
            return yaml.safe_load(yaml_string)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML string: {e}")