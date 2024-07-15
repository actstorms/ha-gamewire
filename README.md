<h3 align="center">Home Assistant Gamewire integration</h3>
<details open="open">
  <summary>Table of Contents</summary>

1. [Sensors](#sensors)
2. [Switches](#switches)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [HACS Installation](#hacs-installation)
4. [Localization](#localization)

</details>

## Sensors

This component will set up the following sensors:

| Platform | Sample sensor               | Description                                                                |
| -------- | --------------------------- | -------------------------------------------------------------------------- |
| `sensor` | `sensor.instance_status` | Sensor with all information of your Gamewire instance                         |

## Switches

This component will set up the following switches:

| Platform | Sample switch                       | Description                                        |
| -------- | ----------------------------------- | -------------------------------------------------- |
| `switch` | `switch.instance_power` | Toggle your Gamewire instance on and off                       |

## Getting Started

### Prerequisites

Use Home Assistant v2023.2.0 or above.

### HACS Installation

You can find it in the default HACS repo. Just search `Gamewire`.

### Integration Setup

- Browse to your Home Assistant instance.
- In the sidebar click on [Configuration](https://my.home-assistant.io/redirect/config).
- From the configuration menu select: [Integrations](https://my.home-assistant.io/redirect/integrations).
- In the bottom right, click on the [Add Integration](https://my.home-assistant.io/redirect/config_flow_start?domain=gamewire) button.
- From the list, search and select “Gamewire”.
- Follow the instruction on screen to complete the set up.
- After completing, the Gamewire integration will be immediately available for use.

## Localization

Currently the integration supports the following languages:

- Danish
- English
- French
- German (Germany)
- Norwegian (bokmål)
- Swedish
- Spanish
- Finnish

If you want to translate the project to your own language, follow the [Localization guide](LOCALIZATION.md).