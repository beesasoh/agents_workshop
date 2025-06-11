from agents import Agent, Runner, WebSearchTool
from models.business import Business

from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

class Innovator:
    def __init__(self):
        pass

    def innovate(self, sector: str) -> Business:

        
        agent = Agent(
            name="Innovator",
            instructions="You are an innovator. You are tasked with coming up with new ideas for the business.",
            output_type=Business,
            tools=[WebSearchTool()],
        )

        prompt = f"""
            You are an innovator. You are tasked with coming up with new ideas in {sector}.
        """

        result = Runner.run_sync(agent, prompt)
        print(result.final_output)
        return result.final_output
        

if __name__ == "__main__":
    innovator = Innovator()
    innovator.innovate("healthcare and wellness")