from agents import Agent, Runner
from models.business import Business
from dotenv import load_dotenv
from tools.html_writer import write_html_to_file

load_dotenv()

class PaidMediaSpecialist:
    def __init__(self):
        pass

    def create_paid_media_strategy(self, business: Business):
        # Agent code goes here
        agent = Agent(
            
        )
        pass

if __name__ == "__main__":
    business = Business(
        businessName="SynapseAI",
        businessDescription="An AI-powered business intelligence platform",
        tagline="Transforming Data into Business Intelligence",
        coreValueProposition="AI-driven insights for smarter business decisions",
        primaryTargetAudience="Small to medium-sized businesses",
        demographics="Business owners and managers aged 25-45",
    )
    
    specialist = PaidMediaSpecialist()
    specialist.create_paid_media_strategy(business)