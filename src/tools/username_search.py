"""
Username Search Tool
Search for usernames across social media platforms
"""

import requests
from typing import List, Dict, Any
from src.models import SearchResult, ToolResult
from src.api import RequestsHandler
import logging


class UsernameSearchTool:
    """
    Search for usernames across multiple social media platforms.
    """
    
    # Social media platforms with typical URL patterns
    PLATFORMS = {
        'Twitter': 'https://twitter.com/{username}',
        'Instagram': 'https://instagram.com/{username}',
        'GitHub': 'https://github.com/{username}',
        'LinkedIn': 'https://linkedin.com/in/{username}',
        'Facebook': 'https://facebook.com/{username}',
        'TikTok': 'https://tiktok.com/@{username}',
        'YouTube': 'https://youtube.com/@{username}',
        'Reddit': 'https://reddit.com/user/{username}',
        'Twitch': 'https://twitch.tv/{username}',
        'Pinterest': 'https://pinterest.com/{username}',
        'Snapchat': 'https://snapchat.com/add/{username}',
        'Medium': 'https://medium.com/@{username}',
        'Stack Overflow': 'https://stackoverflow.com/users/{username}',
        'HackerNews': 'https://news.ycombinator.com/user?id={username}',
        'Imgur': 'https://imgur.com/user/{username}'
    }
    
    def __init__(self, timeout: int = 10, max_retries: int = 3):
        """
        Initialize UsernameSearchTool.
        
        Args:
            timeout (int): Request timeout
            max_retries (int): Maximum retries
        """
        self.requests_handler = RequestsHandler(timeout, max_retries)
        self.logger = logging.getLogger(__name__)
    
    def search(self, username: str) -> ToolResult:
        """
        Search for username across platforms.
        
        Args:
            username (str): Username to search
        
        Returns:
            ToolResult: Search results
        """
        results = []
        found_count = 0
        
        for platform, url_template in self.PLATFORMS.items():
            try:
                url = url_template.format(username=username)
                
                # Use HEAD request for efficiency
                success, headers, error = self.requests_handler.head(url)
                
                if success:
                    found_count += 1
                    result = SearchResult(
                        title=f"{platform} Account Found",
                        value=url,
                        category="Account",
                        metadata={'platform': platform, 'status': 'found'}
                    )
                    results.append(result)
            
            except Exception as e:
                self.logger.error(f"Error searching {platform}: {str(e)}")
                continue
        
        return ToolResult(
            tool_name="Username Search",
            query=username,
            success=found_count > 0,
            results=results,
            error_message=None if found_count > 0 else "No accounts found"
        )
    
    def search_detailed(self, username: str) -> ToolResult:
        """
        Search with more detailed information.
        
        Args:
            username (str): Username to search
        
        Returns:
            ToolResult: Detailed search results
        """
        results = []
        
        for platform, url_template in self.PLATFORMS.items():
            try:
                url = url_template.format(username=username)
                
                success, headers, error = self.requests_handler.head(url)
                
                if success:
                    status = "✓ Found"
                    metadata = {
                        'platform': platform,
                        'status': 'found',
                        'url': url
                    }
                else:
                    status = "✗ Not found"
                    metadata = {
                        'platform': platform,
                        'status': 'not_found',
                        'error': error
                    }
                
                result = SearchResult(
                    title=f"{platform}: {status}",
                    value=url,
                    category="Account",
                    metadata=metadata
                )
                results.append(result)
            
            except Exception as e:
                result = SearchResult(
                    title=f"{platform}: Error",
                    value=str(e),
                    category="Error",
                    metadata={'platform': platform, 'error': str(e)}
                )
                results.append(result)
        
        found_count = sum(1 for r in results if r.metadata.get('status') == 'found')
        
        return ToolResult(
            tool_name="Username Search (Detailed)",
            query=username,
            success=found_count > 0,
            results=results,
            error_message=None if found_count > 0 else "No accounts found"
        )
