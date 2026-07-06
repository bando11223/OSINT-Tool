"""
Data Models
Defines data structures used throughout the application
"""

from dataclasses import dataclass, asdict
from typing import Dict, List, Any, Optional
from datetime import datetime
import json


@dataclass
class SearchResult:
    """
    Represents a single search result item.
    """
    title: str
    value: str
    category: str
    timestamp: datetime = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        """Initialize default values."""
        if self.timestamp is None:
            self.timestamp = datetime.now()
        if self.metadata is None:
            self.metadata = {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            'title': self.title,
            'value': self.value,
            'category': self.category,
            'timestamp': self.timestamp.isoformat(),
            'metadata': self.metadata
        }
    
    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_dict(), indent=2)


@dataclass
class ToolResult:
    """
    Represents the complete result from a tool search.
    """
    tool_name: str
    query: str
    success: bool
    results: List[SearchResult]
    error_message: Optional[str] = None
    execution_time: float = 0.0
    timestamp: datetime = None
    
    def __post_init__(self):
        """Initialize default values."""
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            'tool_name': self.tool_name,
            'query': self.query,
            'success': self.success,
            'results': [r.to_dict() for r in self.results],
            'error_message': self.error_message,
            'execution_time': self.execution_time,
            'timestamp': self.timestamp.isoformat(),
            'result_count': len(self.results)
        }
    
    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_dict(), indent=2)
    
    def to_csv_rows(self) -> List[str]:
        """Convert to CSV rows."""
        rows = []
        rows.append(f"Tool,{self.tool_name}")
        rows.append(f"Query,{self.query}")
        rows.append(f"Success,{self.success}")
        rows.append(f"Execution Time,{self.execution_time}s")
        rows.append(f"Results Count,{len(self.results)}")
        rows.append("")
        rows.append("Title,Value,Category,Timestamp")
        
        for result in self.results:
            rows.append(f'"{result.title}","{result.value}","{result.category}","{result.timestamp.isoformat()}"')
        
        return rows
