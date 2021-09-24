import python_minifier

with open('conways_game_of_life.py', 'w') as f:
	with open('solution.py', 'r') as s:
		f.write(python_minifier.minify(s.read()))
