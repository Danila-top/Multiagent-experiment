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

## Integrated reference architecture

The `integrated-agent-001` experiment instantiates the layers in one executable path:

```
                 +--------------------+
                 |   Research Agent   |
                 +----------+---------+
                            |
              +-------------+-------------+
              |                           |
       +------v------+              +-----v------+
       |   Memory    |              | ML Policy  |
       | persistent  |              | verify?    |
       +------+------+              +-----+------+
              |                       |
              |                 +-----v------+
              |                 | Tool Call  |
              |                 |    add     |
              |                 +-----+------+
              |                       |
              +-----------------------+
                                      |
                              +-------v--------+
                              | Independent    |
                              |   Verifier     |
                              +-------+--------+
                                      |
                              +-------v--------+
                              | Memory write   |
                              +----------------+
```

The architecture is deliberately modular: the in-memory model, tool implementation, or ML policy can be replaced without changing the experiment contract.

The ML classifier is a routing component, not a claim about consciousness or general intelligence.
