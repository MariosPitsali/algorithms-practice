# practicing html in python

class Tag(object):
    
    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents
        
        
    def __str__(self):
        return ("{0.start_tag}{0.contents}{0.end_tag}".format(self))
    
    def display(self):
        print (self)

class DocType(Tag):
    
    def __init__(self):
        super().__init__("!DOCTYPE HTML ", "")
        self.end_tag = ''
        
class Head(Tag):
    
    def __init__(self):
        super().__init__("HEAD","")

class Body(Tag):
    def __init__(self):
        super().__init__("BODY", "") #body contents will be built up separately
        self._body_contents = []
        
    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)
    
    def display(self):
        for tag in self._body_contents:
            self.contents += str(tag)
            
        super().display()

        
        
class HtmlDoc(object):
    
    def __init__(self):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()
        
    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)
        
        
        
        
        
        
