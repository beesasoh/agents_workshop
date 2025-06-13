from typing import Optional
from models.business import Business

from agents import Agent, Runner
from dotenv import load_dotenv
from tools.html_writer import write_html_to_file

load_dotenv()

class WebsiteBuilder:
    """A class for building business websites based on business model data."""
    
    def build(self, business: Business):

        content_design_agent = Agent(
            name="Content Design Agent",
            model="gpt-4o-mini",
            instructions=f"""
                You are a professional content designer.
                Your task is to buid content for the website for {business}.
                Describe each section of the website and the content that should be in it.
                Must have clear call to actions and a clear value proposition.
                Social proof elements and trust badges and certifications.
            """,
        )

        design_agent = Agent(
            name="Design Agent",
            model="gpt-4o-mini",
            instructions=f"""
                You are a professional website designer.
                Your task is to come up with the best theme colors for the business: {business}.
                Make the colors match the business and the industry. Suggest primary and secondary colors.
            """,
        )

        frontend_agent = Agent(
            name="Frontend Agent",
            model="gpt-4o",
            tools=[write_html_to_file],
            instructions=f"""
                You are a professional frontend developer.
                Your task is to built the best frontend single page website for the business. 
                You will receive the content and theme colors.
                You will use the Bootstrap CSS framework to create the frontend.
                You will use the write_html_to_file tool to save the frontend to a file.
                Always include proper meta tags, responsive design, and modern UI components.
            """,
        )

        content = Runner.run_sync(content_design_agent, f"Design the content for the website for {business}").final_output
        theme = Runner.run_sync(design_agent, f"Design the theme colors for the website for {business}").final_output
        
        Runner.run_sync(frontend_agent, f"Build the frontend for the website with the following content and theme colors: {content} and {theme}").final_output

        print("Website built successfully")


if __name__ == "__main__":
    business = Business(
        businessName="SynapseAI",
        businessDescription="An AI-powered business intelligence platform",
        tagline="Transforming Data into Business Intelligence",
        coreValueProposition="AI-driven insights for smarter business decisions",
        primaryTargetAudience="Small to medium-sized businesses",
        demographics="Business owners and managers aged 25-45",
    )
    builder = WebsiteBuilder()
    builder.build(business)