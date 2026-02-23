import codecs
import configparser
import urllib.parse
from typing import Any, Dict, List, Optional, Union

class ConfigHelper:
    """Simplified helper for reading/writing ModOrganizer.ini config."""
    
    def __init__(self, config_path: str = 'ModOrganizer.ini'):
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
    
    def save(self):
        """Write config back to file."""
        with open(self.config_path, 'w') as f:
            self.config.write(f)
    
    def get(self, section: str, key: str = '', default: Any = None) -> Any:
        """
        Get a value or entire section.
        
        Args:
            section: Section name
            key: Optional key to get specific value
            default: Default value if not found
        """
        if section not in self.config:
            return default
        
        if key is None:
            return dict(self.config[section])
        
        return self.config[section].get(key, default)
    
    def get_nested(self, section: str) -> Dict[str, Dict[str, Any]]:
        """
        Get a nested section (e.g., customExecutables).
        
        Returns dict like: {'1': {'title': 'New Vegas', 'binary': '...'}}
        """
        if section not in self.config:
            return {}
        
        result = {}
        for key, value in self.config[section].items():
            if key == 'size':
                continue
            
            parts = key.split('\\')
            if len(parts) >= 2:
                parent, child = parts[0], parts[1]
                if parent not in result:
                    result[parent] = {}
                result[parent][child] = self._unescape(value)
        
        return result
    
    def get_list(self, section: str) -> List[Dict[str, Any]]:
        """Get a nested section as a sorted list."""
        nested = self.get_nested(section)
        return [nested[k] for k in sorted(nested.keys(), key=int)]
    
    def set(self, section: str, key: str, value: Any):
        """Set a simple key-value pair."""
        if section not in self.config:
            self.config.add_section(section)
        self.config[section][key] = str(value)
    
    def set_nested(self, section: str, parent: str, child: str, value: Any):
        """Set a nested key-value pair (e.g., section '1' 'title' 'New Vegas')."""
        if section not in self.config:
            self.config.add_section(section)
        key = f"{parent}\\{child}"
        self.config[section][key] = self._escape(str(value))
    
    def update_nested(self, section: str, parent: str, data: Dict[str, Any]):
        """Update multiple properties for a nested entry."""
        if section not in self.config:
            self.config.add_section(section)
        for child, value in data.items():
            key = f"{parent}\\{child}"
            self.config[section][key] = self._escape(str(value))
    
    def remove_nested(self, section: str, parent: str):
        """Remove all keys for a nested entry."""
        if section not in self.config:
            return
        
        keys_to_remove = [k for k in self.config[section] if k.startswith(f"{parent}\\")]
        for key in keys_to_remove:
            del self.config[section][key]
    
    def _escape(self, value: str) -> str:
        """Escape backslashes for storage."""
        return value.replace('\\', '\\\\')
    
    def _unescape(self, value: str) -> str:
        """Unescape backslashes from storage."""
        return codecs.decode(value, 'unicode_escape')


# Convenience functions
def get_executables(config_path: str = 'ModOrganizer.ini') -> List[Dict[str, Any]]:
    """Get custom executables as a list."""
    helper = ConfigHelper(config_path)
    return helper.get_list('customExecutables')
    
def get_executable_titles(config_path: str = 'ModOrganizer.ini') -> List[str]:
    """Get list of executable titles."""
    return [exe['title'] for exe in get_executables(config_path)]

def get_mod_list(config_path: str = "ModOrganizer.ini") -> List[str]:
    helper = ConfigHelper(config_path)
    mod_list = helper.get('Widgets', 'MainWindow_modList_index')
    mod_list = mod_list.split(', ')
    print(mod_list)
    return mod_list