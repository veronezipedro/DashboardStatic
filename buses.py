import urllib2, argparse, os, sys
from datetime import datetime
import xml.etree.ElementTree
import os, time

service_specs = [('20509', '126')]

for service in service_specs:
        api_key = '0.3003391435305782'
        arrivals_url = 'http://mybusnow.njtransit.com/bustime/eta/getStopPredictionsETA.jsp?route=%s&stop=%s&key=%s'
        submit_url = arrivals_url % (service[1], service[0], api_key)

        try:
            data = urllib2.urlopen(submit_url).read()
        except urllib2.HTTPError, e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            sys.exit('Exiting.')
        except urllib2.URLError, e:
            print 'We failed to reach a server. (internet down?)'
            sys.exit('Exiting.')
        else:
            pass
        arrival_list = []
        e = xml.etree.ElementTree.fromstring(data)

        for atype in e.findall('pre'):
            fields = { }
            for field in atype.getchildren():
                if field.tag not in fields and hasattr(field, 'text'):
                    if field.text is None:
                        fields[field.tag] = ''
                        continue
                    fields[field.tag] = field.text.replace("&nbsp", "")
            arrival_list.append(fields)

        # truncate if more than 2 arrivals so we don't get a sign write bork
        if len(arrival_list) > 2:
            arrival_list = arrival_list[:2]
        else:
            pass

        line2 = ''
        bus_format = '%s min'
        if len(arrival_list) == 0:
            line = 'No service.'
        else:
            for bus in arrival_list:
                if bool(bus) is True:
                    if ';' in bus['pt']:
                        bus['pt'] = '!0!'
                    bus_entry = bus_format % (bus['pt'])
                    line2 = line2 + ' ' + bus_entry
            line1 = datetime.now().strftime('%a') + ' ' + (datetime.now().strftime('%-I:%M %P')) # + ' ' + temp_msg
            lines = []
            lines.append(line1)
            lines.append('#' + bus['rd'] + line2)
            slide = lines[:2]
            line = slide[1]
