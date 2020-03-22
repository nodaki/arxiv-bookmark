# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.author import Author
from app.models.paper import Paper
from app.models.tag import Tag
from app.models.conference import Conference
from app.models.paper_author_link import PaperAuthorLink
from app.models.paper_tag_link import PaperTagLink
from app.models.paper_conference_link import PaperConferenceLink
from app.models.bookmark import Bookmark
