import csv
import json


class Decathlon:

    def __init__(self):
        self.rows = []
        self.sorted_list = []
    def csv_read(self):
        file = open("test.csv.csv")
        csv_reader = csv.reader(file)

        for row in csv_reader:
            row_string = ''.join(row)
            row_list = row_string.split(';')
            split_time = row_list[10].split('.')
            splite_time_other = split_time[0]+split_time[1]+split_time[2]
            decathlon_data = {
                'name': row_list[0],
                '100m': float(row_list[1]),
                'long_jump': float(row_list[2]),
                'shot_put': float(row_list[3]),
                'high_jump': float(row_list[4]),
                '400m': float(row_list[5]),
                '110_hurdles': float(row_list[6]),
                'disc_throw': float(row_list[7]),
                'pole_vault': float(row_list[8]),
                'javelin_throw': float(row_list[9]),
                '1500m': f"{split_time[int(0)]}:{split_time[int(1)]}.{split_time[int(2)]}",
                'points': 0,
                'place': 0,
                '1500m_other': splite_time_other
            }
            self.rows.append(decathlon_data)

        return self.rows

    def count_points(self):
        sorted_100_meters = sorted(self.rows, key=lambda x: x['100m'])
        sorted_long_jump = sorted(self.rows, key=lambda x: x['long_jump'], reverse=True)
        sorted_shot_put = sorted(self.rows, key=lambda x: x['shot_put'], reverse=True)
        sorted_high_jump = sorted(self.rows, key=lambda x: x['high_jump'], reverse=True)
        sorted_disc_throw = sorted(self.rows, key=lambda x: x['disc_throw'], reverse=True)
        sorted_pole_vault = sorted(self.rows, key=lambda x: x['pole_vault'], reverse=True)
        sorted_javelin_throw = sorted(self.rows, key=lambda x: x['javelin_throw'], reverse=True)
        sorted_400m = sorted(self.rows, key=lambda x: x['400m'])
        sorted_110_hurdles = sorted(self.rows, key=lambda x: x['110_hurdles'])
        sorted_1500m_other = sorted(self.rows, key=lambda x: x['1500m_other'])
        points = 1000
        for place in range(len(self.rows)):
            sorted_100_meters[place]['points'] += points
            sorted_long_jump[place]['points'] += points
            sorted_shot_put[place]['points'] += points
            sorted_high_jump[place]['points'] += points
            sorted_disc_throw[place]['points'] += points
            sorted_pole_vault[place]['points'] += points
            sorted_javelin_throw[place]['points'] += points
            sorted_400m[place]['points'] += points
            sorted_110_hurdles[place]['points'] += points
            sorted_1500m_other[place]['points'] += points
            points -= 100

        return self.rows

    def give_placement(self):
        placement = 1
        sorted_points = sorted(self.rows, key=lambda x: x['points'], reverse=True)
        for place in range(len(self.rows)):
            sorted_points[place]['place'] += placement
            placement += 1
            self.rows[place].popitem()
        self.sorted_list = sorted(self.rows, key=lambda x: x['place'])
        if self.sorted_list[0]['points'] == self.sorted_list[1]['points']:
            self.sorted_list[0]['place'] = "1-2"
            self.sorted_list[1]['place'] = "1-2"
        elif self.sorted_list[1]['points'] == self.sorted_list[2]['points']:
            self.sorted_list[1]['place'] = "2-3"
            self.sorted_list[2]['place'] = "2-3"
        elif self.sorted_list[2]['points'] == self.sorted_list[3]['points']:
            self.sorted_list[2]['place'] = "3-4"
            self.sorted_list[3]['place'] = "3-4"

        return self.rows

    def create_json(self):
        f = open("test.json", "w")

        json.dump(self.sorted_list, f)
        f.close()

dec = Decathlon()
dec.csv_read()
dec.count_points()
dec.give_placement()
dec.create_json()