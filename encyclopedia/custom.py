import re


class CustomMarkdown:

    def convert(self, entry):
        """
        Transform the Markdown content to Html content,
        convert the tags: <h1>, <h2>, <h3>, <h4>, <h5>, <h6>
        convert the text-styles: bold, italic, strikethrough, bold and nested italic, all bold and italic
        """
        entry = self._h6(entry)
        entry = self._h5(entry)
        entry = self._h4(entry)
        entry = self._h3(entry)
        entry = self._h2(entry)
        entry = self._h1(entry)

        entry = self._bold_italic_text(entry)
        entry = self._bold_text(entry)
        entry = self._bold_text2(entry)
        entry = self._italic_text(entry)
        entry = self._italic_text2(entry)
        entry = self._mistaken_text(entry)

        return entry

    def _h6(self, entry):
        """
        Format text tht starts with ######, return the text in <h6> tag.
        """
        h6 = re.compile(r'######\s.+\n')
        matches = h6.finditer(entry)
        for match in matches:
            match_string = match.group()[6:]
            entry = re.sub(match.group(), r'<h6>' + match_string + r'</h6>', entry)
        return entry

    def _h5(self, entry):
        """
        Format text tht starts with #####, return the text in <h5> tag.
        """
        h5 = re.compile(r'#####\s.+\n')
        matches = h5.finditer(entry)
        for match in matches:
            match_string = match.group()[5:]
            entry = re.sub(match.group(), r'<h5>' + match_string + r'</h5>', entry)
        return entry

    def _h4(self, entry):
        """
        Format text tht starts with ####, return the text in <h4> tag.
        """
        h4 = re.compile(r'####\s.+\n')
        matches = h4.finditer(entry)
        for match in matches:
            match_string = match.group()[4:]
            entry = re.sub(match.group(), r'<h4>' + match_string + r'</h4>', entry)
        return entry

    def _h3(self, entry):
        """
        Format text tht starts with ###, return the text in <h3> tag.
        """
        h3 = re.compile(r'###\s.+\n')
        matches = h3.finditer(entry)
        for match in matches:
            match_string = match.group()[3:]
            entry = re.sub(match.group(), r'<h3>' + match_string + r'</h3>', entry)
        return entry

    def _h2(self, entry):
        """
        Format text tht starts with ##, return the text in <h2> tag.
        """
        h2 = re.compile(r'##\s.+\n')
        matches = h2.finditer(entry)
        for match in matches:
            match_string = match.group()[2:]
            entry = re.sub(match.group(), r'<h2>' + match_string + r'</h2>', entry)
        return entry

    def _h1(self, entry):
        """
        Format text tht starts with #, return the text in <h1> tag.
        """
        h1 = re.compile(r'#\s.+\n')
        matches = h1.finditer(entry)
        for match in matches:
            match_string = match.group()[1:]
            entry = re.sub(match.group(), r'<h1>' + match_string + r'</h1>', entry)
        return entry

    def _bold_italic_text(self, entry):
        """
        Format text within ***text***, return the text in bold italic type.
        """
        bold_italic_text = re.compile(r'(\*\*\*).+(\*\*\*)')
        matches = bold_italic_text.finditer(entry)
        for match in matches:
            match_string = match.group().strip()[3:-3]
            entry = re.sub('\*\*\*' + match_string + '\*\*\*', r'<b><i>' + match_string + r'</i></b>', entry)
        return entry

    def _bold_text(self, entry):
        """
        Format text within **text**, return the text in bold type.
        """
        bold_text = re.compile(r'(\*\*).+(\*\*)')
        matches = bold_text.finditer(entry)
        for match in matches:
            match_string = match.group().strip()[2:-2]
            entry = re.sub('\*\*' + match_string + '\*\*', r'<b>' + match_string + r'</b>', entry)
        return entry

    def _bold_text2(self, entry):
        """
        Format text within __text__, return the text in bold type.
        """
        bold_text2 = re.compile(r'(__).+(__)')
        matches = bold_text2.finditer(entry)
        for match in matches:
            match_string = match.group().strip()[2:-2]
            entry = re.sub('__' + match_string + '__', r'<b>' + match_string + r'</b>', entry)
        return entry

    def _italic_text(self, entry):
        """
        Format text within *text*, return the text in italic type.
        """
        italic_text = re.compile(r'\*.+\*')
        matches = italic_text.finditer(entry)
        for match in matches:
            match_string = match.group().strip()[1:-1]
            entry = re.sub('\*' + match_string + '\*', r'<i>' + match_string + r'</i>', entry)
        return entry

    def _italic_text2(self, entry):
        """
        Format text within _text_, return the text in italic type.
        """
        italic_text2 = re.compile(r'_.+_')
        matches = italic_text2.finditer(entry)
        for match in matches:
            match_string = match.group().strip()[1:-1]
            entry = re.sub('_' + match_string + '_', r'<i>' + match_string + r'</i>', entry)
        return entry

    def _mistaken_text(self, entry):
        """
        Format text within ~~text~~, return the text in strikethrough type.
        """
        mistaken_text = re.compile(r'~~.+~~')
        matches = mistaken_text.finditer(entry)
        for match in matches:
            match_string = match.group().strip()[2:-2]
            entry = re.sub('~~' + match_string + '~~',
                           r'<span style="text-decoration: line-through">' + match_string + r'</span>', entry)
        return entry
