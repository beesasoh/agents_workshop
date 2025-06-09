from typing import Optional
from models.business import Business

from agents import Agent, Runner
from dotenv import load_dotenv
from tools.html_writer import write_html_to_file

load_dotenv()

class WebsiteBuilder:
    """A class for building business websites based on business model data."""
    
    def __init__(self):
        pass


    def build(self, business: Business):
        # Agent code goes here
        agent = Agent(
        )
    


if __name__ == "__main__":
    business = Business(
        businessName="SynapseAI",
        businessDescription="An AI-powered business intelligence platform",
        tagline="Transforming Data into Business Intelligence",
        coreValueProposition="AI-driven insights for smarter business decisions",
        primaryTargetAudience="Small to medium-sized businesses",
        demographics="Business owners and managers aged 25-45",
    )
    builder = WebsiteBuilder(business)
    builder.build()