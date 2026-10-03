# Duties and Responsibilities for Kafka Consumer Lag Rebalancer Agent

## Dual-Control Architecture
Maker:
assignment-optimizer

Checker:
rebalance-stability-checker

## Operational Workflow
1. The Maker (assignment-optimizer) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (rebalance-stability-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
