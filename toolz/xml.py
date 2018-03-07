from lxml.builder import E
from lxml import etree as ET
A = E.a
I = E.i
B = E.b
def CLASS(v):
            # helper function, 'class' is a reserved word
            return {'class': v}
page = (
            E.html(
                E.head(
                    E.title("This is a sample document")
                ),
                E.body(
                    E.h1("Hello!", CLASS("title")),
                    E.p("肖亮", E.B("bold"), "text in it!"),
                    E.p("This is another paragraph, with a ",
                        A("link", href="http://www.python.org"), "."),
                    E.p("Here are some reserved characters: <spam&egg>."),
                    ET.XML("<p>And finally, here is an embedded XHTML fragment.</p>"),
                )
            )
        )
page=ET.tounicode(page,pretty_print=True)
print(page)
with open('text.xml','w') as p:
    p.write(page)