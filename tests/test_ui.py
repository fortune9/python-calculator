"""Tests for the UI modules."""

import pytest

class TestStreamlitUI:
    """Test cases for StreamlitUI class."""
    
    def test_streamlit_import_error(self, monkeypatch):
        """Test ImportError when Streamlit is not available."""
        import sys
        monkeypatch.setitem(sys.modules, 'streamlit', None)
        
        with pytest.raises(ImportError):
            from src.python_calculator.ui import StreamlitUI
            StreamlitUI()

class TestDashUI:
    """Test cases for DashUI class."""
    
    def test_dash_import_error(self, monkeypatch):
        """Test ImportError when Dash is not available."""
        import sys
        monkeypatch.setitem(sys.modules, 'dash', None)
        
        with pytest.raises(ImportError):
            from src.python_calculator.ui import DashUI
            DashUI()