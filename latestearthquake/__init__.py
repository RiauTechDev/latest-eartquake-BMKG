import requests
from bs4 import BeautifulSoup
"""
Method = fungsi
Field / Attribute = variabel 
"""

class GempaTerkini:
    def __init__(self, url):
        self.description = 'To get the latest earthquake in Indonesia from bmkg.go.id'
        self.result = None
        self.url = url

    # Extract data from Website
    def data_extraction(self):
        try:
            content = requests.get(self.url)
        except Exception:
            return None

        if content.status_code == 200:
            # Get and assign Date and Time data
            soup = BeautifulSoup(content.text, 'html.parser') #1. INSTATIATION = INSTANSIASI = PENCIPTAAN OBJEK DARI CLASS
            result = soup.find('span', {'class': 'waktu'})
            result = result.text.split(', ')
            date = result[0]
            time = result[1]

            # Get and assign magnitude, depth, ls, bt, location, and perceived data
            result = soup.find('div', {'class', 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
            result = result.findChildren('li')

            i = 0
            magnitude = None
            depth = None
            ls = None
            bt = None
            location = None
            perceived = None

            for res in result:
                if i == 1:
                    magnitude = res.text
                elif i == 2:
                    depth = res.text
                elif i == 3:
                    coordinate = res.text.split(' - ')
                    ls = coordinate[0]
                    bt = coordinate[1]
                elif i == 4:
                    location = res.text
                elif i == 5:
                    perceived = res.text
                i = i + 1

            output = dict()
            output['date'] = date
            output['time'] = time
            output['magnitude'] = magnitude
            output['depth'] = depth
            output['coordinate'] = {'ls': ls, 'bt': bt}
            output['location'] = location
            output['perceived'] = perceived
            self.result = output
        else:
            return None

    # Show the data from extraction

    def show_data(self):
        if self.result is None:
            print('Latest earthquake data is not found')
            return
        print('Latest earthquake based on BMKG')
        print(f"Date: {self.result['date']}")
        print(f"Time: {self.result['time']}")
        print(f"Magnitude: {self.result['magnitude']}")
        print(f"Depth: {self.result['depth']}")
        print(f"Coordinate: LS={self.result['coordinate']['ls']}, BT={self. result['coordinate']['bt']}")
        print(f"Location: {self.result['location']}")
        print(f"Perceived: {self.result['perceived']}")

    def run(self):
        self.data_extraction()
        self.show_data()


if __name__ == '__main__':
    gempa_di_indonesia = GempaTerkini('https://bmkg.go.id')
    print('\nDeskripsi class GempaTerkini', gempa_di_indonesia.description)
    gempa_di_indonesia.run()

    gempa_di_dunia = GempaTerkini('https ://bmkg.go.id')
    print('\nDeskripsi class GempaTerkini', gempa_di_dunia.description)
    gempa_di_dunia.run()
    # gempa_di_indonesia.data_extraction()
    # gempa_di_indonesia.show_data()