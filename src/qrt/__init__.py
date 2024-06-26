from quart import Quart, session

from qrt.magic import register_blueprints
from qrt.extensions import init_extensions

# types
from .types import Mode, App


def create_app(mode: Mode) -> App:
    """
    Create a new Quart app with the given configuration.
    """
    app = Quart(__name__)
    app.config.from_object(f"qrt.config.{mode.capitalize()}Config")

    init_extensions(app)
    register_blueprints(app)

    @app.before_request
    async def permanent_session():
        session.permanent = True

    return app
