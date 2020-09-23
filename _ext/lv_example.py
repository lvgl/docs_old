from docutils.parsers.rst import Directive
from docutils import nodes
from docutils.parsers.rst.directives.images import Image
from sphinx.directives.code import LiteralInclude
import os

class LvExample(Directive):
    required_arguments = 3
    def run(self):
        example_path = self.arguments[0]
        example_name = os.path.split(example_path)[1]
        node_list = []

        paragraph_node = nodes.raw(text=f"<iframe class='lv-example' src='https://lvgl.github.io/lv_examples/{example_name}/?w=320&h=240'></iframe>", format='html')
        toggle = nodes.container('', literal_block=False, classes=['toggle'])
        header = nodes.container('', literal_block=False, classes=['header'])
        toggle.append(header)
        example_file = os.path.abspath("lv_examples/src/" + example_path + ".c")

        with open(example_file) as f:
            contents = f.read()
            literal_list = nodes.literal_block(contents, contents)
            literal_list['language'] = self.arguments[2]
        toggle.append(literal_list)
        header.append(nodes.paragraph(text="code"))
        node_list.append(paragraph_node)
        node_list.append(toggle)
        return node_list

def setup(app):
    app.add_directive("lv_example", LvExample)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
