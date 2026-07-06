"""
Helper Functions
Utility functions used across the application
"""

import re
import hashlib
import string
import secrets
from typing import List, Tuple, Dict, Any
from datetime import datetime


def validate_email(email: str) -> Tuple[bool, str]:
    """
    Validate email format.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        Tuple[bool, str]: (is_valid, message)
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not email or len(email) > 254:
        return False, "Invalid email length"
    
    if re.match(pattern, email):
        return True, "Valid email format"
    
    return False, "Invalid email format"


def validate_url(url: str) -> Tuple[bool, str]:
    """
    Validate URL format.
    
    Args:
        url (str): URL to validate
    
    Returns:
        Tuple[bool, str]: (is_valid, message)
    """
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    
    if re.match(pattern, url, re.IGNORECASE):
        return True, "Valid URL"
    
    return False, "Invalid URL format"


def validate_ip(ip: str) -> Tuple[bool, str]:
    """
    Validate IPv4 address format.
    
    Args:
        ip (str): IP address to validate
    
    Returns:
        Tuple[bool, str]: (is_valid, message)
    """
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    if re.match(pattern, ip):
        parts = [int(x) for x in ip.split('.')]
        if all(0 <= x <= 255 for x in parts):
            return True, "Valid IPv4 address"
    
    return False, "Invalid IPv4 address"


def validate_domain(domain: str) -> Tuple[bool, str]:
    """
    Validate domain name format.
    
    Args:
        domain (str): Domain to validate
    
    Returns:
        Tuple[bool, str]: (is_valid, message)
    """
    # Remove http/https if present
    domain = re.sub(r'^https?://', '', domain).split('/')[0]
    
    pattern = r'^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}$'
    
    if re.match(pattern, domain, re.IGNORECASE):
        return True, "Valid domain"
    
    return False, "Invalid domain format"


def generate_hash(data: str, hash_type: str = 'sha256') -> str:
    """
    Generate hash of given data.
    
    Args:
        data (str): Data to hash
        hash_type (str): Hash algorithm (md5, sha1, sha256)
    
    Returns:
        str: Hash digest
    """
    hash_type = hash_type.lower()
    
    if hash_type == 'md5':
        return hashlib.md5(data.encode()).hexdigest()
    elif hash_type == 'sha1':
        return hashlib.sha1(data.encode()).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(data.encode()).hexdigest()
    
    return ""


def identify_hash(hash_string: str) -> str:
    """
    Identify hash type by length and format.
    
    Args:
        hash_string (str): Hash to identify
    
    Returns:
        str: Hash type (MD5, SHA1, SHA256, Unknown)
    """
    hash_string = hash_string.strip().lower()
    
    if not re.match(r'^[a-f0-9]+$', hash_string):
        return "Unknown"
    
    length = len(hash_string)
    
    if length == 32:
        return "MD5"
    elif length == 40:
        return "SHA1"
    elif length == 64:
        return "SHA256"
    
    return "Unknown"


def generate_password(
    length: int = 16,
    include_uppercase: bool = True,
    include_lowercase: bool = True,
    include_numbers: bool = True,
    include_symbols: bool = True
) -> str:
    """
    Generate random password.
    
    Args:
        length (int): Password length
        include_uppercase (bool): Include uppercase letters
        include_lowercase (bool): Include lowercase letters
        include_numbers (bool): Include numbers
        include_symbols (bool): Include symbols
    
    Returns:
        str: Generated password
    """
    characters = ""
    
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    if not characters:
        characters = string.ascii_letters + string.digits
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def check_password_strength(password: str) -> Dict[str, Any]:
    """
    Check password strength and return feedback.
    
    Args:
        password (str): Password to check
    
    Returns:
        Dict: Strength score, level, and feedback
    """
    score = 0
    feedback = []
    
    # Length checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")
    
    if len(password) >= 12:
        score += 1
    
    if len(password) >= 16:
        score += 1
    
    # Character variety checks
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        score += 1
    else:
        feedback.append("Add special characters")
    
    # Determine strength level
    if score <= 2:
        level = "Weak"
    elif score <= 4:
        level = "Fair"
    elif score <= 6:
        level = "Good"
    else:
        level = "Strong"
    
    return {
        "score": score,
        "level": level,
        "feedback": feedback,
        "percentage": (score / 7) * 100
    }


def extract_domain(url: str) -> str:
    """
    Extract domain from URL.
    
    Args:
        url (str): URL string
    
    Returns:
        str: Extracted domain
    """
    # Remove protocol
    url = re.sub(r'^https?://', '', url)
    
    # Remove path and query
    domain = url.split('/')[0]
    
    return domain


def sanitize_input(input_str: str, max_length: int = 1000) -> str:
    """
    Sanitize user input.
    
    Args:
        input_str (str): Input string to sanitize
        max_length (int): Maximum allowed length
    
    Returns:
        str: Sanitized string
    """
    # Remove leading/trailing whitespace
    sanitized = input_str.strip()
    
    # Limit length
    sanitized = sanitized[:max_length]
    
    # Remove null bytes
    sanitized = sanitized.replace('\x00', '')
    
    return sanitized


def format_timestamp(timestamp: float) -> str:
    """
    Format Unix timestamp to readable datetime.
    
    Args:
        timestamp (float): Unix timestamp
    
    Returns:
        str: Formatted datetime string
    """
    try:
        dt = datetime.fromtimestamp(timestamp)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return "Invalid timestamp"


def parse_timestamp(date_string: str) -> float:
    """
    Parse date string to Unix timestamp.
    
    Args:
        date_string (str): Date string
    
    Returns:
        float: Unix timestamp
    """
    try:
        dt = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        return dt.timestamp()
    except Exception:
        return 0.0
