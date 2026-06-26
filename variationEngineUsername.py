from difflib import SequenceMatcher

def add_variation(variiation, username, var_type):
	if username in [v["username"] for v in variation]:
		return

	similarity = SequenceMatcher(
		None,
		username,
		variations[0]["original']
	).ration()
