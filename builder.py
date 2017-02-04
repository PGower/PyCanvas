import click
import json
from jinja2 import Environment, FileSystemLoader
import os
import importlib
import re


def extract_type(element):
    if 'type' in element:
        if 'format' in element and element['format'] is not None:
            tipe = element['format']
        else:
            tipe = element['type'].lower()

        if tipe == 'void':
            return 'None'
        elif tipe in ['integer', 'int32', 'int64', 'long']:
            return 'int'
        elif tipe in ['double', 'float', 'number']:
            return 'float'
        elif tipe == 'string':
            return 'str'
        elif tipe == 'byte':
            return 'bytearray'
        elif tipe == 'date':
            return 'datetime.date'
        elif tipe == 'datetime':
            return 'datetime.datetime'
        elif tipe == 'boolean':
            return 'bool'
        elif tipe == 'array':
            if 'items' in element:
                subtipe = extract_type(element['items'])
                return '[{}]'.format(subtipe)
            else:
                return '[]'
        elif tipe == 'map':
            if 'key' in element and 'value' in element:
                keytipe = extract_type(element['key'])
                valuetipe = extract_type(element['value'])
                return '{{{}:{}}}'.format(keytipe, valuetipe)
            else:
                return '{}'
    else:
        # No type, check for $ref
        if '$ref' in element:
            return 'model:{}'.format(element['$ref'].capitalize())


def startswith(s, v):
    return str(s).startswith(v)


def required_attributes(m):
    return [r for r in m['required']]


def optional_attributes(m):
    return [r for r in (y for y in m['properties'].keys() if y not in m['required'])]


def fix_param_name(name):
    if name[-1:] == ']':
        return name.replace('[','_').replace(']','')
    else:
        return name


def service_param_string(params):
    """Takes a param section from a metadata class and returns a param string for the service method"""
    p = []
    k = []
    for name, data in params.items():
        name = fix_param_name(name)
        if data['required'] is True:
            p.append(name)
        else:
            if 'default' in data:
                k.append('{name}={default}'.format(name=name, default=data['default']))
            else:
                k.append('{name}=None'.format(name=name))
    p.sort(lambda a,b: len(a) - len(b))
    k.sort()
    a = p + k
    a.append('*args')
    a.append('**kwargs')
    return ', '.join(a)


def metadata_path(name):
    return 'pycanvas/meta/{}.py'.format(name)


def model_path(name):
    return 'pycanvas/models/{}.py'.format(name)


def api_path(name):
    return 'pycanvas/apis/{}.py'.format(name)


def get_jinja_env():
    loader = FileSystemLoader(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates'))
    env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
    env.filters['extract_type'] = extract_type
    env.filters['startswith'] = startswith
    env.filters['required_attributes'] = required_attributes
    env.filters['optional_attributes'] = optional_attributes
    env.filters['service_param_string'] = service_param_string
    env.globals['getattr'] = getattr
    return env


@click.command()
@click.option('--specfile', help='Canvas Swagger Spec (JSON Format)')
def build_metadata_class(specfile):
    """Generate a metadata class for the specified specfile."""
    with open(specfile) as f:
        spec = json.load(f)
        name = os.path.basename(specfile).split('.')[0]
        spec['name'] = name

        env = get_jinja_env()

        metadata_template = env.get_template('metadata.py.jinja2')
        with open('pycanvas/meta/{}.py'.format(name), 'w') as t:
            t.write(metadata_template.render(spec=spec))


@click.command()
@click.option('--metadata', help='Path to the python Model Metadata class')
def build_model_classes(metadata):
    """Generate a model class for any models contained in the specified spec file."""
    i = importlib.import_module(metadata)
    env = get_jinja_env()
    model_template = env.get_template('model.py.jinja2')
    for model in i.models:
        with open(model_path(model.name.lower()), 'w') as t:
            t.write(model_template.render(model_md=model))


@click.command()
@click.option('--metadata', help='Path to the python Service Metadata class')
def build_service_class(metadata):
    """Generate a service class for the service contained in the specified metadata class."""
    i = importlib.import_module(metadata)
    service = i.service
    env = get_jinja_env()
    service_template = env.get_template('service.py.jinja2')
    with open(api_path(service.name.lower()), 'w') as t:
        t.write(service_template.render(service_md=service))


@click.group()
def cli():
    pass


cli.add_command(build_metadata_class)
cli.add_command(build_model_classes)
cli.add_command(build_service_class)


if __name__ == '__main__':
    cli()
