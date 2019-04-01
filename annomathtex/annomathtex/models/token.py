from abc import ABCMeta, abstractmethod

"""
Each word/identifier in a tex document is a token. A token must be one of those 2.
Punctuation are excluded.
"""

class Token(object, metaclass=ABCMeta):
    def __init__(
                 self,
                 unique_id,
                 type,
                 highlight,
                 content,
                 endline,
                 wikidata_result,
                 word_window=None,
                 arXiv_evaluation_items=None,
                 wikipedia_evaluation_items=None,
                 math_env=None

                 ):
        """
        :param unique_id: uuid.uuid1 object, converted to a string. Needed in template for rendering.
        :param type: String, "Word" or "Identifier". Needed for correct template rendering
        :param highlight: String, color, that the Token should be highlighted in. None if no highlight desired.
        :param content: String, The Word/Identifier itself.
        :param endline: Boolean, needed for page rendering
        """
        self.unique_id = str(unique_id)
        self.unique_id_2 = 'button' + str(unique_id)
        self.unique_id_3 = 'modal' + str(unique_id)
        self.highlight = highlight
        self.content = content
        self.endline = endline
        self.type = type
        self.wikidata_result = wikidata_result
        self.word_window = word_window
        self.arXiv_evaluation_items = arXiv_evaluation_items
        self.wikipedia_evaluation_items = wikipedia_evaluation_items
        self.math_env=math_env


    @abstractmethod
    def get_unique_id(self):
        raise NotImplementedError('must be implemented')

    @abstractmethod
    def get_type(self):
        raise NotImplementedError('must be implemented')

    @abstractmethod
    def get_highlight(self):
        raise NotImplementedError('must be implemented')

    @abstractmethod
    def get_content(self):
        raise NotImplementedError('must be implemented')

    @abstractmethod
    def get_endline(self):
        raise NotImplementedError('must be implemented')

    @abstractmethod
    def set_endline(self, new_endline_val):
        raise NotImplementedError('must be implemented')