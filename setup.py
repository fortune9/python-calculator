from setuptools import setup, find_packages

setup(
    name="python-calculator",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
    extras_require={
        "streamlit": ["streamlit>=1.28.0"],
        "dash": ["dash>=2.14.0", "dash-bootstrap-components>=1.5.0"],
        "dev": ["pytest>=7.0.0", "pytest-cov>=4.0.0"],
        "all": ["streamlit>=1.28.0", "dash>=2.14.0", "dash-bootstrap-components>=1.5.0"]
    },
    python_requires=">=3.8",
)