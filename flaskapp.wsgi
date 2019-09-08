import sys
sys.path.insert(0, '/var/www/html/flaskapp')
import site

site.addsitedir('/home/ubuntu/anaconda3/envs/py27/lib/python2.7/site-packages')
from flaskapp import app as application