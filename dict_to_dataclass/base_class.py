import json

from dict_to_dataclass import dataclass_from_dict


class DataclassFromDict:
    """A base class for dataclasses that can be created using `dataclass_from_dict`"""

    @classmethod
    def from_dict(cls, origin_dict: dict):
        """Init an instance of this dataclass from a dictionary"""
        return dataclass_from_dict(cls, origin_dict)

    @classmethod
    def from_json(cls, json_str: str):
        """Init an instance of this dataclass from a JSON string"""
        return cls.from_dict(json.loads(json_str))
