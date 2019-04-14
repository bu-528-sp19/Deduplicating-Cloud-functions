"""Sanity

Usage:
  sanity.py -h | --help
  sanity.py --version
  sanity.py --i (<input>) (--o <output>) (--f <function/action>)

Options:
  -h --help     Show this screen.
  --version     Show version.
  --i           Sanity Input Bucket
  --o           Sanity Output Bucket
  --f           Function Name

"""
from docopt import docopt
from connectMinio import connect_minio,createBucket
from kafkaConnect import kafka_consumer
from pyfiglet import Figlet

if __name__ == '__main__':
    arguments = docopt(__doc__, version='sanity 1.0')
    f = Figlet(font='slant')
    print(f.renderText('Sanity'))
    #print(arguments)
    input_bucket = arguments.get('<input>')
    output_bucket = arguments.get('<output>')
    function_name = arguments.get('<function>')

    mc = connect_minio()
    createBucket(mc,input_bucket)
    createBucket(mc, output_bucket)
    kafka_consumer("in-bucket-notifications",function_name)

