class Tag:

    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents

    def __str__(self):
        return "{}\n{}\n{}\n".format(self.start_tag, self.contents, self.end_tag)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__("!DOC_TYPE HTML PUBLIC", "")
        self.end_tag = ''
        # doc_type doesn't has a end tag


class Head(Tag):

    def __init__(self, title=None):
        super().__init__("head", "")
        if title:
            self._title_tag = Tag("title", title)
            self.contents = str(self._title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__("body", '')
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc:

    def __init__(self):
        self._doc_type = DocType()
        self._body = Body()
        self._head = Head()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<html>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</html>", file=file)


if __name__ == '__main__':

    my_page = HtmlDoc()
    my_page.add_tag('h1', 'Main heading')
    my_page.add_tag("h2", "Sub heading")
    my_page.add_tag("p", "this is a small paragraph")
    my_page._head.__init__("Document title")

    with open("test.html", "w") as test:
        my_page.display(file=test)

new_body = Body()
new_body.add_tag("h1", "aggregation")
new_body.add_tag("p", "Unlike <strong>Composition</strong> aggregation uses "
                      "existing instances of object to build up another object.")
new_body.add_tag("p", "The composed object doesn't actually own the object that it"
                      " is composed of - if it's destroyed, those "
                      "objects continues to exists.")

# give your document new content by switching it's body.
my_page._body = new_body
with open("test2.html", "w") as test:
    my_page.display(file=test)
