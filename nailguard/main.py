import click

from nailguard.detectors import get_detectors_names, get_detector
from nailguard.alerts import get_alerts_names, get_alert
from nailguard.nailguard import Nailguard


@click.command()
@click.option(
    '--detector',
    type=click.Choice(get_detectors_names()),
    multiple=True,
    default=["mediapipe"],
    help='Detector to use'
)
@click.option(
    '--alert',
    type=click.Choice(get_alerts_names()),
    multiple=True,
    default=["notification"],
    help='Alerts to use (specify at least once)'
)
@click.option(
    '--camera',
    type=int,
    default=0,
    help='Camera index'
)
def main(detector: str, alert: list[str], camera: int):
    """Nailguard launcher"""
    
    detectors = [get_detector(detector) for detector in detector]
    alerts = [get_alert(alert) for alert in alert]
    Nailguard(camera, detectors, alerts).run()
