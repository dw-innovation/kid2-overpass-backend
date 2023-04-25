from typing import Dict
import json
import inflect
import pprint

num2word_engine = inflect.engine()


class Template:
    def template(self, area, nodes):
        pass

    def generate_op_query(self, intermediate_query: Dict):
        pass


class SearchWithinTemplate(Template):
    def template(self, area, nodes, edges):
        txt = "(\n"

        first_op = 'node' if len(edges) == 1 else 'way'

        for idx, edge in enumerate(edges):

            loc_from = edge['from']
            loc_to = edge['to']

            props_text = ''.join([f'[{prop}]' for prop in nodes[int(loc_to)]['props']])

            if loc_from == '0':
                txt += f'{first_op}{props_text}({area})->.{num2word_engine.number_to_words(loc_to)};\n'
            else:
                dist = edge['weight']
                txt += f'way(around.{num2word_engine.number_to_words(loc_from)}:{dist}){props_text}->.{num2word_engine.number_to_words(loc_to)};\n'

        txt += ");\nout geom;"
        return txt.strip()

    def generate_op_query(self, intermediate_query: Dict):
        nodes = intermediate_query['nodes']
        objects = []
        for node in nodes:
            if node['type'] == 'area':
                area = node['name']

                if area != 'bbox':
                    area = f'geocodeArea:{area}'
                area = f'{{{{{area}}}}}'
            else:
                objects.append(node)

        edges = intermediate_query['relations']
        txt = self.template(area, nodes, edges)

        return txt


TEMPLATES = {
    'search_within': SearchWithinTemplate()
}
