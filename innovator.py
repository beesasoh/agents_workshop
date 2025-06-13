from agents import Agent, Runner, WebSearchTool
from models.business import Business

from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

class Innovator:
    def __init__(self):
        pass

    def innovate(self, sector: str) -> Business:

        ideas_agent = Agent(
            name="Ideas Agent",
            model="gpt-4o-mini",
            instructions=f"""
                You are a brilliant business idea generator. 
                Generate five innovative and practical business ideas in the {sector} sector.
                Each idea should be explained in two concise paragraphs: 
                the first paragraph should describe the concept and how it works, 
                and the second should explain its market potential, target audience, 
                and why it could succeed. Focus on originality, feasibility, and real-world relevance.
            """,
            output_type=list[str],
            # tools=[WebSearchTool()],
        )

        analysis_agent = Agent(
            name="Analysis Agent",
            model="gpt-4o-mini",
            instructions=f"""
                You are a brilliant business idea analyst.
                Analyze the given business ideas and decide which one is the best.
                Return only the best idea. Do not return any other text.
            """,
        )

        research_agent = Agent(
            name="Research Agent",
            model="gpt-4o-mini",
            instructions=f"""
                You are a brilliant business researcher.
                Research the given business idea and come up with a business proposal.
                You must inculude
                - Business Name
                - Business Description
                - Business Model
                - Business Plan
                - Business Strategy
                - Business Goals
            """,
        )

        innovator_agent = Agent(
            name="Business Agent",
            model="gpt-4o-mini",
            instructions=f"""
                You are a brilliant business creator.
                Create a business from the given business proposal.
            """,
            output_type=Business,
        )
        
        ideas = Runner.run_sync(ideas_agent, f"Generate 5 business ideas in the {sector} sector").final_output
        best_idea = Runner.run_sync(analysis_agent, f"Analyze the following business ideas and decide which one is the best: {ideas}").final_output
        research = Runner.run_sync(research_agent, f"Research the given business idea and come up with a business proposal: {best_idea}").final_output
        business = Runner.run_sync(innovator_agent, f"Create a business from the given business proposal: {research}").final_output
        print(business)

        return business


if __name__ == "__main__":
    innovator = Innovator()
    innovator.innovate("healthcare and wellness")