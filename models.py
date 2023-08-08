from pydantic import BaseModel
from typing import List
from enum import Enum


class GeneroEnum(str, Enum):
    RPG = "RPG"
    Indie = 'Indie'
    Action = "Action"
    Casual = 'Casual'
    Racing = 'Racing'
    Sports = 'Sports'
    Strategy = "Strategy"
    Adventure = "Adventure"
    Education = 'Education'
    Utilities = 'Utilities'
    Simulation = "Simulation"
    Early_Access = 'Early Access'
    Free_to_Play = 'Free to Play'
    Photo_Editing = 'Photo Editing'
    Web_Publishing = 'Web Publishing'
    Audio_Production = 'Audio Production'
    Massively_Multiplayer = 'Massively Multiplayer'
    Animation_Modeling = 'Animation & amp; Modeling'
    Design_Illustration = 'Design &amp; Illustration'

class SentimentEnum(str, Enum):
    Mixed = 'Mixed'
    Negative = 'Negative'
    Positive = 'Positive'
    Very_Negative = 'Very Negative'
    Very_Positive = 'Very Positive'
    Mostly_Negative = 'Mostly Negative'
    Mostly_Positive = 'Mostly Positive'
    Overwhelmingly_Negative = 'Overwhelmingly Negative'
    Overwhelmingly_Positive = 'Overwhelmingly Positive'