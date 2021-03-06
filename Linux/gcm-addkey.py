#!/usr/bin/env python3
import configparser
import argparse

parser = argparse.ArgumentParser(description='add keys to hosts in the gcm.conf file')
parser.add_argument('-u', "--username",
                    help="the username to use",
                    default="")
targs = vars(parser.parse_args())

config = configparser.ConfigParser()
config.read('/home/endavis/src/wk/gcm/gcm.conf')

sshhosts = []

for section in config.sections():
    if 'host' in section:
        if 'Linux' in config[section]['group']:
            if 'username' in targs and targs['username']:
                sshhosts.append('%s@%s'% (targs['username'], config[section]['host']))

            elif config[section]['user']:
                sshhosts.append('%s@%s'% (config[section]['user'], config[section]['host']))

            else:
                sshhosts.append(config[section]['host'])

tfile = open('add-keys.sh', 'w')

for host in sshhosts:
  tfile.write('ssh-copy-id %s\n' % host)

tfile.close()
