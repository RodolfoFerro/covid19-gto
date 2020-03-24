from pprint import pprint
import json
import re


class Guanajuato:
	def __init__(self):
		"""Loads data structure from JSON files."""

		with open('guanajuato.json') as json_file:
			gto = json_file.read().encode('utf-8')
		self.data = json.loads(gto)

		with open('numbers.json') as json_file:
			totals = json_file.read().encode('utf-8')
		self.totals = json.loads(totals)
	
	def generate_map(self):
		"""Generates an SVG map from self data."""

		base_svg = """
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 534.91 453.27">
				<defs>
					<style>
						path {
							fill: #D4D4D4
						}
						path:hover {
							opacity: 0.4;
						}
						.cls-1 {
							fill:#18BC9C;
						}
						.cls-2 {
							fill:#FCB748;
						}
						.cls-3 {
							fill:#E74C3C;
						}
					</style>
				</defs>
				<g id="COVID-19" data-name="COVID-19">
					{map_str}
				</g>
			</svg>
		"""

		map_str = ""
		for item in self.data:
			if item['infectados']:
				cls_col = 3
			elif item['sospechosos']:
				cls_col = 2
			else:
				cls_col = 1
			map_str += f"""
					<path class="cls-{cls_col}" d="{item['d']}" onmousemove="showTooltip(evt, '{item['municipio']}');" onmouseout="hideTooltip();" />
			"""

		map_svg = re.sub('{map_str}',  map_str,  base_svg)
		
		return map_svg


if __name__ == "__main__":
	gto = Guanajuato()
	print(gto.generate_map())
	pprint(gto.totals, indent=4)
	pprint(gto.data[11], indent=4)
