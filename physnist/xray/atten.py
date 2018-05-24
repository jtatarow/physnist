import requests
from bs4 import BeautifulSoup


class Attenuation:

    def __init__(self, Z):
        self.Z = Z
        self.edges = None
        self.data = None

    def fetch_atten(self):
        base = r'https://physics.nist.gov/PhysRefData/XrayMassCoef/'
        if type(self.Z) is int:
            url = base + 'ElemTab/z' + str(self.Z).zfill(2) + r'.html'
        else:
            url = base + 'ComTab/' + self.Z + '.html'

        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')

        table = soup.find_all('pre')

        data = list()
        edges = dict()

        for line in table[0].contents[-1].split(' \r\n')[3:-1]:
            if len(line.split()) > 3:
                items = line.split()
                edges[items[0]] = float(items[1])
                line = " ".join(items[1:])
            data.append([float(s) for s in line.split()])

        self.edges = edges
        self.data = data
