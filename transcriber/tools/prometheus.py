from prometheus_client import start_http_server, Counter

class PrometheusClient():
    def __init__(self) -> None:
        # 9100 is the node_exporter, if present
        start_http_server(9101)