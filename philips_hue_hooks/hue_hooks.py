import configargparse

from philips_hue_hooks.action.print_action import PrintAction
from philips_hue_hooks.action.webhook_action import WebHookAction
from philips_hue_hooks.poller import Poller

if __name__ == '__main__':
    parser = configargparse.ArgParser(description='Hook Arguments')

    parser.add('--bridge-host',
               required=True,
               env_var='192.168.1.203',
               help='Hostname/IP address to poll on (for example: 192.168.0.17)')
    parser.add('--username',
               required=True,
               env_var='oK4bBb0BOWX7QgIICIXpSt36EbKXPf9ab2tw6mj1',
               help='Username to use (for example: DjKbc3uiIBf7xleIw08FD3UR7V1vzJGNnfRcDbFv)')
    parser.add('--sensor-ids',
               required=True,
               env_var='7',
               help='Comma-separated list of sensor IDs (for example: 4,9)')
    parser.add('--target',
               action='append',
               env_var='https://maker.ifttt.com/use/bA9mdbLgtK-vRTcpZsisCl',
               help='The WebHook URL(s) to POST to (optional; if absent, will print to stdout)')

    args = parser.parse_known_args()[0]

    host = args.bridge_host
    username = args.username
    sensor_id = [int(i) for i in args.sensor_ids.split(',')]

    actions = []

    if args.target is None:
        actions.append(PrintAction())
    else:
        for target in args.target:
            actions.append(WebHookAction(target))

    poller = Poller(host, username, sensor_id, actions)
    poller.run()
