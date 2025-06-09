from pydantic import BaseModel, Field
from typing import Optional

class Business(BaseModel):
    """A data model representing a business entity with its key attributes."""
    
    businessName: str = Field(
        default="",
        description="The official name of the business"
    )
    
    businessDescription: str = Field(
        default="",
        description="A comprehensive description of the business, its mission, and vision"
    )
    
    tagline: str = Field(
        default="BIA-generated tagline",
        description="A catchy and memorable phrase that captures the essence of the business"
    )
    
    coreValueProposition: str = Field(
        default="",
        description="The primary value that the business delivers to its customers"
    )
    
    primaryTargetAudience: str = Field(
        default="",
        description="The main group of customers or users the business aims to serve"
    )
    
    demographics: str = Field(
        default="",
        description="Detailed demographic information about the target audience"
    )
    
    uniqueSellingPoints: str = Field(
        default="",
        description="The distinctive features or benefits that set the business apart from competitors"
    )
    
    initialRevenueModel: str = Field(
        default="",
        description="The primary strategy for generating revenue"
    )

    class Config:
        """Pydantic model configuration."""
        json_schema_extra = {
            "example": {
                "businessName": "SynapseAI",
                "businessDescription": "An AI-powered business intelligence platform",
                "tagline": "Transforming Data into Business Intelligence",
                "coreValueProposition": "AI-driven insights for smarter business decisions",
                "primaryTargetAudience": "Small to medium-sized businesses",
                "demographics": "Business owners and managers aged 25-45",
                "uniqueSellingPoints": "Real-time analytics, predictive insights, easy integration",
                "initialRevenueModel": "Subscription-based SaaS model"
            }
        }
