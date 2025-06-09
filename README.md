# Agents Workshop

A multi-agent system for Meta marketing specialists, featuring specialized agents for CAPI (Conversions API) and Catalog management.

## Features

- **CAPI Specialist Agent**: Expert in Meta signals and conversions API
- **Catalog Specialist Agent**: Expert in Meta catalog setup, product tagging, matching, and product sets
- **Sales Agent**: Intelligent routing agent that determines which specialist to use based on user queries

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd agents_workshop
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```bash
# Add your API keys here
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the demo:
```bash
python demo.py
```

## Project Structure

- `demo.py` - Main demo script showing agent interaction
- `founder.py` - Founder agent implementation
- `website_builder.py` - Website building agent
- `paid_media_specialist.py` - Paid media specialist agent
- `innovator.py` - Innovation agent
- `tools/` - Custom tools and utilities
- `models/` - Model configurations
- `output/` - Generated outputs

## Contributing

Feel free to contribute by adding new agents or improving existing functionality. 