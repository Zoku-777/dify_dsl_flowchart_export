from pydantic import BaseModel

from const import LANGUAGE_MAPPING


class DifyNode(BaseModel):
    id: str
    title: str
    type: str
    desc: str
    language: str
    local_type: str = ""

    def __init__(
        self,
        id: str,
        title: str,
        type: str,
        desc: str,
        language: str,
        type_jp: str = "",
    ):
        super().__init__(
            id=id, title=title, type=type, desc=desc, language=language, type_jp=type_jp
        )
        node_type_name_dict = LANGUAGE_MAPPING.get(language)
        self.local_type = node_type_name_dict.get(type, "Not definied")
        self.desc = desc.replace("\n", " ")


class DifyNodeEdge(BaseModel):
    source: str
    target: str


class FlowLine(BaseModel):
    text: str
