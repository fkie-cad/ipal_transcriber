from setuptools import setup, find_packages

setup(
    name="ipal-transcriber",
    version="1.1.0",
    packages=find_packages(exclude="tests"),
    scripts=["ipal-transcriber", "ipal-state-extractor", "ipal-minimize"],
    package_data={"": ["*.ipal", "*.pcapng"]},
    install_requires=["pyshark", "python-dateutil"],
    tests_require=["pytest"],
    url="https://github.com/fkie-cad/ipal_transcriber",
    author="Konrad Wolsing",
    author_email="wolsing@comsys.rwth-aachen.de",
    long_description="Cyber-physical systems are increasingly threatened by sophisticated attackers, also attacking the physical aspect of systems. Supplementing protective measures, industrial intrusion detection systems promise to detect such attacks. However, due to industrial protocol diversity and lack of standard interfaces, great efforts are required to adapt these technologies to a large number of different protocols. To address this issue, we propose IPAL - a common representation of industrial communication as input for industrial intrusion detection systems.  This software (transcriber) implements the automatic translation of industrial network traffic into IPAL for a variety of industrial protocols.",
    description="Industrial protocol transcriber - a common representation of industrial communication as input for protocol-independent industrial intrusion detection systems",
    keywords="industrial protocols networking security capture packets IDS CIP GOOSE Modbus S7 IEC 60870-5-104 NMEA0183 IEC 61162-450 DNP3",
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
