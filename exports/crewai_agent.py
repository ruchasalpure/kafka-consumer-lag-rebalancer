from crewai import Agent

kafka_consumer_lag_rebalancer = Agent(
    role="Kafka Consumer Lag Rebalancer",
    goal="Deliver high-precision autonomous Kafka Consumer Lag Rebalancer operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
