# Workflow

flowchart TD
    A[Start] --> B[Extract Data]
    B --> C{For each commodity}
    C --> D[Fetch commodity data]
    D --> E[Transform Data]
    E --> F[Concatenate Data]
    F --> G[Load Data]
    G --> H[End]

    %% Define the links between the elements
    B -->|Extract| C
    C -->|Data| D
    D -->|Data| E
    E -->|Transformed Data| F
    F -->|Data| G
    G -->|Load Data| H
