from distutils.core import setup

setup(
    name='cve_vendor_scraping',
    version='0.1',
    packages=[''],
    url='https://github.com/fgaudenzi/cve_vendor_scraping',
    license='Apache License 2.0',
    author='Filippo Gaudenzi',
    author_email='gaudenzi dot filippo at gmail dot com',
    description='Scrape all cve (all pages) once you have the specific url ',
    install_requires=[
        'scrapy'
    ],

)
