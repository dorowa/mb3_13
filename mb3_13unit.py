class FileHTML():
    def __init__(self, output = "screen"):
        self.output = output
        self.fHTML = None
        self.dataObj = None
    def __enter__(self):
        if self.output!="screen":
            self.fHTML = open(self.output,"w")
        return self
    def __exit__(self, type, value, traceback):
        if self.fHTML:
            self.fHTML.close()
        return self
    def write_(self):
        if self.output=="screen":
            print(str(self.dataObj))
        elif self.dataObj:
            self.fHTML.write(str(self.dataObj))
        return

class TopLevelTag:
    def __init__(self, tag):
        self.tag = tag
        self.attributes = {}
        self.children = []
        self.prefix = 0

    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        return self
    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append(f'{attribute}="{value}"')
        attrs = " ".join(attrs)
        if self.children:
            opening = " "*4*self.prefix + f"<{self.tag}" + (bool(attrs) and (" "+f"{attrs}") or "") + ">\n"
            internal = ""
            for child in self.children:
                internal += str(child)
            ending = " "*4*self.prefix + f"</{self.tag}>\n"
            return opening + internal + ending
        else:
            return " "*4*self.prefix + f"<{self.tag}"+(bool(attrs) and " " or "")+f"{attrs}></{self.tag}>\n"


class Tag:
    def __init__(self, tag, is_single=False):
        self.tag = tag
        self.text = ""
        self.attributes = {}
        self.is_single = is_single
        self.children = []
        self.prefix = 0

    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        return self
    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append(f'{attribute}="{value}"')
        attrs = " ".join(attrs)
        if self.children:
            opening = " "*4*self.prefix + f"<{self.tag}" + (bool(attrs) and (" "+f"{attrs}") or "") + ">\n"
            internal = f"{self.text}" + (bool(self.text) and "\n" or "")
            for child in self.children:
                internal += str(child)
            ending = " "*4*self.prefix + f"</{self.tag}>\n"
            return opening + internal + ending
        else:
            if self.is_single:
                return " "*4*self.prefix + f"<{self.tag} {attrs}>\n"
            else:
                return " "*4*self.prefix + f"<{self.tag}"+(bool(attrs) and " " or "")+f"{attrs}>{self.text}</{self.tag}>\n"







