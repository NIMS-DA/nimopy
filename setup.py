from setuptools import setup, find_packages

setup(
    name="nimopy",
    version="1.0.0",
    author="NIMO developers",
    license="MIT",
    description='NIMO package',
    packages=["nimopy", "nimopy.ai_tools", "nimopy.input_tools", "nimopy.output_tools", "nimopy.visualization"],
    install_requires=[
        "matplotlib",
        "numpy",
        "scikit-learn",
        "scipy"
    ]
)
