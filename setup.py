import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dj-gravatar", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="souravdas.sd20@gmail.com",
    description="Use Gravatar in a Django Website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PhysicistSouravDas/dj-gravatar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)