import logging

version = "v1.3.6"

# Gzip options
compresslevel = 9  # 0 no compress, 1 large/fast, 9 small/slow

# Assumed default ports
MBTCP_PORT = 502
ENIP_PORT = 44818
MAVLINK_PORT = [14550, 14580]

pyshark_options = [
    "-o",
    "udp.check_checksum:TRUE",
    "-o",
    "tcp.check_checksum:TRUE",
    "-o",
    "mbtcp.tcp.port:{}".format(MBTCP_PORT),
]

pyshark_decode_as = {}

# Transcriber default settings
mode = None  # 'pcap' or 'interface'
source = None  # path to pcap or interface name
protocols = []  # protocol names to transcribe
rules = None
rulesin = None  # path to rule file
crc = "and"  # application, transport, and, or
timeout = 0.250  # 250 ms
maliciousdefault = None
malicious = None
maliciousin = None

# Output settings
ipalout = None
ipaloutfd = None
evalout = None
evaloutfd = None

# Logging settings
hostname = False
logger = logging.getLogger("ipal-transcriber")
log = logging.WARNING
logformat = "%(levelname)s:%(name)s:%(message)s"
logfile = None

# State output
ipalin = None
ipalinfd = None
state_extractor = None
stateout = None
stateoutfd = None
filter = None
completeonly = False
stateinmessage = False


def transcriber_settings_to_dict():
    return {
        "version": version,
        "compresslevel": compresslevel,
        "mbtcp_port": MBTCP_PORT,
        "enip_port": ENIP_PORT,
        "mavlink_port": MAVLINK_PORT,
        "pyshark_options": pyshark_options,
        "source": source,
        "protocols": protocols,
        "rules": rulesin,
        "crc": crc,
        "timeout": timeout,
        "maliciousdefault": maliciousdefault,
        "malicious": maliciousin,
        "ipalout": ipalout,
        "hostname": hostname,
        "log": log,
        "logformat": logformat,
        "logfile": logfile,
    }


def state_extractor_settings_to_dict():
    return {
        "version": version,
        "compresslevel": compresslevel,
        "ipalin": ipalin,
        "state_extractor": state_extractor._name,
        "stateout": stateout,
        "filter": filter,
        "completeonly": completeonly,
        "stateinmessage": stateinmessage,
        "hostname": hostname,
        "log": log,
        "logformat": logformat,
        "logfile": logfile,
    }
