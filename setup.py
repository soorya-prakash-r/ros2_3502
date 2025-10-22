from setuptools import setup

package_name = 'dice_roller'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    author='R. Soorya Prakash',
    description='ROS 2 Dice Roller: Publishes a random dice number.',
    entry_points={
        'console_scripts': [
            'dice_roller = dice_roller.dice_roller:main',
        ],
    },
)
