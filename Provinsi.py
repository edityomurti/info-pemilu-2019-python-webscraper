import json

class Provinsi:
	def __init__(self, prov_id, name):
		self.prov_id = prov_id
		self.name = name;

	def toJSON(self):
		return json.dumps(self, default=lambda o:o.__dict__, sort_keys=True, indent=4)