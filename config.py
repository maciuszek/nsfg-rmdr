from tinyconf.deserializers import IniDeserializer
from tinyconf.fields import IntegerField, Field, BooleanField
from tinyconf.section import Section


class Config(IniDeserializer):
    patreon_role = IntegerField()
    patreon_server = IntegerField()
    patreon_enabled = BooleanField(default=False)

    dbl_token = Field()

    ignore_bots = BooleanField(default=False)

    DEFAULT = Section(
        patreon_role,
        patreon_server,
        patreon_enabled,
        dbl_token,
        ignore_bots
    )
