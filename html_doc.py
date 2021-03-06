# practicing html in python

class Tag(object):
    
    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents
        
        
    def __str__(self):
        return ("{0.start_tag}{0.contents}{0.end_tag}".format(self))
    
    def display(self, file=None):
        print (self, file=file)

class DocType(Tag):
    
    def __init__(self):
        super().__init__("!DOCTYPE HTML ", "")
        self.end_tag = ''
        
class Head(Tag):
    
    def __init__(self, title=None):
        
        super().__init__("HEAD",'')
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)

class Body(Tag):
    def __init__(self):
        super().__init__("BODY", "") #body contents will be built up separately
        self._body_contents = []
        
    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)
    
    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)
            
        super().display(file=file)

        
        
class HtmlDoc(object):
    
    def __init__(self, title=None):
        self._doc_type = DocType()
        self._head = Head(title)
        self._body = Body()
        
    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)
        
    def display(self, file=None):
        self._doc_type.display(file=file)
        print ("<html>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print ("</html>", file=file)
        
        
        
if __name__ == "__main__":
    my_page = HtmlDoc("This is one hell of a document")
    my_page.add_tag('h1', 'Main Heading')
    my_page.add_tag('h2', 'Sub Heading')
    my_page.add_tag('p', 'Paragraph that will appear on the page')
    with open("test.html", 'w') as html_file:
        my_page.display(file=html_file)
