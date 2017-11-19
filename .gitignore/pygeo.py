


import sys
import pygeoip
import socket

def ipRecord(db, targetIP):
    try:
        query = db.record_by_addr(targetIP)
        country = query['country_name']
        city = query['city']
        postal_code = query['postal_code']
        long = query['longitude']
        lat = query['latitude']
        print "Results for: ", targetIP
        print "Country: ", country, "\nCity: ", city, "\nPostal Code: ", postal_code, "\nLongitude: ", long, "\nLatitude: ", lat
    except Exception, e:
        print "Error: ", e

if __name__ == "__main__":
    if len(sys.argv) > 1 :
        kmlname = str(sys.argv[1])
    database = pygeoip.GeoIP('/opt/database/database.dat')
    ip = str(raw_input('Enter Target IP address: '))
    IP = str(socket.gethostbyname(ip))
    ipRecord(database, IP)
