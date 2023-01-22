#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace
from configparser import ConfigParser
from os.path import exists
from sys import exit, stderr

from defaults import Defaults


defaults = Defaults()


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', type=str, help='Override notifier.conf with custom one')
    parser.add_argument('-d', '--dry-run', action='store_true', help='Don\'t send message and print it to stdout instead')
    parser.add_argument('-j', '--jobs', type=str, help='Run only given job(s), jobs are separated by comma (,) character')

    return parser.parse_args()


def main():
    options = parse_args()

    if options.config:
        if not exists(options.config):
            stderr.write('Given config file does not exist.\n')
            return 1
    else:
        for cfg_file in defaults.cfg_locations:
            if exists(cfg_file):
                options.config = cfg_file
                break
        if not options.config:
            stderr.write('Did not find config file in any of: {}.\n'.format(defaults.cfg_locations))
            return 1

    if options.jobs:
        options.jobs = options.jobs.split(',')

    cfg = ConfigParser()
    cfg.read(options.config)

    if not cfg['main']['telegram_apikey']:
        stderr.write('\'telegram_apikey\' is missing in \'[main]\' conf.\n')
        return 1

    main_cfg = cfg['main']
    del cfg['main']
    import pdb; pdb.set_trace()

    return 0


if __name__ == '__main__':
    exit(main())
