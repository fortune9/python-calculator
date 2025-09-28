"""UI components for the calculator."""

from typing import Optional
from .calculator import Calculator

try:
    import streamlit as st
    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False

try:
    import dash
    from dash import html, dcc, Input, Output, State
    import dash_bootstrap_components as dbc
    DASH_AVAILABLE = True
except ImportError:
    DASH_AVAILABLE = False

class StreamlitUI:
    """Streamlit-based UI for the calculator."""
    
    def __init__(self):
        if not STREAMLIT_AVAILABLE:
            raise ImportError("Streamlit is not installed. Install with: pip install streamlit")
        self.calculator = Calculator()
    
    def render(self):
        """Render the Streamlit UI."""
        st.set_page_config(page_title="Python Calculator", page_icon="🧮")
        st.title("🧮 Python Calculator")
        
        # Input expression
        expression = st.text_input("Enter mathematical expression:", value="2 + 2")
        
        # Operation buttons
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            if st.button("Calculate"):
                try:
                    result = self.calculator.calculate(expression)
                    st.success(f"Result: {result}")
                except ValueError as e:
                    st.error(f"Error: {e}")
        
        with col2:
            if st.button("Clear"):
                st.rerun()
        
        # Quick operations
        st.subheader("Quick Operations")
        num1 = st.number_input("Number 1", value=10.0)
        num2 = st.number_input("Number 2", value=5.0)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("Add"):
                result = self.calculator.add(num1, num2)
                st.info(f"{num1} + {num2} = {result}")
        
        with col2:
            if st.button("Subtract"):
                result = self.calculator.subtract(num1, num2)
                st.info(f"{num1} - {num2} = {result}")
        
        with col3:
            if st.button("Multiply"):
                result = self.calculator.multiply(num1, num2)
                st.info(f"{num1} × {num2} = {result}")
        
        with col4:
            if st.button("Divide"):
                try:
                    result = self.calculator.divide(num1, num2)
                    st.info(f"{num1} ÷ {num2} = {result}")
                except ValueError as e:
                    st.error(f"Error: {e}")

class DashUI:
    """Dash-based UI for the calculator."""
    
    def __init__(self):
        if not DASH_AVAILABLE:
            raise ImportError("Dash is not installed. Install with: pip install dash dash-bootstrap-components")
        self.calculator = Calculator()
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self._setup_layout()
        self._setup_callbacks()
    
    def _setup_layout(self):
        """Setup the Dash layout."""
        self.app.layout = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1("🧮 Python Calculator", className="text-center mb-4")
                ], width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Expression Calculator", className="card-title"),
                            dcc.Input(
                                id="expression-input",
                                type="text",
                                value="2 + 2",
                                className="form-control mb-3",
                                placeholder="Enter mathematical expression"
                            ),
                            dbc.Button("Calculate", id="calculate-btn", color="primary", className="me-2"),
                            dbc.Button("Clear", id="clear-btn", color="secondary"),
                            html.Div(id="result-output", className="mt-3")
                        ])
                    ])
                ], width=6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Quick Operations", className="card-title"),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Input(id="num1-input", type="number", value=10.0, className="mb-2")
                                ]),
                                dbc.Col([
                                    dbc.Input(id="num2-input", type="number", value=5.0, className="mb-2")
                                ])
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button("Add", id="add-btn", color="success", className="w-100 mb-2")
                                ]),
                                dbc.Col([
                                    dbc.Button("Subtract", id="subtract-btn", color="success", className="w-100 mb-2")
                                ])
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button("Multiply", id="multiply-btn", color="success", className="w-100 mb-2")
                                ]),
                                dbc.Col([
                                    dbc.Button("Divide", id="divide-btn", color="success", className="w-100 mb-2")
                                ])
                            ]),
                            html.Div(id="quick-result-output", className="mt-3")
                        ])
                    ])
                ], width=6)
            ])
        ], fluid=True)
    
    def _setup_callbacks(self):
        """Setup Dash callbacks."""
        @self.app.callback(
            Output("result-output", "children"),
            Input("calculate-btn", "n_clicks"),
            State("expression-input", "value"),
            prevent_initial_call=True
        )
        def calculate_expression(n_clicks, expression):
            try:
                result = self.calculator.calculate(expression)
                return dbc.Alert(f"Result: {result}", color="success")
            except ValueError as e:
                return dbc.Alert(f"Error: {e}", color="danger")
        
        @self.app.callback(
            Output("expression-input", "value"),
            Input("clear-btn", "n_clicks"),
            prevent_initial_call=True
        )
        def clear_expression(n_clicks):
            return ""
        
        @self.app.callback(
            Output("quick-result-output", "children"),
            [Input("add-btn", "n_clicks"),
             Input("subtract-btn", "n_clicks"),
             Input("multiply-btn", "n_clicks"),
             Input("divide-btn", "n_clicks")],
            [State("num1-input", "value"),
             State("num2-input", "value")],
            prevent_initial_call=True
        )
        def quick_operations(add_clicks, subtract_clicks, multiply_clicks, divide_clicks, num1, num2):
            ctx = dash.callback_context
            if not ctx.triggered:
                return ""
            
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            num1 = float(num1) if num1 else 0.0
            num2 = float(num2) if num2 else 0.0
            
            try:
                if button_id == "add-btn":
                    result = self.calculator.add(num1, num2)
                    return dbc.Alert(f"{num1} + {num2} = {result}", color="info")
                elif button_id == "subtract-btn":
                    result = self.calculator.subtract(num1, num2)
                    return dbc.Alert(f"{num1} - {num2} = {result}", color="info")
                elif button_id == "multiply-btn":
                    result = self.calculator.multiply(num1, num2)
                    return dbc.Alert(f"{num1} × {num2} = {result}", color="info")
                elif button_id == "divide-btn":
                    result = self.calculator.divide(num1, num2)
                    return dbc.Alert(f"{num1} ÷ {num2} = {result}", color="info")
            except ValueError as e:
                return dbc.Alert(f"Error: {e}", color="danger")
            
            return ""
    
    def run(self, debug: bool = True, **kwargs):
        """Run the Dash app."""
        self.app.run_server(debug=debug, **kwargs)