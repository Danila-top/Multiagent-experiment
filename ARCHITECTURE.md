# Architecture notes

## Conceptual layers

### 1. Agents
Independent AI systems with distinct roles and capabilities.

### 2. Context
Durable project knowledge, experiment logs, and reusable instructions.

### 3. Tools
External capabilities such as repositories, files, databases, deployment platforms, and computer access.

### 4. Coordination
Protocols for assigning work, exchanging artifacts, checking results, and maintaining consistency.

### 5. Evaluation
Tests and observations that separate reproducible behavior from interpretation or hypothesis.

The architecture is intentionally tool-agnostic so individual services can change without invalidating the project documentation.
