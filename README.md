[![OMERO](https://github.com/ome/omero-prometheus-tools/workflows/OMERO/badge.svg)](https://github.com/ome/omero-prometheus-tools/actions)

[![PyPI version](https://badge.fury.io/py/omero-prometheus-tools.svg)](https://badge.fury.io/py/omero-prometheus-tools)

# Tools for monitoring OMERO with Prometheus

This repository is under development.
Breaking changes may be made without warning.

## Installation

```bash
python3 -mvenv /opt/prometheus-omero-tools
/opt/prometheus-omero-tools/bin/pip \
    install \
    https://github.com/glencoesoftware/zeroc-ice-py-linux-x86_64/releases/download/20240202/zeroc_ice-3.6.5-cp310-cp310-manylinux_2_28_x86_64.whl \
    https://github.com/imcf/omero-prometheus-tools/releases/download/v0.3.0.dev0/omero_prometheus_tools-0.3.0.dev0-py3-none-any.whl
```

## Running

```bash
/opt/prometheus-omero-tools/bin/omero-prometheus-tools \
    --server omero.example.org \
    --user public \
    --password S3cr3T \
    [-c /opt/prometheus-omero-tools/etc/prometheus-omero-counts.yml ...]
```

Metrics will be published on <http://localhost:9449>.
