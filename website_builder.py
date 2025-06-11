from typing import Optional
from models.business import Business

from agents import Agent, Runner
from dotenv import load_dotenv
from tools.html_writer import write_html_to_file

load_dotenv()

class WebsiteBuilder:
    """A class for building business websites based on business model data."""
    
    def __init__(self, business: Business):
        """Initialize the WebsiteBuilder with a business model.
        
        Args:
            business: A Business model instance containing all business information
        """
        self.business = business



    def build(self):

        instructions = f"""
            You are a professional website builder assistant specializing in modern, responsive web design.
            Use Tailwind CSS framework for styling to create beautiful, professional websites.
            Generate HTML content based on user requests and use the write_html_to_file tool to save it to a file.
            Always include proper meta tags, responsive design, and modern UI components.
        """

        agent = Agent(
            name="Website Builder",
            instructions=instructions,
            tools=[write_html_to_file],
        )

        prompt = f"""Create a modern, professional HTML website for {self.business.businessName}.

        Business Details:
        - Name: {self.business.businessName}
        - Description: {self.business.businessDescription}
        - Tagline: {self.business.tagline}
        - Value Proposition: {self.business.coreValueProposition}
        - Target Audience: {self.business.primaryTargetAudience}
        - Demographics: {self.business.demographics}

        Website Requirements:
        1. Modern Design:
           - Use Tailwind CSS for styling
           - Implement a clean, professional layout
           - Include a responsive navigation menu
           - Add smooth animations and transitions
           - Use modern typography and color schemes

        2. Key Sections:
           - Hero section with compelling headline and CTA
           - Features/Benefits section
           - About/Company section
           - Testimonials section (include 3-4 sample testimonials)
           - Pricing/Plans section (if applicable)
           - Contact section with form
           - Footer with social links

        3. Call-to-Actions:
           - Primary CTA buttons for main actions
           - Secondary CTAs for additional engagement
           - Clear value proposition in CTAs

        4. Mobile App Integration:
           - Add app store download buttons (App Store and Google Play)
           - Include app screenshots or mockups
           - Highlight key app features

        5. Additional Features:
           - Social proof elements
           - Trust badges and certifications
           - Newsletter signup
           - Social media integration
           - FAQ section

        Create a professional and modern website that effectively communicates the business details and drives conversions.
        Ensure the design is responsive and works well on all devices.
        Save the file using the write_html_to_file tool."""

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
    builder = WebsiteBuilder(business)
    builder.build()