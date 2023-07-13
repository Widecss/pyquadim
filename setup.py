from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="pyquadim",
    version="0.1.0",
    author="Widecss",
    author_email="widecss@gmail.com",
    description="Quadim 到 Python 的简单移植。",
    long_description_content_type="text/markdown",
    readme="README.md",
    project_urls={
        "Documentation": "https://github.com/Widecss/wiki/",
        "Code": "https://github.com/Widecss/pyquadim/",
        "Issue Tracker": "https://github.com/Widecss/pyquadim/issues",
    },
    platforms=["macOS", "Windows", "X11"],
    rust_extensions=[RustExtension("pyquadim.pyquadim", binding=Binding.PyO3)],
    packages=["pyquadim"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)
