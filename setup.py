import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='animated-barnacle',
        version='0.1.0-dev',
        author='Charles Tapley Hoyt',
        author_email='cthoyt@gmail.com',
        description='If Dr. Frankenstein were an arthropod, and also a python package',
        license='Apache License 2.0',
        url='https://github.com/cthoyt/animated-barnacle',

        # Look for python code inside /src/
        packages=setuptools.find_packages(where='src'),

        # Assign the package-level folder ('') to be the one it finds in 'src'
        package_dir={'': 'src'},

        install_requires=[
            'click',
        ],

        # Add command line function to automatically run the main function from animated_barnacle.cli
        entry_points={
            'console_scripts': [
                'animated_barnacle = animated_barnacle.cli:main',
            ]
        },
    )
