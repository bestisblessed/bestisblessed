# Signal Pipeline

<p align="center">
  <img src="https://img.shields.io/badge/Layout-Architecture%20Flow-black?style=flat-square" alt="layout" />
  <img src="https://img.shields.io/badge/Style-System%20Design-0f766e?style=flat-square" alt="style" />
</p>

```mermaid
flowchart LR
    A["Data Collection"] --> B["Feature and Model Layer"]
    B --> C["Prediction Products"]
    C --> D["Automation and Distribution"]
    D --> E["Execution and Monitoring"]
```

<table>
  <tr>
    <td width="20%"><strong>Stage 1</strong><br>Data Collection</td>
    <td width="80%">
      <a href="https://github.com/bestisblessed/odds-monitoring"><strong>odds-monitoring</strong></a> - line movement and market feed monitoring.<br>
      <a href="https://github.com/bestisblessed/the-fight-predictor-agent"><strong>the-fight-predictor-agent</strong></a> - agent-driven fight data and content automation.
    </td>
  </tr>
  <tr>
    <td width="20%"><strong>Stage 2</strong><br>Feature and Model Layer</td>
    <td width="80%">
      <a href="https://github.com/bestisblessed/ai-templates"><strong>ai-templates</strong></a> - reusable inference and assistant patterns.<br>
      <a href="https://github.com/bestisblessed/ai-local-builds"><strong>ai-local-builds</strong></a> - local model and tool orchestration.<br>
      <a href="https://github.com/bestisblessed/deepseek"><strong>deepseek</strong></a> - alternate model provider integration.
    </td>
  </tr>
  <tr>
    <td width="20%"><strong>Stage 3</strong><br>Prediction Products</td>
    <td width="80%">
      <a href="https://github.com/bestisblessed/mma-ai"><strong>mma-ai</strong></a> - MMA prediction application.<br>
      <a href="https://github.com/bestisblessed/nfl-ai"><strong>nfl-ai</strong></a> - NFL prediction application.<br>
      <a href="https://github.com/bestisblessed/mlb-ai"><strong>mlb-ai</strong></a> - MLB prediction application.
    </td>
  </tr>
  <tr>
    <td width="20%"><strong>Stage 4</strong><br>Automation and Distribution</td>
    <td width="80%">
      <a href="https://github.com/bestisblessed/mma-ai-swift-app"><strong>mma-ai-swift-app</strong></a> - mobile distribution channel for predictions.<br>
      <a href="https://github.com/bestisblessed/oil-ai-dashboard"><strong>oil-ai-dashboard</strong></a> - domain dashboard delivery and monitoring UI.
    </td>
  </tr>
  <tr>
    <td width="20%"><strong>Stage 5</strong><br>Execution and Monitoring</td>
    <td width="80%">
      <a href="https://github.com/bestisblessed/trading-bots-public"><strong>trading-bots-public</strong></a> - public automation strategy scripts and tests.<br>
      <a href="https://github.com/bestisblessed/trading-bots-private"><strong>trading-bots-private</strong></a> - private production execution systems.
    </td>
  </tr>
</table>
