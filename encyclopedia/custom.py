import re


class CustomMarkdown:
    def __init__(self, entry):
        self.entry = entry

    def convert(self):
        print('custom here')
        print(self.entry)

        h6 = re.compile(r'######\s.+\n')
        matches = h6.finditer(self.entry)
        new_entry = self.entry
        for match in matches:
            match_string = match.group()[6:]
            new_entry = re.sub(match.group(), r'<h6>' + match_string + r'</h6>', new_entry)

        h5 = re.compile(r'#####\s.+\n')
        matches = h5.finditer(self.entry)
        for match in matches:
            match_string = match.group()[5:]
            new_entry = re.sub(match.group(), r'<h5>' + match_string + r'</h5>', new_entry)

        h4 = re.compile(r'####\s.+\n')
        matches = h4.finditer(self.entry)
        for match in matches:
            match_string = match.group()[4:]
            new_entry = re.sub(match.group(), r'<h4>' + match_string + r'</h4>', new_entry)

        h3 = re.compile(r'###\s.+\n')
        matches = h3.finditer(self.entry)
        for match in matches:
            match_string = match.group()[3:]
            new_entry = re.sub(match.group(), r'<h3>' + match_string + r'</h3>', new_entry)

        h2 = re.compile(r'##\s.+\n')
        matches = h2.finditer(self.entry)
        for match in matches:
            match_string = match.group()[2:]
            new_entry = re.sub(match.group(), r'<h2>' + match_string + r'</h2>', new_entry)

        h1 = re.compile(r'#\s.+\n')
        matches = h1.finditer(self.entry)
        for match in matches:
            match_string = match.group()[1:]
            new_entry = re.sub(match.group(), r'<h1>' + match_string + r'</h1>', new_entry)

        return new_entry
