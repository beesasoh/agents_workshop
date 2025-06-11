from innovator import Innovator
from website_builder import WebsiteBuilder
from paid_media_specialist import MetaPaidMediaSpecialist
class Founder:
    def __init__(self):
        pass

if __name__ == "__main__":
    business = Innovator().innovate("Ai bible chat app")
    WebsiteBuilder(business).build()
    MetaPaidMediaSpecialist().create_meta_paid_media_strategy(business)