import os
import configparser

base_dir = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser(interpolation=None,
                allow_no_value=True, delimiters=('='), strict=False)

config_file = os.path.join(base_dir, 'conf', 'f01_configure.ini')

if not os.path.exists(os.path.join(base_dir, 'conf')):
    os.mkdir(os.path.join(base_dir, 'conf'))
if not os.path.exists(config_file) or os.path.isfile(config_file):
    with open(config_file, 'w', encoding='UTF-8') as fd:
        fd.write('[lv1]\nlv2 = Value\n')

config.read(config_file, encoding='UTF-8')

print(config.sections(), '''\t: print(config.sections()''')
for item in config['lv1']:
    print(item, '''\t: print(item)''')

print(config['lv1']['lv2'], '''\t: print(config['lv1']['lv2']''')

config.set('lv1', 'lv3', 'Value')
with open(config_file, 'w', encoding='UTF-8') as configfile:
   config.write(configfile)

with open(config_file, 'r', encoding='UTF-8') as fd:
    line = fd.read()
    print(line)