from glob import glob
import os
from setuptools import find_packages, setup

package_name = 'temperature_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anthonyubuntu',
    maintainer_email='anthony.moundalak@net.usj.edu.lb',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_publisher = temperature_package.temperature_publisher_node:main',
            'threshold_subscriber = temperature_package.threshold_subscriber_node:main',
            'alert_publisher = temperature_package.alert_publisher_node:main',
            'temperature_logger = temperature_package.temperature_logging_node:main',
        ],
    },
)
