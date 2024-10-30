import click

from nailguard.detectors import get_detectors_names, get_detector
from nailguard.alerts import get_alerts_names, get_alert


@click.command()
@click.option(
    '--detector',
    type=click.Choice(get_detectors_names()),
    default="mediapipe",
    help='Detector to use'
)
@click.option(
    '--alert',
    type=click.Choice(get_alerts_names()),
    multiple=True,
    default=["notification"],
    help='Alerts to use (specify at least once)'
)
def main(detector: str, alert: list[str]):
    """Nailguard launcher"""
    
    print(detector, alert)
    
    detector = get_detector(detector)
    alerts = [get_alert(alert) for alert in alert]
