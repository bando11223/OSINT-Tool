"""
Input Validation
Validates user input for all OSINT tools
"""

import re
from typing import Tuple, List
from src.utils.helpers import (
    validate_email, validate_url, validate_ip,
    validate_domain, sanitize_input
)


class InputValidator:
    """
    Validates user input for various OSINT operations.
    """
    
    @staticmethod
    def validate_username(username: str) -> Tuple[bool, str]:
        """
        Validate username format.
        
        Args:
            username (str): Username to validate
        
        Returns:
            Tuple[bool, str]: (is_valid, message)
        """
        username = sanitize_input(username, 100)
        
        if not username or len(username) < 1:
            return False, "Username cannot be empty"
        
        if len(username) > 50:
            return False, "Username too long (max 50 characters)"
        
        # Allow alphanumeric, underscores, hyphens, dots
        if re.match(r'^[a-zA-Z0-9._-]+$', username):
            return True, "Valid username"
        
        return False, "Invalid username format"
    
    @staticmethod
    def validate_email_input(email: str) -> Tuple[bool, str]:
        """
        Validate email input.
        
        Args:
            email (str): Email to validate
        
        Returns:
            Tuple[bool, str]: (is_valid, message)
        """
        email = sanitize_input(email, 254)
        return validate_email(email)
    
    @staticmethod
    def validate_domain_input(domain: str) -> Tuple[bool, str]:
        """
        Validate domain input.
        
        Args:
            domain (str): Domain to validate
        
        Returns:
            Tuple[bool, str]: (is_valid, message)
        """
        domain = sanitize_input(domain, 255)
        return validate_domain(domain)
    
    @staticmethod
    def validate_ip_input(ip: str) -> Tuple[bool, str]:
        """
        Validate IP address input.
        
        Args:
            ip (str): IP address to validate
        
        Returns:
            Tuple[bool, str]: (is_valid, message)
        """
        ip = sanitize_input(ip, 50)
        return validate_ip(ip)
    
    @staticmethod
    def validate_phone_number(phone: str) -> Tuple[bool, str]:
        """
        Validate phone number format.
        
        Args:
            phone (str): Phone number to validate
        
        Returns:
            Tuple[bool, str]: (is_valid, message)
        """
        phone = sanitize_input(phone.replace(' ', '').replace('-', ''), 20)
        
        if not re.match(r'^\+?1?\d{9,15}$', phone):
            return False, "Invalid phone number format"
        
        return True, "Valid phone number"
    
    @staticmethod
    def validate_hash(hash_string: str) -> Tuple[bool, str]:
        """
        Validate hash format.
        
        Args:
            hash_string (str): Hash to validate
        
        Returns:
            Tuple[bool, str]: (is_valid, message)
        """
        hash_string = sanitize_input(hash_string.strip(), 128).lower()
        
        if not re.match(r'^[a-f0-9]+$', hash_string):
            return False, "Invalid hash format"
        
        length = len(hash_string)
        
        if length not in [32, 40, 64]:
            return False, "Invalid hash length (must be 32, 40, or 64 characters)"
        
        return True, "Valid hash"
    
    @staticmethod
    def validate_search_query(query: str, min_length: int = 2, max_length: int = 100) -> Tuple[bool, str]:
        """
        Validate general search query.
        
        Args:
            query (str): Search query
            min_length (int): Minimum query length
            max_length (int): Maximum query length
        
        Returns:
            Tuple[bool, str]: (is_valid, message)
        """
        query = sanitize_input(query, max_length)
        
        if len(query) < min_length:
            return False, f"Query too short (minimum {min_length} characters)"
        
        if len(query) > max_length:
            return False, f"Query too long (maximum {max_length} characters)"
        
        return True, "Valid query"
    
    @staticmethod
    def validate_file_path(file_path: str) -> Tuple[bool, str]:
        """
        Validate file path.
        
        Args:
            file_path (str): File path to validate
        
        Returns:
            Tuple[bool, str]: (is_valid, message)
        """
        file_path = sanitize_input(file_path, 255)
        
        if not file_path:
            return False, "File path cannot be empty"
        
        # Check for dangerous characters
        dangerous_chars = ['*', '?', '"', '<', '>', '|']
        if any(char in file_path for char in dangerous_chars):
            return False, "File path contains invalid characters"
        
        return True, "Valid file path"
