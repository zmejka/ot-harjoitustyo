import os

dirname = os.path.dirname(__file__)

class Results:

    def __init__(self, file="results.txt"):
        self.results_file = file

    def load_results(self):
        try:
            results_file = os.path.join(dirname, self.results_file)
            with open(results_file, encoding="utf-8") as game_results:
                loaded_results = []
                lines = game_results.readlines()
                for line in lines:
                    loaded_results.append(line)
                return loaded_results
        except FileNotFoundError:
            loaded_results = self.write_results(("_", "_"))
            return loaded_results

    def write_results(self, result):
        game_results_file = os.path.join(dirname, self.results_file)
        game_results = open(game_results_file, "a")
        game_results.write(str(result[0]))
        game_results.write(",")
        game_results.write(str(result[1]))
        game_results.write("\n")
        game_results.close()
        return result
