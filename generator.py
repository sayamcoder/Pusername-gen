import random
import utils

class UsernameGenerator:
    """
    A class to generate powerful and creative usernames.
    It loads word lists upon initialization and provides methods
    to create usernames based on various patterns.
    """

    def __init__(self):
        """Initializes the generator by loading all necessary word lists."""
        self.adjectives = utils.load_words('adjectives.txt')
        self.nouns = utils.load_words('nouns.txt')
        self.prefixes = utils.load_words('prefixes.txt')
        self.suffixes = utils.load_words('suffixes.txt')

    def _get_random_word(self, word_list):
        """Safely gets a random word from a list, or returns an empty string."""
        return random.choice(word_list) if word_list else ''

    def _apply_transformations(self, username, add_nums, use_leet, separator):
        """Applies optional transformations like numbers and leet speak."""
        if use_leet:
            username = utils.to_leet_speak(username.lower())
        
        if add_nums:
            username += str(random.randint(10, 999))
            
        if separator:
            # Re-introduce the separator after potential lowercasing by leet speak
            username = username.replace(" ", separator)

        return username

    def generate_adj_noun(self, add_nums=False, use_leet=False, use_separator=False):
        """
        Generates a username in the AdjectiveNoun format.
        Example: 'SilentPhoenix', 'Clever_Wolf', 'b4v3ph03n1x'
        """
        adj = self._get_random_word(self.adjectives).capitalize()
        noun = self._get_random_word(self.nouns).capitalize()
        
        # We use a space as a temporary separator to handle it correctly in transformations
        base_username = f"{adj} {noun}"
        
        separator = '_' if use_separator else ''
        
        # If not using leet, we can just join them
        if not use_leet:
            base_username = base_username.replace(" ", separator)

        return self._apply_transformations(base_username, add_nums, use_leet, separator)

    def generate_gamer_tag(self, add_nums=False, use_leet=False, use_separator=False):
        """
        Generates a username in the Prefix-Noun-Suffix format.
        Example: 'xX_Knight_Xx', 'ProGamer', 'DrW0lfYT'
        """
        prefix = self._get_random_word(self.prefixes)
        noun = self._get_random_word(self.nouns).capitalize()
        suffix = self._get_random_word(self.suffixes)
        
        # Temporary space separator
        base_username = f"{prefix} {noun} {suffix}"
        
        separator = '_' if use_separator else ''

        # If not using leet, join them
        if not use_leet:
            base_username = base_username.replace(" ", separator)

        return self._apply_transformations(base_username, add_nums, use_leet, separator)