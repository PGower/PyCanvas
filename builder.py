import subprocess
import os
import shutil
import multiprocessing

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
p = lambda a: os.path.join(BASE_PATH, a)

def process_swagger_def(d):
    with open(d[1], 'w+') as f:
        subprocess.call(d[0], stderr=f, stdout=f)

def main():
    # Create a log dir
    try:
        os.mkdir(p('logs'))
    except OSError:
        shutil.rmtree(p('logs'))
        os.mkdir(p('logs'))

    if os.path.exists(p('pycanvas')):
        shutil.rmtree(p('pycanvas'))
        os.mkdir(p('pycanvas'))
        with open(p('pycanvas/__init__.py'), 'w+') as f:
            f.write('# __init__.py')

    pool = multiprocessing.Pool(processes=4)
    data = []
    results = {}

    for spec in os.listdir(p('specs')):
        name = spec[:spec.find('.json')]
        # setup logging
        os.mkdir(os.path.join(BASE_PATH, 'logs/{}'.format(name)))
        output_path = os.path.join(BASE_PATH, './logs/{name}/{name}.log'.format(name=name))
        subprocess_args = ['java', '-jar', 'swagger-codegen-cli.jar', 'generate', '-i', p('specs/{}'.format(spec)), '-l', 'python', '-o', 'pycanvas/{}'.format(name), '-t', p('templates')]
        data.append((subprocess_args, output_path))

    it = pool.map(process_swagger_def, data)

    pool.close()
    pool.join()

    for api in os.listdir(p('pycanvas')):
        if api == '__init__.py':
            continue
        if os.path.exists(p('pycanvas/{}/__init__.py'.format(api))):
            continue
        destination = p('pycanvas/{}'.format(api))
        source = p('pycanvas/{}/swagger_client'.format(api))
        temporary = p('pycanvas/{}_temp'.format(api))
        shutil.copytree(source, temporary)
        shutil.rmtree(destination)
        os.rename(temporary, destination)
        if not os.path.exists(p('pycanvas/configuration.py')):
            shutil.copyfile(os.path.join(destination, 'configuration.py'), p('pycanvas/configuration.py'))
        if not os.path.exists(p('pycanvas/rest.py')):
            shutil.copyfile(os.path.join(destination, 'rest.py'), p('pycanvas/rest.py'))
        os.remove(os.path.join(destination, 'configuration.py'))
        os.remove(os.path.join(destination, 'rest.py'))


if __name__ == '__main__':
    main()