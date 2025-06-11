from agents import Agent, Runner
from models.business import Business
from dotenv import load_dotenv
from tools.html_writer import write_html_to_file

load_dotenv()

class MetaPaidMediaSpecialist:
    def __init__(self):
        pass

    def create_meta_paid_media_strategy(self, business: Business):

        agent = Agent(
            name="Meta Paid Media Specialist",
            instructions="You are a Meta Paid Media Specialist who creates comprehensive Meta advertising strategies and formats them as professional HTML documents. Focus on Facebook and Instagram platforms, including signals setup, catalog requirements, creative development, and campaign structure. Use the write_html_to_file tool to save your work.",
            tools=[write_html_to_file],
        )

        prompt = f"""
            You are a Meta Paid Media Specialist Agent. Create a comprehensive Meta advertising strategy for the business.
            
            Business Details:
            - Name: {business.businessName}
            - Description: {business.businessDescription}
            - Tagline: {business.tagline}
            - Value Proposition: {business.coreValueProposition}
            - Target Audience: {business.primaryTargetAudience}
            - Demographics: {business.demographics}

            Create a well-formatted HTML document with the Meta paid media strategy. Include the following sections:

            1. Signals Setup
            - Standard Events Implementation (ViewContent, AddToCart, Purchase, etc.)
            - Custom Events Configuration
            - Conversion Tracking Setup

            2. Catalog Requirements
            - Catalog Need Assessment
            - Product Feed Setup (if required)

            3. Creative Development
            - Video Concept 1 (15-30s)
            - Video Concept 2 (15-30s)
            - Video Concept 3 (15-30s)
            For each video concept, include:
            - Storyboard outline
            - Key messaging points
            - Visual style recommendations
            - Call-to-action suggestions

            4. Campaign Structure
            Create a detailed campaign structure with:
            - Campaign objectives
            - Ad set configurations
            - Audience targeting
            - Placements
            - Budget allocation
            - Bid strategies

            Format the strategy as a professional HTML document with:
            - DOCTYPE and HTML tags
            - CSS styling for professional appearance
            - Clear sections and headings
            - Tables, lists, and other HTML elements as needed
            
            Save the strategy as an HTML file using the write_html_to_file tool.
        """
        
        result = Runner.run_sync(agent, prompt)
        print(result.final_output)

if __name__ == "__main__":
    business = Business(
        businessName="SynapseAI",
        businessDescription="An AI-powered business intelligence platform",
        tagline="Transforming Data into Business Intelligence",
        coreValueProposition="AI-driven insights for smarter business decisions",
        primaryTargetAudience="Small to medium-sized businesses",
        demographics="Business owners and managers aged 25-45",
    )
    
    specialist = MetaPaidMediaSpecialist()
    specialist.create_meta_paid_media_strategy(business)