"""Generate, update and serve metrics on OMERO."""

from prometheus_client import Gauge, start_http_server
from time import sleep, time
from omero_prometheus_tools import CountMetrics, SessionMetrics


def connect(hostname, username, password):
    client = omero.client(hostname)
    client.setAgent("prometheus-omero-tools")
    client.createSession(username, password)
    return client


def update_metrics(args, g_conn_fail, g_last_login):
    client = connect(args.host, args.user, args.password)
    g_conn_fail.set(0)
    # Don't catch exception, exit on login failure so user knows
    g_last_login.set_to_current_time()

    try:
        if args.config:
            counts = CountMetrics(client, args.config, args.verbose)
        else:
            counts = None
        sessions = SessionMetrics(client, verbose=args.verbose)
        while True:
            starttm = time()
            sessions.update()
            if counts:
                counts.update()
            endtm = time()
            # HQL queries may take a long time
            sleep(max(args.interval + endtm - starttm, 0))
    finally:
        client.closeSession()


def serve_metrics(args):
    # Start up the server to expose the metrics.
    start_http_server(args.listen)

    g_last_login = Gauge(
        "omero_prometheus_tools_agent_login_time",
        "Time of last Prometheus agent login",
    )
    g_conn_fail = Gauge(
        "omero_prometheus_tools_connection_failed",
        "Gauge indicating if connecting to OMERO failed.",
    )


    while True:
        try:
            update_metrics(args, g_conn_fail, g_last_login)
        except:  # noqa: E722  pylint: disable-msg=W0702
            g_conn_fail.set(1)
            sleep(60)

