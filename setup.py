from setuptools import setup

setup(name='ohmlaws',
        version='0.1',
        description='The formula of electrical enginering ',
        url='https://github.com/zizonk/electrical-formula.git',
        author='M afif Nur Azizi',
        author_email='afifnurazizi@gmail.com',
        license='MIT',
        packages=['ohm_formula'],
        packages_dir={'':'scr'},
        dependency_links=[
                'https://github.com/zizonk/electrical-formula'
        ],
        install_requires=[
          'markdown'
          ],
        zip_safe=False)