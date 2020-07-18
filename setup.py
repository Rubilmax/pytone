import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytone",
    version="1.0.0",
    author="Rubilmax, Merlin Égalité",
    author_email="rmilon@gmail.com, egalite.merlin@gmail.com",
    description="Notifies you when your program finishes!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rubilmax/pytone",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': ['pytone=pytone.command_line:run_python_command'],
    },
    package_data={'pytone': ['assets/*.mp3']}
)
