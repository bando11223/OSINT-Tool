"""
Configuration Management
Handles loading, saving, and managing application configuration
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional


class ConfigManager:
    """
    Manages application configuration settings.
    
    Handles loading from config.json, updating settings, and saving changes.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize ConfigManager.
        
        Args:
            config_path (str): Path to config.json file
        """
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = {}
        self.load()
    
    def load(self) -> None:
        """Load configuration from file."""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
            else:
                # Use default config if file doesn't exist
                self.config = self._get_default_config()
                self.save()
        except Exception as e:
            print(f"Error loading config: {e}")
            self.config = self._get_default_config()
    
    def save(self) -> None:
        """Save configuration to file."""
        try:
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value by dot notation.
        
        Args:
            key (str): Key path (e.g., 'app.theme')
            default (Any): Default value if key not found
        
        Returns:
            Any: Configuration value
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        
        return value if value is not None else default
    
    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value by dot notation.
        
        Args:
            key (str): Key path (e.g., 'app.theme')
            value (Any): Value to set
        """
        keys = key.split('.')
        config = self.config
        
        # Navigate to the nested key
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        # Set the value
        config[keys[-1]] = value
        self.save()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration."""
        return {
            "app": {
                "theme": "dark",
                "accent_color": "blue",
                "window_width": 1400,
                "window_height": 900,
                "update_check": True,
                "font_size": 12
            },
            "api_keys": {
                "ipinfo": "",
                "abuseipdb": "",
                "emailrep": ""
            },
            "settings": {
                "timeout": 10,
                "max_retries": 3,
                "log_searches": True,
                "auto_save_history": True,
                "max_history_items": 100
            }
        }
