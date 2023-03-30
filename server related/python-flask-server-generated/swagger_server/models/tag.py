# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Tag(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, tag_id: str=None, name: str=None, number_of_questions: int=None, description: str=None):  # noqa: E501
        """Tag - a model defined in Swagger

        :param tag_id: The tag_id of this Tag.  # noqa: E501
        :type tag_id: str
        :param name: The name of this Tag.  # noqa: E501
        :type name: str
        :param number_of_questions: The number_of_questions of this Tag.  # noqa: E501
        :type number_of_questions: int
        :param description: The description of this Tag.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'tag_id': str,
            'name': str,
            'number_of_questions': int,
            'description': str
        }

        self.attribute_map = {
            'tag_id': 'tagId',
            'name': 'Name',
            'number_of_questions': 'NumberOfQuestions',
            'description': 'description'
        }
        self._tag_id = tag_id
        self._name = name
        self._number_of_questions = number_of_questions
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Tag':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Tag of this Tag.  # noqa: E501
        :rtype: Tag
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tag_id(self) -> str:
        """Gets the tag_id of this Tag.


        :return: The tag_id of this Tag.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id: str):
        """Sets the tag_id of this Tag.


        :param tag_id: The tag_id of this Tag.
        :type tag_id: str
        """

        self._tag_id = tag_id

    @property
    def name(self) -> str:
        """Gets the name of this Tag.


        :return: The name of this Tag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Tag.


        :param name: The name of this Tag.
        :type name: str
        """

        self._name = name

    @property
    def number_of_questions(self) -> int:
        """Gets the number_of_questions of this Tag.


        :return: The number_of_questions of this Tag.
        :rtype: int
        """
        return self._number_of_questions

    @number_of_questions.setter
    def number_of_questions(self, number_of_questions: int):
        """Sets the number_of_questions of this Tag.


        :param number_of_questions: The number_of_questions of this Tag.
        :type number_of_questions: int
        """

        self._number_of_questions = number_of_questions

    @property
    def description(self) -> str:
        """Gets the description of this Tag.


        :return: The description of this Tag.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Tag.


        :param description: The description of this Tag.
        :type description: str
        """

        self._description = description
