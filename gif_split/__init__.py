from pyramid.config import Configurator


def includeme(config):
    """ Set up and configure the app """
    settings = config.get_settings()
    settings['jinja2.filters'] = {
        'static_url': 'pyramid_jinja2.filters:static_url_filter',
    }
    settings['jinja2.directories'] = ['gif_split:templates']
    config.include('pyramid_jinja2')

    config.add_route('root', '/')

    config.add_static_view(name='static', path='gif_split:static')

    config.scan()


def main(config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('gif_split')
    return config.make_wsgi_app()
