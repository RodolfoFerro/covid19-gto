import json


class Guanajuato:
    def __init__(self):
        """Loads data structure from JSON files."""

        with open('data/mapdata.json', encoding='utf-8') as json_file:
            self.mapdata = json.load(json_file)

        with open('data/data.json', encoding='utf-8') as json_file:
            self.data = json.load(json_file)

    def generate_map_data(self):
        """Return map data to build in an SVG.
        Map ref:
            https://seseaguanajuato.org/sistema_estatal_anticorrupcion/municipios
        """
        generated_mapdata = []

        for name, mapdata in self.mapdata.items():
            try:
                item_data = self.data['estados'][name]

                if item_data['confirmados']:
                    cls_col = 3
                elif item_data['investigacion']:
                    cls_col = 2
                else:
                    cls_col = 1
            except KeyError as e:
                print(f'KeyError: {str(e)}')
                cls_col = ''

            generated_mapdata.append({
                'name': name,
                'data': mapdata,
                'cls_col': cls_col
            })

        return generated_mapdata


if __name__ == "__main__":
    from pprint import pprint

    gto = Guanajuato()
    print(gto.generate_map_data())
    pprint(gto.data, indent=4)
    pprint(gto.mapdata[11], indent=4)
