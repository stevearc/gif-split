import fabric.api as fab
from fabric.decorators import roles


fab.env.roledefs = {
    'nimbus': ['stevearc@stevearc.com'],
}


def _version():
    return fab.local('git describe --tags', capture=True)



def bundle():
    fab.local('./dl-deps.sh')
    version = _version()
    fab.local("sed -i -e 's/version=.*/version=\"%s\",/' setup.py" % version)
    fab.local('python setup.py sdist')
    print "Created dist/gif_split-%s.tar.gz" % version


@roles('nimbus')
def deploy():
    bundle()
    version = _version()
    tarball = "gif_split-%s.tar.gz" % version
    fab.put("dist/" + tarball)
    venv = "/envs/gif"
    fab.sudo("if [ ! -e %s ]; then virtualenv %s; fi" % (venv, venv))
    fab.sudo("yes | %s/bin/pip uninstall gif_split || true" % venv)
    fab.sudo("%s/bin/pip install pastescript" % venv)
    fab.sudo("%s/bin/pip install %s" % (venv, tarball))
    fab.put('prod.ini', '/etc/emperor/gif.ini', use_sudo=True)
    fab.sudo("rm %s" % tarball)
    tarball = "gif_split-%s.tar.gz" % version
