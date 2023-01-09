import mock
from mock import patch
from ..ohce import Ohce
from ..utils.ohceBuilder import OhceBuilder

def test():
    """Vérifie que pytest se lance bien"""
    assert 1 == 1


def test_miroir():
    """Test le renvoi en miroir"""
    # Instancie un nouvel objet Ohce
    ohce = OhceBuilder().default()
    # Etant donné une chaîne
    string = "chaine"
    # elle est renvoyé en miroir
    assert ohce.miroir(string) == "eniahc"

def test_palindrome():
  """Test la réponse bien dit lorsqu'un palindrome est donné"""
  ohce = OhceBuilder().default()
  #Création de spy sur la class ohce
  with mock.patch.object(ohce, 'miroir', wraps=ohce.miroir) as spy_miroir:
    with mock.patch.object(ohce, 'congrate', wraps=ohce.congrate) as spy_congrate:
        #Etant donnée un palindrome
        string_palindrome = "kayak" 
        #Call de la fonction palindrome
        ohce.palindrome(string_palindrome)
        #Il est renvoyé
        # & "bien dit est envoyé ensuite"
        spy_miroir.assert_called_once_with(string_palindrome)
        spy_congrate.assert_called_once()


def test_greet():
    """Test le renvoi du bonjour avant toute chose"""
    # quand on lance Ohce
    ohce = OhceBuilder().default()
    spy = mock.Mock(spec=ohce)
    Ohce.__init__(spy)
    # "bonjour" est envoyé avant toute chose
    assert spy.mock_calls == [mock.call.greet()]


def test_salute():
    """Test le renvoi du bonjour après toute chose"""
    # Quand on lance ohce
    ohce = OhceBuilder().default()
    spy = mock.Mock(spec=ohce)
    Ohce.__del__(spy)
	# "Au revoir" est envoyé en dernier
    assert spy.mock_calls == [mock.call.salute()]


def test_palindrome_langue():
    congrat_cases = {
    'english':"Well done !",
    'svenska' : "Det ar bra",
    'french' : "Bien joué !" 
    }
    # Etant donné un user parlant une langue
    for langue in congrat_cases:
        ohce = Ohce(langue)
        # Quand on entre un palindrome
        with mock.patch.object(ohce, 'miroir', wraps=ohce.miroir) as spy_miroir:
            #Etant donnée un palindrome
            string_palindrome = "kayak" 
            #Call de la fonction palindrome
            ohce.palindrome(string_palindrome)
            #Il est renvoyé
            spy_miroir.assert_called_once_with(string_palindrome)
        # "Bien dit" de cette langue est envoyé
        assert ohce.congrate() == congrat_cases[langue]

    return

def test_greet_langue():
    greet_cases = {
    'english':"Good morning",
    'svenska' : "God morgon",
    'french' : "Bonjour"
    }
    
    for langue in greet_cases:
        # Etant donné un user parlant une langue
        ohce = Ohce(langue)
        # Quand on saisit une chaîne
        # Alors "Bonjour" dans cette langue est envoyé avant tout
        assert ohce.greet() == greet_cases[langue]


def test_salute_langue():
    salute_cases = {
    'english':"Goodbye !",
    'svenska' : "Senare",
    'french' : "Au revoir"
    }
    for langue in salute_cases:
        # Etant donne un user parlant une langue
        ohce = Ohce(langue)
        # Quand on saisit une chaîne
        # Alors "Au revoir" dans cette langue est envoyé en dernier
        assert ohce.salute() == salute_cases[langue]


def test_greet_periode():
    # Etant donnee un user parlant une langue
    # Et que la periode de test a journée est <période>
    # Quand on saisit une chaîne
    # Alors "greet" de cette langue à cette période est envoyé avant tout
    return


def test_salute_periode():
    # Etant donne un user parlant une langue
    # Et que la periode de la journée <période>
    # Quand on saisit une chaîne
    # Alors "salute" de cette langue à cette période est envoyé en dernier
    return
