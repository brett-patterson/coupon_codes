from setuptools import setup, find_packages


def setup_package():
    setup(
        name='coupon_codes',
        version='0.1',
        description='A coupon code generation algorithm',
        url='https://github.com/brett-patterson/coupon_codes',
        author='Brett Patterson',
        author_email='bmp2@rice.edu',
        packages=find_packages()
    )

if __name__ == '__main__':
    setup_package()
