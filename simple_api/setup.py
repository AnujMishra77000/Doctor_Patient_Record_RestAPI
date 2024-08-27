from setuptools import setup, find_packages
setup(
    name="Doctor_Patient_Relational_Restapi",
    version="0.1.0",
    author="Anuj Mishra",
    author_email="anujm77000@gmail.com",
    description="Making doctor and patient relation system how doctors and paitent can access there records using RestApi",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AnujMishra77000/Hospitals_Doctor_Patient_record_system/tree/main/simple_api",
    packages=find_packages(),  # Automatically find packages in your project
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    install_requires=[
        # List your project's dependencies
        "Django",
        "Djangorestframework",
        
        # Add more dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    
)
