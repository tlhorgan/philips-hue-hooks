from argparse import ArgumentParser

from philips_hue_hooks.action.print_action import PrintAction
from philips_hue_hooks.action.webhook_action import WebHookAction
from philips_hue_hooks.poller import Poller

if __name__ == '__main__':
    parser = ArgumentParser(description='Hook Arguments')

    parser.add_argument('--host',
                        required=True,
                        help='Hostname/IP address to poll on (for example: 192.168.0.17)')
    parser.add_argument('--username',
                        required=True,
                        help='Username to use (for example: DjKbc3uiIBf7xleIw08FD3UR7V1vzJGNnfRcDbFv)')
    parser.add_argument('--sensor_ids',
                        required=True,
                        help='Comma-separated list of sensor IDs (for example: 4,9)')
    parser.add_argument('--target',
                        action='append',
                        help='The WebHook URL(s) to POST to (optional; if absent, will print to stdout)')

    args = parser.parse_args()

    host = args.host
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
