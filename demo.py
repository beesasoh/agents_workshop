
import asyncio

from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()


capi_agent = Agent(
    name="CAPI Specialist Agent",
    model="gpt-4.1-nano",
    instructions="You provide detailed explanations of Meta signals and conversions API",
    handoff_description="You are an expert in Meta signals and conversions API",
)

catalog_agent = Agent(
    name="Catalog Specialist Agent",
    model="gpt-4.1-nano",
    instructions="You provide detailed explanations of Meta catalog setup, including product tagging, product matching, and product sets",
    handoff_description="You are an expert in Meta catalog setup",
    
)

sales_agent = Agent(
    name="Sales Agent",
    model="gpt-4.1-nano",
    instructions="You determine which agent to use based on the user's question",
    handoffs=[capi_agent, catalog_agent],
)


async def main():
    result = await Runner.run(
        sales_agent,
        "What is the easiest way to set up a catalog for a business?"
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
