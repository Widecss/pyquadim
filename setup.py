from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="pyquadim",
    version="0.1.0",
    rust_extensions=[RustExtension("pyquadim.pyquadim", binding=Binding.PyO3)],
    packages=["pyquadim"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)
