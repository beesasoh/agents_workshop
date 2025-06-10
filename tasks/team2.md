# Team 2: Website Builder Agent (WBA) Designers

## Task Overview
Your team is designing an AI agent called the Website Builder Agent (WBA). This agent is responsible for creating professional websites based on business information provided in a structured format.

## Core Responsibilities
1. Receiving a business object with complete business information
2. Analyzing the business details to determine website requirements
3. Generating a professional website structure and content
4. Creating a visually appealing and functional one page website

## Input Format
```json
{
  "businessName": "SynapseAI",
  "BusinessDescription": "",
  "tagline": "BIA-generated tagline",
  "coreValueProposition": "generated core value prop",
  "primaryTargetAudience": "",
  "demographics": "",
  "uniqueSellingPoints": "",
  "initialRevenueModel": ""
}
```

## Expected Output
The agent should generate:
- A complete website structure
- HTML/CSS code for the website
- Call-to-action elements based on the business model

## Implementation Tips
- Start very simple, maybe with one agent
- Brainstorm different agent roles that can work together to give better results
