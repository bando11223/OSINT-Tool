"""
HTTP Requests Handler
Manages all HTTP requests with error handling and retries
"""

import requests
from typing import Optional, Dict, Any, Tuple
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging


class RequestsHandler:
    """
    Handles HTTP requests with retry logic and error handling.
    """
    
    def __init__(self, timeout: int = 10, max_retries: int = 3):
        """
        Initialize RequestsHandler.
        
        Args:
            timeout (int): Request timeout in seconds
            max_retries (int): Maximum number of retries
        """
        self.timeout = timeout
        self.max_retries = max_retries
        self.logger = logging.getLogger(__name__)
        self.session = self._create_session()
    
    def _create_session(self) -> requests.Session:
        """
        Create requests session with retry strategy.
        
        Returns:
            requests.Session: Configured session
        """
        session = requests.Session()
        
        retry_strategy = Retry(
            total=self.max_retries,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"]
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Set user agent
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        return session
    
    def get(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Tuple[bool, Any, str]:
        """
        Make GET request.
        
        Args:
            url (str): Request URL
            headers (Dict, optional): Custom headers
            params (Dict, optional): Query parameters
        
        Returns:
            Tuple[bool, Any, str]: (success, data, error_message)
        """
        try:
            response = self.session.get(
                url,
                headers=headers,
                params=params,
                timeout=self.timeout
            )
            
            response.raise_for_status()
            
            return True, response.json() if response.text else response.text, ""
        
        except requests.exceptions.Timeout:
            error = f"Request timeout ({self.timeout}s)"
            self.logger.error(f"Timeout: {url}")
            return False, None, error
        
        except requests.exceptions.ConnectionError:
            error = "Connection error"
            self.logger.error(f"Connection error: {url}")
            return False, None, error
        
        except requests.exceptions.HTTPError as e:
            error = f"HTTP Error: {e.response.status_code}"
            self.logger.error(f"HTTP error {e.response.status_code}: {url}")
            return False, None, error
        
        except requests.exceptions.RequestException as e:
            error = f"Request failed: {str(e)}"
            self.logger.error(f"Request error: {error}")
            return False, None, error
        
        except Exception as e:
            error = f"Unexpected error: {str(e)}"
            self.logger.error(f"Unexpected error: {error}")
            return False, None, error
    
    def post(
        self,
        url: str,
        json_data: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Tuple[bool, Any, str]:
        """
        Make POST request.
        
        Args:
            url (str): Request URL
            json_data (Dict, optional): JSON body
            data (Any, optional): Form data
            headers (Dict, optional): Custom headers
        
        Returns:
            Tuple[bool, Any, str]: (success, data, error_message)
        """
        try:
            response = self.session.post(
                url,
                json=json_data,
                data=data,
                headers=headers,
                timeout=self.timeout
            )
            
            response.raise_for_status()
            
            return True, response.json() if response.text else response.text, ""
        
        except requests.exceptions.RequestException as e:
            error = f"Request failed: {str(e)}"
            self.logger.error(f"POST error: {error}")
            return False, None, error
        
        except Exception as e:
            error = f"Unexpected error: {str(e)}"
            self.logger.error(f"Unexpected error: {error}")
            return False, None, error
    
    def head(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None
    ) -> Tuple[bool, Dict[str, Any], str]:
        """
        Make HEAD request.
        
        Args:
            url (str): Request URL
            headers (Dict, optional): Custom headers
        
        Returns:
            Tuple[bool, Dict, str]: (success, headers_dict, error_message)
        """
        try:
            response = self.session.head(
                url,
                headers=headers,
                timeout=self.timeout
            )
            
            response.raise_for_status()
            
            return True, dict(response.headers), ""
        
        except requests.exceptions.RequestException as e:
            error = f"Request failed: {str(e)}"
            self.logger.error(f"HEAD error: {error}")
            return False, {}, error
        
        except Exception as e:
            error = f"Unexpected error: {str(e)}"
            self.logger.error(f"Unexpected error: {error}")
            return False, {}, error
    
    def close(self) -> None:
        """Close the session."""
        self.session.close()
